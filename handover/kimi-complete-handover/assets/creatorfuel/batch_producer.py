#!/usr/bin/env python3
"""
CreatorFuel Batch Producer
Orchestriert Style-Analyse, Trend-Injektion und Post-Generierung.
Erzeugt den kompletten Tagessatz an Posts fur einen Creator.

Usage:
    # Vollautomatischer Modus (mit Style-Profile)
    python batch_producer.py --profile max_mustermann.json --niche fitness --platforms TikTok,Instagram --count 5

    # Mit interaktiver Style-Analyse
    python batch_producer.py --interactive --creator "Max Mustermann" --niche fitness --platforms TikTok,Instagram

    # Tagesbatch (alles auf einmal)
    python batch_producer.py --daily --creator "Lisa Creator" --niche business --platforms TikTok,Instagram,YouTube --posts-per-platform 2
"""

import os
import sys
import json
import argparse
from datetime import datetime
from typing import Dict, List, Optional

from dotenv import load_dotenv
load_dotenv()

# Importiere eigene Module
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from style_analyzer import analyze_local, analyze_with_ai, save_profile
from trend_injector import get_platform_trends, format_trends_for_prompt
from post_generator import generate_posts, save_posts, print_posts

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "/mnt/agents/output/creatorfuel/posts")


def load_or_create_profile(creator_name: str, posts_file: str = None, interactive: bool = False) -> Dict:
    """
    Ladt ein existierendes Profile oder erstellt ein neues.
    """
    # Prufe ob Profile existiert
    date_str = datetime.now().strftime("%Y-%m-%d")
    profile_dir = os.path.join(OUTPUT_DIR, date_str, "profiles")

    safe_name = creator_name.lower().replace(" ", "_")
    profile_path = os.path.join(profile_dir, f"{safe_name}_profile.json")

    if os.path.exists(profile_path):
        print(f"Existierendes Profile gefunden: {profile_path}")
        with open(profile_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # Prufe auch im aktuellen Verzeichnis
    local_path = os.path.join(os.getcwd(), f"{safe_name}_profile.json")
    if os.path.exists(local_path):
        print(f"Profile gefunden: {local_path}")
        with open(local_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # Neues Profile erstellen
    if posts_file and os.path.exists(posts_file):
        print(f"\nErstelle neues Style-Profile fur '{creator_name}'...")
        with open(posts_file, "r", encoding="utf-8") as f:
            posts_text = f.read()

        local_results = analyze_local(posts_text)
        profile = analyze_with_ai(local_results, creator_name)
        save_profile(profile)
        return profile

    if interactive:
        print(f"\nKein Profile gefunden fur '{creator_name}'.")
        print("Mochtest du Posts eingeben fur die Analyse? (j/n)")
        choice = input().strip().lower()

        if choice in ["j", "ja", "y", "yes"]:
            print("\nFuge die letzten Posts ein (trenne mit '---'):")
            print("(Beende mit Ctrl+D oder leerer Zeile)\n")

            lines = []
            try:
                while True:
                    line = input()
                    if line.strip() == "" and lines:
                        break
                    lines.append(line)
            except (EOFError, KeyboardInterrupt):
                pass

            posts_text = "\n".join(lines)
            if posts_text.strip():
                local_results = analyze_local(posts_text)
                profile = analyze_with_ai(local_results, creator_name)
                save_profile(profile)
                return profile

    # Minimal-Profile als Fallback
    print(f"\nVerwende Minimal-Profile fur '{creator_name}'.")
    print("Tipp: Erstelle ein detailliertes Profile mit:")
    print(f"  python style_analyzer.py --interactive")

    return {
        "creator_name": creator_name,
        "tone": "casual",
        "tone_description": "Standard-Casual-Ton",
        "sentence_length": "medium",
        "emoji_usage": "moderate",
        "hook_style": "question",
        "cta_style": "soft",
        "vocabulary_level": "moderate",
        "brand_voice_summary": f"Standard-Profile fur {creator_name}",
        "common_phrases": [],
        "donts": []
    }


def generate_daily_batch(
    creator_name: str,
    niche: str,
    platforms: List[str],
    profile: Dict,
    posts_per_platform: int = 2,
    language: str = "both",
    topics: List[str] = None
) -> Dict:
    """
    Generiert den kompletten Tagessatz an Posts.

    Returns:
        Dictionary mit allen generierten Posts pro Plattform
    """
    print(f"\n{'='*60}")
    print(f"  DAILY BATCH: {creator_name}")
    print(f"{'='*60}")
    print(f"  Nische: {niche}")
    print(f"  Plattformen: {', '.join(platforms)}")
    print(f"  Posts/Plattform: {posts_per_platform}")
    print(f"  Sprache: {language}")
    print(f"{'='*60}\n")

    all_results = {
        "batch_info": {
            "creator": creator_name,
            "niche": niche,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "platforms": platforms,
            "posts_per_platform": posts_per_platform,
            "language": language
        },
        "platforms": {},
        "total_cost_usd": 0.0,
        "total_posts": 0,
        "failed_generations": []
    }

    # Generiere Topics wenn nicht vorgegeben
    if not topics:
        topics = _generate_topic_ideas(niche, len(platforms) * posts_per_platform)

    topic_idx = 0

    for platform in platforms:
        print(f"\n{'='*40}")
        print(f"  PLATTFORM: {platform}")
        print(f"{'='*40}")

        # Trends fur diese Plattform holen
        print("  Suche Trends...")
        trends = get_platform_trends(platform, niche)
        trends_text = format_trends_for_prompt(trends)

        platform_posts = []

        for i in range(posts_per_platform):
            topic = topics[topic_idx % len(topics)]
            topic_idx += 1

            print(f"\n  Post {i+1}/{posts_per_platform}: '{topic}'")

            try:
                result = generate_posts(
                    profile=profile,
                    topic=topic,
                    platform=platform,
                    num_posts=1,
                    language=language,
                    trends_text=trends_text
                )

                info = result.get("generation_info", {})
                all_results["total_cost_usd"] += info.get("api_cost_usd", 0)
                all_results["total_posts"] += info.get("num_generated", 0)

                posts = result.get("posts", [])
                platform_posts.extend(posts)

                if posts:
                    print(f"    -> OK (Score: {posts[0].get('_quality', {}).get('overall_score', '?')}/5)")
                else:
                    print(f"    -> KEINE POSTS generiert")
                    all_results["failed_generations"].append({
                        "platform": platform,
                        "topic": topic,
                        "error": "Keine Posts generiert"
                    })

            except Exception as e:
                print(f"    -> FEHLER: {e}")
                all_results["failed_generations"].append({
                    "platform": platform,
                    "topic": topic,
                    "error": str(e)
                })

        all_results["platforms"][platform] = {
            "num_posts": len(platform_posts),
            "posts": platform_posts,
            "trends_used": [t.get("hashtag", t.get("topic", "")) for t in trends[:5]]
        }

    # Kosten-Info
    print(f"\n{'='*60}")
    print(f"  BATCH-ZUSAMMENFASSUNG")
    print(f"{'='*60}")
    print(f"  Gesamtkosten: ${all_results['total_cost_usd']:.4f}")
    print(f"  Posts: {all_results['total_posts']}")
    if all_results['total_posts'] > 0:
        print(f"  Kosten/Post: ${all_results['total_cost_usd']/all_results['total_posts']:.4f}")

    if all_results["failed_generations"]:
        print(f"\n  Fehler: {len(all_results['failed_generations'])} Generierungen fehlgeschlagen")

    # Hinweis wenn gar keine Posts generiert wurden (typisch: kein API-Key)
    if all_results['total_posts'] == 0:
        print(f"\n  HINWEIS: Keine Posts wurden generiert.")
        print(f"  Mogliche Ursachen:")
        print(f"    - Kein OPENAI_API_KEY in .env eingetragen")
        print(f"    - API-Key ist ungultig oder abgelaufen")
        print(f"    - Rate-Limit bei OpenAI erreicht")
        print(f"\n  Nachste Schritte:")
        print(f"    1. .env Datei prufen: cat .env")
        print(f"    2. API-Key eintragen: OPENAI_API_KEY=sk-dein-key")
        print(f"    3. Oder Demo ausfuhren: python demo.py (kein API-Key notig)")

    return all_results


def save_daily_batch(results: Dict, output_dir: str = None) -> str:
    """Speichert den kompletten Daily Batch."""
    if output_dir is None:
        output_dir = OUTPUT_DIR

    date_str = results["batch_info"]["date"]
    creator = results["batch_info"]["creator"].lower().replace(" ", "_")

    batch_dir = os.path.join(output_dir, date_str, "batches")
    os.makedirs(batch_dir, exist_ok=True)

    # JSON speichern
    json_path = os.path.join(batch_dir, f"{creator}_batch.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    # Formatierten Text speichern
    txt_path = os.path.join(batch_dir, f"{creator}_batch.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(format_batch_as_text(results))

    print(f"\nBatch gespeichert:")
    print(f"  JSON: {json_path}")
    print(f"  Text: {txt_path}")

    return batch_dir


def format_batch_as_text(results: Dict) -> str:
    """Formatiert den Batch als lesbaren Text."""
    info = results["batch_info"]
    lines = []

    lines.append("=" * 60)
    lines.append("  CREATORFUEL - TAGESBATCH")
    lines.append("=" * 60)
    lines.append(f"Creator:   {info['creator']}")
    lines.append(f"Nische:    {info['niche']}")
    lines.append(f"Datum:     {info['date']}")
    lines.append(f"Plattformen: {', '.join(info['platforms'])}")
    lines.append(f"Posts:     {results['total_posts']}")
    lines.append(f"Kosten:    ${results['total_cost_usd']:.4f}")
    lines.append("=" * 60)
    lines.append("")

    for platform, data in results["platforms"].items():
        lines.append(f"\n{'='*40}")
        lines.append(f"  {platform.upper()}")
        lines.append(f"{'='*40}")

        if data.get("trends_used"):
            lines.append(f"\nTrends: {', '.join(data['trends_used'])}")

        for i, post in enumerate(data.get("posts", []), 1):
            quality = post.get("_quality", {})
            score = quality.get("overall_score", "?")

            lines.append(f"\n--- POST {i} (Quality: {score}/5) ---")

            if "title" in post:
                lines.append(f"\nTITEL: {post['title']}")

            if "hook" in post:
                lines.append(f"HOOK: {post['hook']}")

            content_key = "script" if "script" in post else "content" if "content" in post else "caption"
            lines.append(f"\n{content_key.upper()}:")
            lines.append(post.get(content_key, ""))

            if "mid_video_hook" in post:
                lines.append(f"\nMID-HOOK: {post['mid_video_hook']}")

            hashtags = post.get("hashtags", [])
            if isinstance(hashtags, list):
                lines.append(f"\nHASHTAGS: {' '.join(hashtags)}")

            lines.append(f"\nCTA: {post.get('cta', '')}")

            if "estimated_duration" in post:
                lines.append(f"\nDauer: {post['estimated_duration']}")

            # Warnungen
            warnings = quality.get("warnings", [])
            if warnings:
                lines.append(f"\nWARNUNGEN:")
                for w in warnings:
                    lines.append(f"  ! {w}")

            lines.append("\n" + "-" * 40)

    lines.append(f"\n{'='*60}")
    lines.append("  ENDE DES BATCHES")
    lines.append(f"{'='*60}")

    return "\n".join(lines)


def _generate_topic_ideas(niche: str, count: int) -> List[str]:
    """Generiert Themen-Ideen fur die Nische."""
    topic_templates = [
        f"5 {niche} Fehler die Anfanger machen",
        f"So startest du mit {niche} richtig",
        f"Die Wahrheit uber {niche} die niemand sagt",
        f"{niche} Tutorial fur Fortgeschrittene",
        f"Mein {niche} Morgenroutine",
        f"{niche} Hacks die funktionieren",
        f"Was ich uber {niche} gelernt habe",
        f"{niche} Tools die du kennen musst",
        f"Vorher vs Nachher: {niche} Transformation",
        f"{niche} Mythos aufgedeckt",
        f"Warum deine {niche} Strategie scheitert",
        f"{niche} Geheimtipps von Profis",
        f"Tag im Leben: {niche} Edition",
        f"{niche} Q&A - Eure Fragen",
        f"{niche} Experiment - 30 Tage Challenge"
    ]

    # Wiederhole wenn notwendig
    topics = []
    while len(topics) < count:
        topics.extend(topic_templates)

    return topics[:count]


def main():
    parser = argparse.ArgumentParser(description="CreatorFuel Batch Producer")

    # Hauptmodi
    parser.add_argument("--profile", "-p", help="Pfad zum Style-Profile JSON")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Interaktiver Modus (Profile-Erstellung)")

    # Batch Parameter
    parser.add_argument("--creator", "-c", help="Creator Name")
    parser.add_argument("--niche", "-n", required=True, help="Nische (z.B. fitness, business)")
    parser.add_argument("--platforms", "-pl", required=True,
                        help="Plattformen, komma-getrennt (TikTok,Instagram,YouTube)")
    parser.add_argument("--posts-per-platform", "-ppp", type=int, default=2,
                        help="Posts pro Plattform (1-5)")
    parser.add_argument("--language", "-l", default="both",
                        choices=["de", "eng", "both"], help="Sprache")
    parser.add_argument("--posts-file", help="Datei mit Creator-Posts fur Analyse")

    # Daily-Modus
    parser.add_argument("--daily", "-d", action="store_true",
                        help="Daily-Batch-Modus (alles auf einmal)")

    # Output
    parser.add_argument("--output", "-o", help="Ausgabeverzeichnis")

    args = parser.parse_args()

    # Creator Name bestimmen
    creator_name = args.creator or "MeinCreator"

    # Profile laden/erstellen
    if args.profile:
        if not os.path.exists(args.profile):
            print(f"FEHLER: Profile nicht gefunden: {args.profile}")
            sys.exit(1)
        with open(args.profile, "r", encoding="utf-8") as f:
            profile = json.load(f)
        creator_name = profile.get("creator_name", creator_name)
    else:
        profile = load_or_create_profile(creator_name, args.posts_file, args.interactive)

    # Plattformen parsen
    platforms = [p.strip() for p in args.platforms.split(",")]

    # Validiere Plattformen
    valid_platforms = ["TikTok", "Instagram", "YouTube Shorts", "YouTube"]
    platforms = [p for p in platforms if p in valid_platforms]

    if not platforms:
        print(f"FEHLER: Keine gultigen Plattformen. Moglich: {', '.join(valid_platforms)}")
        sys.exit(1)

    # Batch generieren
    results = generate_daily_batch(
        creator_name=creator_name,
        niche=args.niche,
        platforms=platforms,
        profile=profile,
        posts_per_platform=min(args.posts_per_platform, 5),
        language=args.language
    )

    # Speichern
    save_daily_batch(results, args.output)

    # Zeige Zusammenfassung
    print(f"\n{'='*60}")
    print("  BATCH ERFOLGREICH GENERIERT!")
    print(f"{'='*60}")
    print(f"Creator:      {creator_name}")
    print(f"Nische:       {args.niche}")
    print(f"Plattformen:  {', '.join(platforms)}")
    print(f"Posts:        {results['total_posts']}")
    print(f"Gesamtkosten: ${results['total_cost_usd']:.4f} (~{results['total_cost_usd']*0.92:.2f} EUR)")
    print(f"{'='*60}")

    return results


if __name__ == "__main__":
    main()
