#!/usr/bin/env python3
"""
CreatorFuel Trend Injector
Recherchiert aktuelle Trends fuer Social-Media-Plattformen.
Kann mit Web-Suche (SERP API) oder ohne API arbeiten (Fallback).

Usage:
    python trend_injector.py --niche fitness --platform TikTok
    python trend_injector.py --niche business --platform Instagram --save
"""

import os
import sys
import json
import argparse
from datetime import datetime
from typing import Dict, List, Optional

# Versuche requests zu importieren
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    print("Hinweis: 'requests' nicht installiert. Verwende Fallback-Modus.")


# SerpAPI Key (optional - fuer echte Trend-Recherche)
SERP_API_KEY = os.getenv("SERP_API_KEY", "")

# Fallback: Statische Trend-Datenbank (wird regelmaessig aktualisiert)
FALLBACK_TRENDS = {
    "fitness": {
        "TikTok": {
            "hashtags": ["#gymtok", "#fitnesstips", "#muskelaufbau", "#homeworkout", "#fitnessmotivation", "#workoutroutine", "#gymlife"],
            "sounds": ["Original Sound - FitnessBeats", "Gym Motivation Remix"],
            "formats": ["Before/After Transformation", "Day in the Life", "Form Check", "Meal Prep"],
            "topics": ["Progress nicht Perfektion", "Form ueber Gewicht", "Rest Days", "Meal Prep Sonntag"]
        },
        "Instagram": {
            "hashtags": ["#fitness", "#gymmotivation", "#fitnessjourney", "#workout", "#fitnesslifestyle", "#bodybuilding", "#fitfam"],
            "formats": ["Carousel Tips", "Reels Transformation", "Story Q&A", "Before/After"],
            "topics": ["Gym Tips", "Healthy Recipes", "Motivation Monday", "Transformation Tuesday"]
        },
        "YouTube Shorts": {
            "hashtags": ["#Shorts", "#fitness", "#gym", "#workout", "#musclegrowth"],
            "topics": ["Quick Tips", "Myth Debunking", "Exercise Form", "Fitness Hacks"]
        }
    },
    "business": {
        "TikTok": {
            "hashtags": ["#businesstips", "#entrepreneur", "#startup", "#makemoneyonline", "#passiveincome", "#businessmindset"],
            "formats": ["Day in the Life", "Myth Debunking", "Tips & Tricks", "Story Time"],
            "topics": ["Produktivitaet", "Mindset", "Skalierung", "Automation"]
        },
        "Instagram": {
            "hashtags": ["#business", "#entrepreneurship", "#success", "#motivation", "#businessowner", "#hustle"],
            "formats": ["Carousel Tips", "Quote Post", "Story Q&A", "Behind the Scenes"],
            "topics": ["Productivity Hacks", "Business Mindset", "Growth Strategies", "Passive Income"]
        },
        "YouTube Shorts": {
            "hashtags": ["#Shorts", "#business", "#money", "#success"],
            "topics": ["Quick Business Tips", "Money Myths", "Entrepreneur Advice"]
        }
    },
    "tech": {
        "TikTok": {
            "hashtags": ["#techtok", "#coding", "#programming", "#developer", "#ai", "#technology"],
            "formats": ["Tutorial", "Day in the Life", "Tips & Tricks", "Review"],
            "topics": ["KI-Tools", "Coding Tips", "Tech Reviews", "Developer Life"]
        },
        "Instagram": {
            "hashtags": ["#tech", "#coding", "#programmer", "#developer", "#technology", "#ai"],
            "formats": ["Carousel Tips", "Reels Tutorial", "Story Poll", "Code Snippet"],
            "topics": ["Coding Tips", "AI Tools", "Tech News", "Developer Productivity"]
        },
        "YouTube Shorts": {
            "hashtags": ["#Shorts", "#tech", "#coding", "#ai"],
            "topics": ["Quick Tutorials", "AI News", "Coding Hacks"]
        }
    },
    "lifestyle": {
        "TikTok": {
            "hashtags": ["#lifestyle", "#motivation", "#selfcare", "#mindset", "#personalgrowth", "#habits"],
            "formats": ["Day in the Life", "Routine", "Tips & Tricks", "Story Time"],
            "topics": ["Morgenroutine", "Gewohnheiten", "Mindset", "Self-Care"]
        },
        "Instagram": {
            "hashtags": ["#lifestyle", "#motivation", "#selfcare", "#mindset", "#goals", "#inspiration"],
            "formats": ["Aesthetic Post", "Carousel Tips", "Story Q&A", "Reel Routine"],
            "topics": ["Morning Routine", "Habit Building", "Mindset Tips", "Goal Setting"]
        },
        "YouTube Shorts": {
            "hashtags": ["#Shorts", "#lifestyle", "#motivation", "#habits"],
            "topics": ["Quick Tips", "Routine Ideas", "Motivation Hacks"]
        }
    }
}


def search_trends_serpapi(niche: str, platform: str) -> List[Dict]:
    """
    Recherchiert Trends ueber SerpAPI (Google Trends).
    Erfordert SERP_API_KEY in Umgebungsvariablen.
    """
    if not SERP_API_KEY or not HAS_REQUESTS:
        return []

    try:
        url = "https://serpapi.com/search"
        params = {
            "engine": "google_trends_trending_now",
            "geo": "DE",
            "api_key": SERP_API_KEY
        }

        response = requests.get(url, params=params, timeout=30)
        data = response.json()

        trends = []
        for item in data.get("trending_searches", [])[:10]:
            trends.append({
                "topic": item.get("query", ""),
                "hashtag": f"#{item.get('query', '').replace(' ', '')}",
                "volume": item.get("search_volume", "N/A"),
                "source": "google_trends"
            })

        return trends

    except Exception as e:
        print(f"SERPAPI-Fehler: {e}")
        return []


def get_platform_trends(platform: str, niche: str = "general") -> List[Dict]:
    """
    Holt Trends fuer eine Plattform und Nische.
    Kombiniert API-Daten mit Fallback-Daten.

    Args:
        platform: Plattform-Name (TikTok/Instagram/YouTube Shorts)
        niche: Themen-Nische

    Returns:
        Liste von Trend-Dictionaries
    """
    trends = []

    # Versuche API-basierte Suche
    api_trends = search_trends_serpapi(niche, platform)
    trends.extend(api_trends)

    # Fallback-Daten hinzufuegen
    niche_lower = niche.lower()
    platform_lower = platform.lower()

    # Finde passende Nische in Fallback-Datenbank
    niche_data = None
    for key in FALLBACK_TRENDS:
        if key in niche_lower:
            niche_data = FALLBACK_TRENDS[key]
            break

    if not niche_data:
        # Verwende 'lifestyle' als generischen Fallback
        niche_data = FALLBACK_TRENDS.get("lifestyle", {})

    # Plattform-Daten holen
    platform_data = niche_data.get(platform, niche_data.get("TikTok", {}))

    # Hashtags
    for hashtag in platform_data.get("hashtags", []):
        trends.append({
            "topic": hashtag.replace("#", ""),
            "hashtag": hashtag,
            "type": "hashtag",
            "source": "fallback"
        })

    # Formate
    for fmt in platform_data.get("formats", []):
        trends.append({
            "topic": fmt,
            "hashtag": f"#{fmt.replace(' ', '').replace('/', '')}",
            "type": "format",
            "source": "fallback"
        })

    # Topics
    for topic in platform_data.get("topics", []):
        trends.append({
            "topic": topic,
            "hashtag": f"#{topic.replace(' ', '').replace('/', '').replace('-', '')}",
            "type": "topic",
            "source": "fallback"
        })

    # Entferne Duplikate
    seen = set()
    unique_trends = []
    for t in trends:
        key = t.get("hashtag", t.get("topic", ""))
        if key and key not in seen:
            seen.add(key)
            unique_trends.append(t)

    return unique_trends


def format_trends_for_prompt(trends: List[Dict]) -> str:
    """
    Formatiert Trends fuer die Nutzung im KI-Prompt.

    Args:
        trends: Liste von Trend-Dictionaries

    Returns:
        Formatierte Trend-Text
    """
    if not trends:
        return "Nutze aktuelle, relevante Trends fuer die Nische."

    lines = []
    lines.append("AKTUELLE TRENDS FUER DIESE PLATTFORM:")
    lines.append("")

    # Hashtags
    hashtags = [t["hashtag"] for t in trends if t.get("type") == "hashtag"][:10]
    if hashtags:
        lines.append(f"Trending Hashtags: {', '.join(hashtags)}")

    # Formate
    formats = [t["topic"] for t in trends if t.get("type") == "format"][:5]
    if formats:
        lines.append(f"Virale Formate: {', '.join(formats)}")

    # Topics
    topics = [t["topic"] for t in trends if t.get("type") == "topic"][:5]
    if topics:
        lines.append(f"Trending Topics: {', '.join(topics)}")

    # API-Trends mit Volume
    api_trends = [t for t in trends if t.get("source") == "google_trends"][:5]
    if api_trends:
        lines.append("")
        lines.append("Google Trends (aktuell):")
        for t in api_trends:
            lines.append(f"  - {t['topic']} ({t.get('volume', 'N/A')} Suchen)")

    return "\n".join(lines)


def save_trends(trends: List[Dict], niche: str, output_dir: str = None) -> str:
    """Speichert Trends als JSON-Datei."""
    if output_dir is None:
        output_dir = os.getenv("OUTPUT_DIR", "/mnt/agents/output/creatorfuel/posts")

    date_str = datetime.now().strftime("%Y-%m-%d")
    trend_dir = os.path.join(output_dir, date_str, "trends")
    os.makedirs(trend_dir, exist_ok=True)

    filename = f"{niche.lower().replace(' ', '_')}_trends.json"
    filepath = os.path.join(trend_dir, filename)

    trend_data = {
        "date": date_str,
        "niche": niche,
        "trends": trends
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(trend_data, f, ensure_ascii=False, indent=2)

    return filepath


def print_trends(trends: List[Dict], niche: str, platform: str):
    """Zeigt Trends formatiert an."""
    print(f"\n{'='*60}")
    print(f"  TRENDS: {niche.upper()} auf {platform}")
    print(f"{'='*60}")

    # Hashtags
    hashtags = [t for t in trends if t.get("type") == "hashtag"]
    if hashtags:
        print(f"\n  HASHTAGS:")
        for t in hashtags[:10]:
            print(f"    {t['hashtag']}")

    # Formate
    formats = [t for t in trends if t.get("type") == "format"]
    if formats:
        print(f"\n  VIRALE FORMATE:")
        for t in formats[:5]:
            print(f"    - {t['topic']}")

    # Topics
    topics = [t for t in trends if t.get("type") == "topic"]
    if topics:
        print(f"\n  TRENDING TOPICS:")
        for t in topics[:5]:
            print(f"    - {t['topic']}")

    # API-Trends
    api_trends = [t for t in trends if t.get("source") == "google_trends"]
    if api_trends:
        print(f"\n  GOOGLE TRENDS:")
        for t in api_trends[:5]:
            print(f"    - {t['topic']} ({t.get('volume', 'N/A')})")

    print(f"\n  Gesamt: {len(trends)} Trends gefunden")


def main():
    parser = argparse.ArgumentParser(description="CreatorFuel Trend Injector")
    parser.add_argument("--niche", "-n", required=True,
                        help="Nische (fitness/business/tech/lifestyle)")
    parser.add_argument("--platform", "-p", default="TikTok",
                        choices=["TikTok", "Instagram", "YouTube Shorts", "YouTube"],
                        help="Plattform")
    parser.add_argument("--save", "-s", action="store_true",
                        help="Trends als JSON speichern")
    parser.add_argument("--output", "-o", help="Ausgabeverzeichnis")
    parser.add_argument("--format", "-f", action="store_true",
                        help="Als Prompt-formatierten Text ausgeben")

    args = parser.parse_args()

    # Trends holen
    trends = get_platform_trends(args.platform, args.niche)

    # Anzeigen
    if args.format:
        formatted = format_trends_for_prompt(trends)
        print(formatted)
    else:
        print_trends(trends, args.niche, args.platform)

    # Speichern
    if args.save:
        filepath = save_trends(trends, args.niche, args.output)
        print(f"\nTrends gespeichert: {filepath}")

    return trends


if __name__ == "__main__":
    main()
