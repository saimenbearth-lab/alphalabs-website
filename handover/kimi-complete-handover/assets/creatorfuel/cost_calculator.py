#!/usr/bin/env python3
"""
CreatorFuel Cost Calculator
Berechnet API-Kosten und erstellt Ubersichten fur Business-Planung.

Usage:
    python cost_calculator.py                    # Zeigt Kostenubersicht
    python cost_calculator.py --scenario         # Business-Szenario berechnen
    python cost_calculator.py --excel            # Excel-CSV exportieren
"""

import os
import sys
import argparse
from typing import Dict, List
from datetime import datetime


# Preise pro 1K Tokens (OpenAI, Stand 2024)
MODEL_PRICING = {
    "gpt-4o-mini": {
        "input_per_1k": 0.00015,
        "output_per_1k": 0.00060,
        "name": "GPT-4o Mini (empfohlen)"
    },
    "gpt-4o": {
        "input_per_1k": 0.00250,
        "output_per_1k": 0.01000,
        "name": "GPT-4o (Premium)"
    },
    "gpt-4": {
        "input_per_1k": 0.03000,
        "output_per_1k": 0.06000,
        "name": "GPT-4 (Legacy)"
    },
    "gpt-3.5-turbo": {
        "input_per_1k": 0.00050,
        "output_per_1k": 0.00150,
        "name": "GPT-3.5 Turbo (Budget)"
    }
}

# Geschatzte Token-Verbrauche pro Post (basierend auf Benchmarks)
ESTIMATED_TOKENS = {
    "style_analysis": {
        "input": 2000,      # 20 Posts x ~100 Worter
        "output": 1500      # JSON Style-Profile
    },
    "trend_research": {
        "input": 500,
        "output": 800
    },
    "post_generation": {
        "input": 1200,      # Prompt mit Style-Profile + Trends
        "output": 1000      # 3-5 Posts als JSON
    }
}


def calculate_post_cost(model: str, num_posts: int = 1, platform_factor: float = 1.0) -> Dict:
    """
    Berechnet die Kosten fur die Generierung von Posts.

    Args:
        model: Modell-Name (gpt-4o-mini, gpt-4o, etc.)
        num_posts: Anzahl der Posts
        platform_factor: Multiplikator fur komplexere Plattformen

    Returns:
        Dict mit Kosten-Details
    """
    pricing = MODEL_PRICING.get(model, MODEL_PRICING["gpt-4o-mini"])

    # Style Analysis (einmalig pro Batch)
    style_input = ESTIMATED_TOKENS["style_analysis"]["input"]
    style_output = ESTIMATED_TOKENS["style_analysis"]["output"]
    style_cost = ((style_input / 1000) * pricing["input_per_1k"] +
                  (style_output / 1000) * pricing["output_per_1k"])

    # Trend Research (einmalig pro Batch)
    trend_input = ESTIMATED_TOKENS["trend_research"]["input"]
    trend_output = ESTIMATED_TOKENS["trend_research"]["output"]
    trend_cost = ((trend_input / 1000) * pricing["input_per_1k"] +
                  (trend_output / 1000) * pricing["output_per_1k"])

    # Post Generation (pro Post)
    post_input = ESTIMATED_TOKENS["post_generation"]["input"] * platform_factor
    post_output = ESTIMATED_TOKENS["post_generation"]["output"] * platform_factor
    post_cost = ((post_input / 1000) * pricing["input_per_1k"] +
                 (post_output / 1000) * pricing["output_per_1k"])

    # Gesamtkosten
    total_style = style_cost
    total_trend = trend_cost
    total_posts = post_cost * num_posts
    grand_total = total_style + total_trend + total_posts

    return {
        "model": model,
        "model_name": pricing["name"],
        "num_posts": num_posts,
        "platform_factor": platform_factor,
        "style_analysis": {
            "input_tokens": style_input,
            "output_tokens": style_output,
            "cost_usd": round(style_cost, 4)
        },
        "trend_research": {
            "input_tokens": trend_input,
            "output_tokens": trend_output,
            "cost_usd": round(trend_cost, 4)
        },
        "per_post": {
            "input_tokens": int(post_input),
            "output_tokens": int(post_output),
            "cost_usd": round(post_cost, 4)
        },
        "total": {
            "style_usd": round(total_style, 4),
            "trend_usd": round(total_trend, 4),
            "posts_usd": round(total_posts, 4),
            "grand_total_usd": round(grand_total, 4),
            "grand_total_eur": round(grand_total * 0.92, 4),
            "cost_per_post_usd": round(grand_total / max(num_posts, 1), 4),
            "cost_per_post_eur": round(grand_total * 0.92 / max(num_posts, 1), 4)
        }
    }


def print_cost_comparison():
    """Zeigt eine Kostenvergleichstabelle fur alle Modelle."""
    print("=" * 70)
    print("  CREATORFUEL KOSTENVERGLEICH")
    print("=" * 70)
    print(f"\nSzenario: 5 Posts generieren (inkl. Style-Analyse + Trends)")
    print("-" * 70)

    print(f"\n{'Modell':<25} {'Kosten/Post':<15} {'Gesamt (5 Posts)':<20} {'In EUR'}")
    print("-" * 70)

    for model_key, pricing in MODEL_PRICING.items():
        result = calculate_post_cost(model_key, num_posts=5)
        total = result["total"]

        print(f"{pricing['name']:<25} "
              f"${total['cost_per_post_usd']:<14.4f} "
              f"${total['grand_total_usd']:<19.4f} "
              f"~{total['grand_total_eur']:.2f} EUR")

    print("-" * 70)
    print("\nEmpfehlung: GPT-4o Mini fur den Produktivbetrieb")
    print("            GPT-4o fur Premium-Creator (hochwertigere Outputs)")
    print("\nHinweis: Preise sind Schatzungen. Tatsachliche Kosten konnen leicht variieren.")


def calculate_business_scenario(
    num_creators: int = 10,
    posts_per_day: int = 5,
    days_per_month: int = 22,
    model: str = "gpt-4o-mini"
) -> Dict:
    """
    Berechnet ein Business-Szenario fur mehrere Kunden.

    Args:
        num_creators: Anzahl Creators (Kunden)
        posts_per_day: Posts pro Tag pro Creator
        days_per_month: Arbeitstage pro Monat
        model: Verwendetes Modell

    Returns:
        Dict mit Business-Metriken
    """
    total_posts_month = num_creators * posts_per_day * days_per_month

    # Kosten pro Tag pro Creator
    daily_cost = calculate_post_cost(model, num_posts=posts_per_day)
    daily_per_creator = daily_cost["total"]["grand_total_usd"]

    # Monatliche Kosten
    monthly_total = daily_per_creator * num_creators * days_per_month
    monthly_per_creator = daily_per_creator * days_per_month

    # Empfohlener Verkaufspreis (3x Kosten = 66% Marge)
    recommended_price_per_creator = monthly_per_creator * 3

    # Alternative Preismodelle
    price_per_post = daily_cost["total"]["cost_per_post_usd"] * 3

    return {
        "scenario": {
            "creators": num_creators,
            "posts_per_day": posts_per_day,
            "days_per_month": days_per_month,
            "model": model,
            "model_name": MODEL_PRICING[model]["name"]
        },
        "monthly_totals": {
            "total_posts": total_posts_month,
            "api_costs_usd": round(monthly_total, 2),
            "api_costs_eur": round(monthly_total * 0.92, 2)
        },
        "per_creator_monthly": {
            "posts": posts_per_day * days_per_month,
            "api_cost_usd": round(monthly_per_creator, 2),
            "api_cost_eur": round(monthly_per_creator * 0.92, 2),
            "recommended_price_usd": round(recommended_price_per_creator, 2),
            "recommended_price_eur": round(recommended_price_per_creator * 0.92, 2),
            "profit_margin_usd": round(recommended_price_per_creator - monthly_per_creator, 2),
            "profit_margin_percent": 66.7
        },
        "per_post": {
            "api_cost_usd": round(daily_cost["total"]["cost_per_post_usd"], 4),
            "api_cost_eur": round(daily_cost["total"]["cost_per_post_eur"], 4),
            "retail_price_usd": round(price_per_post, 2),
            "retail_price_eur": round(price_per_post * 0.92, 2)
        }
    }


def print_business_scenario(scenario: Dict):
    """Gibt ein Business-Szenario formatiert aus."""
    s = scenario["scenario"]
    m = scenario["monthly_totals"]
    p = scenario["per_creator_monthly"]

    print("\n" + "=" * 70)
    print("  BUSINESS-SZENARIO")
    print("=" * 70)
    print(f"\nParameter:")
    print(f"  Creator (Kunden):    {s['creators']}")
    print(f"  Posts/Tag/Creator:   {s['posts_per_day']}")
    print(f"  Arbeitstage/Monat:   {s['days_per_month']}")
    print(f"  Modell:              {s['model_name']}")

    print(f"\n{'='*70}")
    print(f"  MONATLICHE GESAMTZAHLEN")
    print(f"{'='*70}")
    print(f"  Gesamt-Posts/Monat:      {m['total_posts']:,}")
    print(f"  API-Gesamtkosten:        ${m['api_costs_usd']:.2f} (~{m['api_costs_eur']:.2f} EUR)")

    print(f"\n{'='*70}")
    print(f"  PRO CREATOR / MONAT")
    print(f"{'='*70}")
    print(f"  Posts/Monat:             {p['posts']}")
    print(f"  API-Kosten:              ${p['api_cost_usd']:.2f} (~{p['api_cost_eur']:.2f} EUR)")
    print(f"\n  EMPFOHLENER VERKAUFSPREIS:")
    print(f"  Preis/Creator/Monat:     ${p['recommended_price_usd']:.2f} (~{p['recommended_price_eur']:.2f} EUR)")
    print(f"  Marge/Creator:           ${p['profit_margin_usd']:.2f} ({p['profit_margin_percent']:.0f}%)")

    print(f"\n{'='*70}")
    print(f"  GESAMTGEWINN")
    print(f"{'='*70}")
    total_revenue = p['recommended_price_usd'] * s['creators']
    total_profit = p['profit_margin_usd'] * s['creators']
    print(f"  Gesamtumsatz/Monat:      ${total_revenue:.2f} (~{total_revenue * 0.92:.2f} EUR)")
    print(f"  Gesamtgewinn/Monat:      ${total_profit:.2f} (~{total_profit * 0.92:.2f} EUR)")


def generate_csv_report(output_path: str = None):
    """Generiert eine CSV-Datei mit Kostenubersichten."""
    if output_path is None:
        output_path = "/mnt/agents/output/creatorfuel/cost_report.csv"

    scenarios = [
        (1, 3),   # 1 Creator, 3 Posts/Tag
        (1, 5),   # 1 Creator, 5 Posts/Tag
        (5, 3),   # 5 Creators, 3 Posts/Tag
        (5, 5),   # 5 Creators, 5 Posts/Tag
        (10, 3),  # 10 Creators, 3 Posts/Tag
        (10, 5),  # 10 Creators, 5 Posts/Tag
        (25, 5),  # 25 Creators, 5 Posts/Tag
        (50, 5),  # 50 Creators, 5 Posts/Tag
    ]

    lines = []
    lines.append("Creator,Posts/Tag,Modell,Posts/Monat,API-Kosten (USD),API-Kosten (EUR),"
                 "Verkaufspreis (USD),Verkaufspreis (EUR),Marge (USD),Marge (EUR),Marge %")

    for model_key in ["gpt-4o-mini", "gpt-4o"]:
        for creators, posts_per_day in scenarios:
            result = calculate_business_scenario(
                num_creators=creators,
                posts_per_day=posts_per_day,
                model=model_key
            )
            s = result["scenario"]
            m = result["monthly_totals"]
            p = result["per_creator_monthly"]

            for scope in ["total", "per_creator"]:
                if scope == "total":
                    lines.append(f"{creators},{posts_per_day},{model_key},"
                               f"{m['total_posts']},{m['api_costs_usd']:.2f},{m['api_costs_eur']:.2f},"
                               f"{p['recommended_price_usd'] * creators:.2f},"
                               f"{p['recommended_price_eur'] * creators:.2f},"
                               f"{p['profit_margin_usd'] * creators:.2f},"
                               f"{p['profit_margin_usd'] * creators * 0.92:.2f},"
                               f"{p['profit_margin_percent']:.1f}")
                else:
                    lines.append(f"1 Creator,{posts_per_day},{model_key},"
                               f"{p['posts']},{p['api_cost_usd']:.2f},{p['api_cost_eur']:.2f},"
                               f"{p['recommended_price_usd']:.2f},"
                               f"{p['recommended_price_eur']:.2f},"
                               f"{p['profit_margin_usd']:.2f},"
                               f"{p['profit_margin_usd'] * 0.92:.2f},"
                               f"{p['profit_margin_percent']:.1f}")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\nCSV-Report gespeichert: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="CreatorFuel Cost Calculator")
    parser.add_argument("--scenario", "-s", action="store_true",
                        help="Business-Szenario berechnen")
    parser.add_argument("--creators", "-c", type=int, default=10,
                        help="Anzahl Creators im Szenario")
    parser.add_argument("--posts-per-day", "-ppd", type=int, default=5,
                        help="Posts pro Tag")
    parser.add_argument("--model", "-m", default="gpt-4o-mini",
                        choices=list(MODEL_PRICING.keys()),
                        help="Modell fur Kalkulation")
    parser.add_argument("--excel", "-e", action="store_true",
                        help="CSV-Report exportieren")
    parser.add_argument("--output", "-o", help="Ausgabepfad fur CSV")

    args = parser.parse_args()

    # Zeige immer den Basis-Vergleich
    print_cost_comparison()

    # Business-Szenario
    if args.scenario:
        scenario = calculate_business_scenario(
            num_creators=args.creators,
            posts_per_day=args.posts_per_day,
            model=args.model
        )
        print_business_scenario(scenario)

    # CSV Export
    if args.excel:
        generate_csv_report(args.output)

    print("\n" + "=" * 70)
    print("  ZIEL-KOSTEN:")
    print("  - GPT-4o Mini: <$0.50 pro Post")
    print("  - GPT-4o:      <$2.00 pro Post")
    print("=" * 70)


if __name__ == "__main__":
    main()
