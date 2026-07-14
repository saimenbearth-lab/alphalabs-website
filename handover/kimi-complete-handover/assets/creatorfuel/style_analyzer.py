#!/usr/bin/env python3
"""
CreatorFuel Style Analyzer
Analysiert Creator-Posts und erstellt ein detailliertes Style-Profile.
Kann lokal (Regex/Heuristik) und mit OpenAI (KI-Deep-Dive) arbeiten.

Usage:
    python style_analyzer.py --input creator_posts.txt --creator "Max Mustermann"
    python style_analyzer.py --interactive
    python style_analyzer.py --input posts.txt --creator "Lisa" --local-only
"""

import os
import sys
import json
import re
import argparse
from datetime import datetime
from typing import Dict, List, Optional
from collections import Counter

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_posts_from_file(filepath: str) -> str:
    """Laedt Posts aus einer Textdatei."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def split_posts(text: str) -> List[str]:
    """Teilt Post-Texte anhand von Trennzeichen (--- oder Leerzeile)."""
    posts = re.split(r'\n?---\n?', text)
    return [p.strip() for p in posts if p.strip()]


def analyze_local(posts_text: str) -> Dict:
    """
    Lokale Heuristik-Analyse der Posts.
    Schnell, kostenlos, kein API-Key noetig.
    """
    posts = split_posts(posts_text)
    if not posts:
        return {"error": "Keine Posts gefunden"}

    all_text = " ".join(posts)
    words = all_text.split()
    sentences = re.split(r'[.!?]+', all_text)
    sentences = [s.strip() for s in sentences if s.strip()]

    # Satzlaenge
    avg_sentence_length = len(words) / max(len(sentences), 1)

    if avg_sentence_length < 8:
        sentence_length = "short"
    elif avg_sentence_length < 15:
        sentence_length = "medium"
    else:
        sentence_length = "long"

    # Emojis
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE
    )
    emojis = emoji_pattern.findall(all_text)
    emoji_count = len(emojis)

    if emoji_count == 0:
        emoji_usage = "none"
    elif emoji_count < len(posts) * 2:
        emoji_usage = "light"
    elif emoji_count < len(posts) * 5:
        emoji_usage = "moderate"
    else:
        emoji_usage = "heavy"

    # Haeufige Woerter (ohne Stoppwoerter)
    stopwords = {
        "der", "die", "das", "ein", "eine", "und", "oder", "ist", "sind", "war",
        "mit", "fuer", "auf", "in", "zu", "von", "den", "dem", "nicht", "auch",
        "als", "wie", "ich", "du", "er", "sie", "es", "wir", "ihr", "sie", "the",
        "a", "an", "and", "or", "is", "are", "was", "with", "for", "on", "in",
        "to", "of", "not", "also", "as", "like", "i", "you", "he", "she", "it",
        "we", "they", "me", "my", "your"
    }

    word_counts = Counter(w.lower() for w in words if w.lower() not in stopwords and len(w) > 3)
    common_words = [w for w, c in word_counts.most_common(10)]

    # Rufe Woerter/Phrasen
    phrase_pattern = re.findall(r'\b[A-Z][a-z]+\s+[a-z]+\b', all_text)
    common_phrases = [p for p, c in Counter(phrase_pattern).most_common(5) if c > 1]

    # Hooks (erste Saetze)
    hooks = []
    for post in posts:
        first_sentence = re.split(r'[.!?\n]', post.strip())[0].strip()
        if first_sentence:
            hooks.append(first_sentence)

    # CTAs (letzte Zeilen mit Call-to-Action Signalwoertern)
    cta_signals = ["folge", "folgt", "abonniert", "like", "kommentiert", "teilt",
                   "speichern", "merken", "link", "bio", "kommentar", "frage",
                   "follow", "subscribe", "comment", "share", "save", "check",
                   "swipe", "tippe", "klick"]
    ctas = []
    for post in posts:
        lines = post.strip().split("\n")
        for line in lines[-3:]:  # Pruefe letzte 3 Zeilen
            line_lower = line.lower()
            if any(signal in line_lower for signal in cta_signals):
                ctas.append(line.strip())
                break

    return {
        "posts_analyzed": len(posts),
        "avg_sentence_length": round(avg_sentence_length, 1),
        "sentence_length": sentence_length,
        "emoji_usage": emoji_usage,
        "emoji_count": emoji_count,
        "common_words": common_words,
        "common_phrases": common_phrases,
        "hooks": hooks[:5],
        "ctas": ctas[:5],
        "raw_text_sample": all_text[:500]
    }


def analyze_with_ai(local_results: Dict, creator_name: str) -> Dict:
    """
    Tiefenanalyse mit OpenAI API.
    Erstellt ein detailliertes Style-Profile.
    """
    if not OPENAI_API_KEY or OPENAI_API_KEY == "sk-your-key-here"::
        print("=" * 60)
        print("  KEIN API-KEY - Lokale Analyse wird verwendet")
        print("=" * 60)
        return create_basic_profile(local_results, creator_name)

    client = OpenAI(api_key=OPENAI_API_KEY)

    # Prompt fuer die KI-Analyse
    prompt = f"""
Analysiere die folgenden Social-Media-Posts von "{creator_name}" und erstelle ein detailliertes Style-Profile.

LOKALE ANALYSE (Vorab):
- Posts analysiert: {local_results['posts_analyzed']}
- Durchschnittliche Satzlaenge: {local_results['avg_sentence_length']}
- Emoji-Nutzung: {local_results['emoji_usage']}
- Haeufige Woerter: {', '.join(local_results['common_words'][:5])}
- Haeufige Phrasen: {', '.join(local_results['common_phrases'][:3])}

BEISPIEL-HOOKS:
{chr(10).join('- ' + h for h in local_results['hooks'][:3])}

BEISPIEL-CTAs:
{chr(10).join('- ' + c for c in local_results['ctas'][:3])}

TEXT-SAMPLE:
{local_results['raw_text_sample'][:800]}

ERSTELLE EIN JSON Style-Profile mit folgenden Feldern:
{{
  "creator_name": "Name",
  "tone": "Hauptton (motivational/casual/professional/energetic/funny)",
  "tone_description": "Detaillierte Beschreibung des Tons in 2-3 Saetzen",
  "sentence_length": "short/medium/long",
  "sentence_style": "Beschreibung des Satz-Stils",
  "emoji_usage": "none/light/moderate/heavy",
  "emoji_description": "Welche Emojis, wie oft, in welchem Kontext",
  "hook_style": "Welche Hook-Art (question/challenge/fact/story)",
  "hook_examples": ["Beispiel 1", "Beispiel 2"],
  "cta_style": "Art des CTA (soft/direct/engagement/question)",
  "cta_examples": ["Beispiel 1", "Beispiel 2"],
  "common_phrases": ["Phrase 1", "Phrase 2"],
  "vocabulary_level": "simple/moderate/advanced",
  "vocabulary_description": "Beschreibung des Wortschatzes",
  "signature_elements": ["Element 1", "Element 2"],
  "writing_quirks": ["Eigenheit 1", "Eigenheit 2"],
  "audience_perception": "Wie wirkt der Creator auf das Publikum",
  "brand_voice_summary": "2-3 Saetze Zusammenfassung der Brand Voice",
  "donts": ["Was der Creator NIEMALS schreiben wuerde"]
}}
"""

    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Du bist ein Experte fuer Social-Media-Stilanalyse. Du erstellst praezise Style-Profile fuer Content Creators. Du antwortest IMMER im angeforderten JSON-Format."
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000,
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content
        profile = json.loads(content)

        # Fuege Metadaten hinzu
        profile["_analysis_metadata"] = {
            "posts_analyzed": local_results["posts_analyzed"],
            "analysis_date": datetime.now().isoformat(),
            "model_used": OPENAI_MODEL
        }

        return profile

    except Exception as e:
        print(f"KI-Analyse-Fehler: {e}")
        print("Verwende lokale Analyse als Fallback...")
        return create_basic_profile(local_results, creator_name)


def create_basic_profile(local_results: Dict, creator_name: str) -> Dict:
    """
    Erstellt ein einfaches Profile aus lokalen Ergebnissen (ohne KI).
    """
    return {
        "creator_name": creator_name,
        "tone": "casual",
        "tone_description": f"Basierend auf {local_results['posts_analyzed']} analysierten Posts. Casual-Ton mit {local_results['sentence_length']} Saetzen.",
        "sentence_length": local_results["sentence_length"],
        "emoji_usage": local_results["emoji_usage"],
        "hook_style": "mixed",
        "cta_style": "soft",
        "common_phrases": local_results["common_phrases"],
        "vocabulary_level": "moderate",
        "brand_voice_summary": f"Authentischer Stil von {creator_name}, basierend auf {local_results['posts_analyzed']} Posts.",
        "donts": ["Niemals generisch klingen", "Keine AI-typischen Phrasen"],
        "_analysis_metadata": {
            "posts_analyzed": local_results["posts_analyzed"],
            "analysis_date": datetime.now().isoformat(),
            "model_used": "local-only"
        }
    }


def save_profile(profile: Dict, output_dir: str = None) -> str:
    """
    Speichert das Style-Profile als JSON-Datei.

    Returns:
        Pfad zur gespeicherten Datei
    """
    if output_dir is None:
        output_dir = os.getenv("OUTPUT_DIR", "/mnt/agents/output/creatorfuel/posts")

    date_str = datetime.now().strftime("%Y-%m-%d")
    profile_dir = os.path.join(output_dir, date_str, "profiles")
    os.makedirs(profile_dir, exist_ok=True)

    creator_name = profile.get("creator_name", "unknown").lower().replace(" ", "_")
    filename = f"{creator_name}_profile.json"
    filepath = os.path.join(profile_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)

    print(f"Profile gespeichert: {filepath}")
    return filepath


def print_profile(profile: Dict):
    """Zeigt das Style-Profile formatiert an."""
    print(f"\n{'='*60}")
    print(f"  STYLE-PROFILE: {profile.get('creator_name', 'Unbekannt')}")
    print(f"{'='*60}")

    fields = [
        ("Ton", "tone"),
        ("Ton-Beschreibung", "tone_description"),
        ("Satzlaenge", "sentence_length"),
        ("Emoji-Nutzung", "emoji_usage"),
        ("Hook-Stil", "hook_style"),
        ("CTA-Stil", "cta_style"),
        ("Wortschatz", "vocabulary_level"),
        ("Brand Voice", "brand_voice_summary"),
    ]

    for label, key in fields:
        value = profile.get(key, "N/A")
        if isinstance(value, list):
            value = ", ".join(value[:5])
        print(f"  {label}: {value}")

    # Common Phrases
    phrases = profile.get("common_phrases", [])
    if phrases:
        print(f"\n  Haeufige Phrasen:")
        for p in phrases[:5]:
            print(f"    - {p}")

    # Don'ts
    donts = profile.get("donts", [])
    if donts:
        print(f"\n  DON'Ts:")
        for d in donts[:5]:
            print(f"    - {d}")

    # Metadaten
    meta = profile.get("_analysis_metadata", {})
    if meta:
        print(f"\n  Analysierte Posts: {meta.get('posts_analyzed', 'N/A')}")
        print(f"  Modell: {meta.get('model_used', 'N/A')}")


def interactive_mode():
    """Fuehrt den interaktiven Analyse-Modus aus."""
    print("=" * 60)
    print("  CREATORFUEL - Style Analyzer (Interaktiv)")
    print("=" * 60)

    # Creator Name
    print("\nName des Creators:")
    creator_name = input("> ").strip()
    if not creator_name:
        creator_name = "MeinCreator"

    # Posts eingeben
    print(f"\nFuge die letzten Posts von {creator_name} ein.")
    print("Trenne Posts mit '---' oder Leerzeilen.")
    print("Beende mit Ctrl+D (Mac) oder Ctrl+Z + Enter (Windows):\n")

    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except (EOFError, KeyboardInterrupt):
        pass

    posts_text = "\n".join(lines)

    if not posts_text.strip():
        print("Keine Posts eingegeben. Beende.")
        return

    print(f"\nAnalysiere {len(posts_text)} Zeichen...")

    # Lokale Analyse
    local_results = analyze_local(posts_text)
    print(f"Lokale Analyse: {local_results['posts_analyzed']} Posts erkannt")

    # KI-Analyse
    print("Starte KI-Tiefenanalyse...")
    profile = analyze_with_ai(local_results, creator_name)

    # Anzeigen
    print_profile(profile)

    # Speichern
    save_profile(profile)

    print(f"\n{'='*60}")
    print("  ANALYSE ABGESCHLOSSEN!")
    print(f"{'='*60}")
    print(f"\nNaechster Schritt:")
    print(f"  python batch_producer.py --profile [pfad] --niche [nische]")


def main():
    parser = argparse.ArgumentParser(description="CreatorFuel Style Analyzer")
    parser.add_argument("--input", "-i", help="Pfad zur Post-Textdatei")
    parser.add_argument("--creator", "-c", help="Creator Name")
    parser.add_argument("--interactive", action="store_true",
                        help="Interaktiver Modus")
    parser.add_argument("--local-only", action="store_true",
                        help="Nur lokale Analyse (kein API-Key noetig)")
    parser.add_argument("--output", "-o", help="Ausgabeverzeichnis")

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    # Datei-Modus
    if not args.input:
        print("FEHLER: --input [datei] oder --interactive erforderlich")
        sys.exit(1)

    if not os.path.exists(args.input):
        print(f"FEHLER: Datei nicht gefunden: {args.input}")
        sys.exit(1)

    creator_name = args.creator or "MeinCreator"
    posts_text = load_posts_from_file(args.input)

    print(f"Analysiere Posts von {creator_name}...")

    # Lokale Analyse
    local_results = analyze_local(posts_text)
    print(f"Lokale Analyse: {local_results['posts_analyzed']} Posts erkannt")

    # KI-Analyse oder lokales Profile
    if args.local_only:
        profile = create_basic_profile(local_results, creator_name)
    else:
        profile = analyze_with_ai(local_results, creator_name)

    # Anzeigen und speichern
    print_profile(profile)
    save_profile(profile, args.output)

    return profile


if __name__ == "__main__":
    main()
