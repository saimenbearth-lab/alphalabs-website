#!/usr/bin/env python3
"""
CreatorFuel Post Generator
Generiert Social-Media-Posts basierend auf Style-Profile, Thema und Plattform.

Usage:
    python post_generator.py --profile creator_profile.json --topic "Proteinriegel" --platform TikTok
    python post_generator.py --profile creator_profile.json --topic "Produktivitat" --platform Instagram --count 3
"""

import os
import sys
import json
import re
import argparse
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Prompt-Lade-Funktion
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_prompt_template(platform: str) -> str:
    """Ladt das Prompt-Template fur eine Plattform."""
    prompt_file = os.path.join(SCRIPT_DIR, "prompts", f"{platform.lower()}_prompt.txt")

    if os.path.exists(prompt_file):
        with open(prompt_file, "r", encoding="utf-8") as f:
            return f.read()

    # Fallback-Templates wenn Datei nicht existiert
    templates = {
        "tiktok": "Erstelle {num_posts} TikTok-Script(s) zum Thema '{topic}' im Style von {creator_name}. Trends: {trends}",
        "instagram": "Erstelle {num_posts} Instagram-Post(s) zum Thema '{topic}' im Style von {creator_name}. Trends: {trends}",
        "youtube shorts": "Erstelle {num_posts} YouTube-Shorts-Script(s) zum Thema '{topic}' im Style von {creator_name}. Trends: {trends}",
    }
    return templates.get(platform.lower(), templates["tiktok"])


def format_style_profile(profile: Dict) -> str:
    """Formatiert das Style-Profile fur den Prompt."""
    lines = []

    fields = [
        ("Tone/Stimmung", "tone"),
        ("Ton-Beschreibung", "tone_description"),
        ("Satzlange", "sentence_length"),
        ("Satz-Stil", "sentence_style"),
        ("Emoji-Nutzung", "emoji_usage"),
        ("Emoji-Beschreibung", "emoji_description"),
        ("Hook-Stil", "hook_style"),
        ("Hook-Beispiele", "hook_examples"),
        ("CTA-Stil", "cta_style"),
        ("CTA-Beispiele", "cta_examples"),
        ("Wortschatz-Level", "vocabulary_level"),
        ("Wortschatz-Beschreibung", "vocabulary_description"),
        ("Signatur-Elemente", "signature_elements"),
        ("Writing Quirks", "writing_quirks"),
        ("Brand Voice", "brand_voice_summary"),
        ("DON'Ts", "donts"),
    ]

    for label, key in fields:
        value = profile.get(key, "")
        if value:
            if isinstance(value, list):
                if value:  # Nur wenn Liste nicht leer
                    lines.append(f"{label}:")
                    for item in value:
                        lines.append(f"  - {item}")
            else:
                lines.append(f"{label}: {value}")

    return "\n".join(lines) if lines else "Kein detailliertes Style-Profile verfugbar."


def generate_posts(
    profile: Dict,
    topic: str,
    platform: str,
    num_posts: int = 3,
    language: str = "both",
    trends_text: str = ""
) -> Dict:
    """
    Generiert Posts mit OpenAI API.

    Args:
        profile: Style-Profile als Dictionary
        topic: Thema der Posts
        platform: Zielplattform (TikTok/Instagram/YouTube Shorts)
        num_posts: Anzahl der Posts (1-5)
        language: Sprache (de/eng/both)
        trends_text: Formatierte Trends als Text

    Returns:
        Dictionary mit generierten Posts und Metadaten
    """
    if not OPENAI_API_KEY or OPENAI_API_KEY == "sk-your-key-here":
        print("=" * 60)
        print("  KEIN API-KEY GEFUNDEN")
        print("=" * 60)
        print("\nUm Posts zu generieren, brauchst du einen OpenAI API-Key.")
        print("\nSchnellstart:")
        print("  1. cp .env.example .env")
        print("  2. OPENAI_API_KEY in .env eintragen")
        print("  3. python post_generator.py erneut ausfuhren")
        print("\nOder fuhre die Offline-Demo aus:")
        print("  python demo.py")
        print("=" * 60)
        return {
            "generation_info": {
                "error": "API-Key fehlt. Bitte .env Datei konfigurieren.",
                "topic": topic,
                "platform": platform,
                "timestamp": datetime.now().isoformat(),
                "api_cost_usd": 0.0,
                "num_generated": 0
            },
            "posts": []
        }

    client = OpenAI(api_key=OPENAI_API_KEY)

    # Prompt-Template laden
    template = load_prompt_template(platform)

    # Style-Profile formatieren
    style_text = format_style_profile(profile)
    creator_name = profile.get("creator_name", "Creator")

    # Sprachanweisung
    lang_instruction = {
        "de": "Schreibe auf Deutsch.",
        "eng": "Schreibe auf Englisch.",
        "both": "Erstelle Posts auf Deutsch UND Englisch (je ein Post pro Sprache wenn moglich)."
    }.get(language, "Schreibe auf Deutsch.")

    # Prompt zusammenbauen
    prompt = template.format(
        style_profile=style_text,
        trends=trends_text or "Keine spezifischen Trends verfugbar.",
        num_posts=num_posts,
        topic=topic,
        language=lang_instruction,
        creator_name=creator_name
    )

    print(f"\nGeneriere {num_posts} Posts fur {platform}...")
    print(f"  Thema: {topic}")
    print(f"  Sprache: {language}")
    print(f"  Modell: {OPENAI_MODEL}")

    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Du bist ein Elite Social-Media-Copywriter. Du schreibst nur authentischen, viralen Content. Du achtest auf Plattform-Spezifika. Du schreibst nie generisch. Du antwortest immer im angeforderten JSON-Format."
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.85,
            max_tokens=4000,
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content

        # JSON parsen
        try:
            result = json.loads(content)
        except json.JSONDecodeError:
            # Versuche JSON aus Text zu extrahieren
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
            else:
                raise ValueError(f"Konnte kein JSON in der Antwort finden: {content[:200]}")

        # Quality Gates anwenden
        posts = result.get("posts", [])
        if not posts:
            print("WARNUNG: Keine Posts in der Antwort. Versuche Fallback...")
            posts = [result] if result else []

        validated_posts = []
        for post in posts:
            validated = apply_quality_gates(post, platform)
            validated_posts.append(validated)

        # Kosten berechnen
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        cost = _calculate_cost(prompt_tokens, completion_tokens)

        output = {
            "generation_info": {
                "creator": creator_name,
                "topic": topic,
                "platform": platform,
                "language": language,
                "num_requested": num_posts,
                "num_generated": len(validated_posts),
                "model": OPENAI_MODEL,
                "timestamp": datetime.now().isoformat(),
                "api_cost_usd": round(cost, 4),
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": prompt_tokens + completion_tokens
            },
            "posts": validated_posts
        }

        return output

    except Exception as e:
        print(f"FEHLER bei der Generierung: {e}")
        return {
            "generation_info": {
                "error": str(e),
                "topic": topic,
                "platform": platform,
                "timestamp": datetime.now().isoformat()
            },
            "posts": []
        }


def apply_quality_gates(post: Dict, platform: str) -> Dict:
    """
    Wendet Quality Gates auf einen generierten Post an.
    Fugt Scores und Warnungen hinzu.
    """
    quality = {
        "hook_check": False,
        "cta_check": False,
        "ai_tell_check": False,
        "length_check": False,
        "hashtag_check": False,
        "overall_score": 0,
        "warnings": []
    }

    # Hole den zu prufenden Text
    text_to_check = ""
    if "script" in post:
        text_to_check = post["script"]
    elif "content" in post:
        text_to_check = post["content"]
    elif "caption" in post:
        text_to_check = post["caption"]

    word_count = len(text_to_check.split())

    # 1. Hook Check
    hook = post.get("hook", "")
    if hook and len(hook) > 5:
        quality["hook_check"] = True
    else:
        quality["warnings"].append("Kein klarer Hook gefunden")

    # 2. CTA Check
    cta = post.get("cta", "")
    if cta and len(cta) > 3:
        quality["cta_check"] = True
    else:
        quality["warnings"].append("Kein Call-to-Action gefunden")

    # 3. AI-Tell Check
    ai_tells = [
        "es ist wichtig", "es ist entscheidend", "denke daran",
        "lass uns", "hier sind", "schlussfolgernd", "zusammenfassend",
        "in diesem artikel", "wie du sehen kannst", "es ist offensichtlich"
    ]
    text_lower = text_to_check.lower()
    found_ai_tells = [t for t in ai_tells if t in text_lower]
    quality["ai_tell_check"] = len(found_ai_tells) == 0
    if found_ai_tells:
        quality["warnings"].append(f"AI-Tells gefunden: {found_ai_tells}")

    # 4. Lange Check
    platform_limits = {
        "TikTok": (50, 150),
        "Instagram": (100, 300),
        "YouTube Shorts": (100, 200),
        "YouTube": (100, 200)
    }

    limits = platform_limits.get(platform, (50, 300))
    quality["length_check"] = limits[0] <= word_count <= limits[1]
    if not quality["length_check"]:
        quality["warnings"].append(
            f"Wortanzahl ({word_count}) ausserhalb der Empfehlung ({limits[0]}-{limits[1]})"
        )

    # 5. Hashtag Check
    hashtags = post.get("hashtags", [])
    if isinstance(hashtags, str):
        hashtags = hashtags.split()
    quality["hashtag_check"] = len(hashtags) >= 3
    if not quality["hashtag_check"]:
        quality["warnings"].append(f"Nur {len(hashtags)} Hashtags (mind. 3 empfohlen)")

    # Overall Score
    checks = [quality["hook_check"], quality["cta_check"],
              quality["ai_tell_check"], quality["length_check"], quality["hashtag_check"]]
    quality["overall_score"] = sum(1 for c in checks if c)

    # Fuge Quality-Gates zum Post hinzu
    post["_quality"] = quality

    return post


def _calculate_cost(prompt_tokens: int, completion_tokens: int) -> float:
    """Berechnet API-Kosten."""
    model = OPENAI_MODEL.lower()
    if "gpt-4o-mini" in model:
        return (prompt_tokens * 0.00000015) + (completion_tokens * 0.00000060)
    elif "gpt-4o" in model:
        return (prompt_tokens * 0.00000250) + (completion_tokens * 0.00001000)
    elif "gpt-4" in model:
        return (prompt_tokens * 0.00003000) + (completion_tokens * 0.00006000)
    return 0.0


def save_posts(output: Dict, creator_name: str, output_dir: str = None) -> str:
    """Speichert generierte Posts als JSON."""
    if output_dir is None:
        output_dir = os.getenv("OUTPUT_DIR", "/mnt/agents/output/creatorfuel/posts")

    date_str = datetime.now().strftime("%Y-%m-%d")
    posts_dir = os.path.join(output_dir, date_str, "posts")
    os.makedirs(posts_dir, exist_ok=True)

    safe_name = creator_name.lower().replace(" ", "_")
    platform = output.get("generation_info", {}).get("platform", "unknown")
    topic = output.get("generation_info", {}).get("topic", "general").replace(" ", "_")

    filename = f"{safe_name}_{platform.lower()}_{topic}.json"
    filepath = os.path.join(posts_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    return filepath


def print_posts(output: Dict):
    """Zeigt generierte Posts formatiert an."""
    info = output.get("generation_info", {})
    posts = output.get("posts", [])

    print(f"\n{'='*60}")
    print(f"  GENERIERTE POSTS")
    print(f"{'='*60}")
    print(f"  Creator: {info.get('creator', 'N/A')}")
    print(f"  Thema:   {info.get('topic', 'N/A')}")
    print(f"  Plattform: {info.get('platform', 'N/A')}")
    print(f"  Posts:   {len(posts)} / {info.get('num_requested', 'N/A')}")
    print(f"  Kosten:  ${info.get('api_cost_usd', 0):.4f}")
    print(f"  Tokens:  {info.get('total_tokens', 'N/A')}")
    print(f"{'='*60}")

    for i, post in enumerate(posts, 1):
        quality = post.get("_quality", {})
        score = quality.get("overall_score", 0)

        print(f"\n--- POST {i} (Quality: {score}/5) ---")

        if "hook" in post:
            print(f"\nHOOK:")
            print(f"  {post['hook']}")

        if "title" in post:
            print(f"\nTITEL:")
            print(f"  {post['title']}")

        content_key = "script" if "script" in post else "content" if "content" in post else "caption"
        print(f"\n{content_key.upper()}:")
        content = post.get(content_key, "")
        # Zeige nur die ersten 300 Zeichen
        preview = content[:300] + "..." if len(content) > 300 else content
        for line in preview.split("\n"):
            print(f"  {line}")

        if "hashtags" in post:
            hashtags = post["hashtags"]
            if isinstance(hashtags, list):
                print(f"\nHASHTAGS:")
                print(f"  {' '.join(hashtags)}")

        if "cta" in post:
            print(f"\nCTA:")
            print(f"  {post['cta']}")

        # Warnungen anzeigen
        warnings = quality.get("warnings", [])
        if warnings:
            print(f"\nWARNUNGEN:")
            for w in warnings:
                print(f"  ! {w}")

    print(f"\n{'='*60}")


def main():
    parser = argparse.ArgumentParser(description="CreatorFuel Post Generator")
    parser.add_argument("--profile", "-p", required=True, help="Pfad zum Style-Profile JSON")
    parser.add_argument("--topic", "-t", required=True, help="Thema der Posts")
    parser.add_argument("--platform", "-pl", required=True,
                        choices=["TikTok", "Instagram", "YouTube Shorts", "YouTube"],
                        help="Zielplattform")
    parser.add_argument("--count", "-c", type=int, default=3, help="Anzahl Posts (1-5)")
    parser.add_argument("--language", "-l", default="both",
                        choices=["de", "eng", "both"], help="Sprache")
    parser.add_argument("--trends", help="Pfad zur Trends-JSON Datei")
    parser.add_argument("--output", "-o", help="Ausgabeverzeichnis")

    args = parser.parse_args()

    # Style-Profile laden
    if not os.path.exists(args.profile):
        print(f"FEHLER: Style-Profile nicht gefunden: {args.profile}")
        sys.exit(1)

    with open(args.profile, "r", encoding="utf-8") as f:
        profile = json.load(f)

    # Trends laden (optional)
    trends_text = ""
    if args.trends and os.path.exists(args.trends):
        with open(args.trends, "r", encoding="utf-8") as f:
            trends_data = json.load(f)
            from trend_injector import format_trends_for_prompt
            trends_text = format_trends_for_prompt(trends_data)

    # Posts generieren
    output = generate_posts(
        profile=profile,
        topic=args.topic,
        platform=args.platform,
        num_posts=min(args.count, 5),
        language=args.language,
        trends_text=trends_text
    )

    # Ergebnis anzeigen
    print_posts(output)

    # Speichern
    creator_name = profile.get("creator_name", "unknown")
    filepath = save_posts(output, creator_name, args.output)
    print(f"\nGespeichert unter: {filepath}")

    return output


if __name__ == "__main__":
    main()
