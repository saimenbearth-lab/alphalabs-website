#!/usr/bin/env python3
"""
CreatorFuel - OFFLINE DEMO
===========================
Funktioniert OHNE API-Key!
Zeigt, wie ein fertiger Post im CreatorFuel-System aussieht.

Usage:
    python demo.py
"""

import json
import os
import sys
from datetime import datetime


def print_header():
    print("=" * 70)
    print("  C R E A T O R F U E L   -   O F F L I N E   D E M O")
    print("=" * 70)
    print("\n  Diese Demo zeigt, wie ein fertiger Post aussieht.")
    print("  Kein API-Key notwendig!")
    print("=" * 70)


def get_example_profile():
    """Liefert ein Beispiel-Style-Profile fur einen Fitness-Creator."""
    return {
        "creator_name": "Alex FitCoach",
        "tone": "energetic",
        "tone_description": "Motivierend, direkt, enthusiastisch. Alex redet wie ein Trainingspartner, nicht wie ein Lehrer. Kurze, kraftvolle Satze mit Ausrufezeichen.",
        "sentence_length": "short",
        "sentence_style": "Fragmente und rhetorische Fragen. Wenig Subjunktionen. Direkte Ansprache ('du').",
        "emoji_usage": "moderate",
        "emoji_description": "Training-relevante Emojis (Fuer, Schwitzen, Hantel). Maximal 2-3 pro Post.",
        "hook_style": "challenge",
        "hook_examples": [
            "3 Uebungen die du falsch machst",
            "Tag 47 - und das passiert",
            "STOPP - mach das nicht mehr"
        ],
        "cta_style": "soft",
        "cta_examples": [
            "Speicher dir das fuer dein naechstes Training",
            "Tag jemanden der das braucht",
            "Wie machst du das? Kommentar!"
        ],
        "common_phrases": [
            "Let's go",
            "Keine Ausreden",
            "Progress, nicht Perfektion",
            "Form ueber Gewicht",
            "Consistency is key"
        ],
        "vocabulary_level": "simple",
        "vocabulary_description": "Einfache, direkte Worte. Kein Fachjargon ohne Erklaerung. Wie man einem Freund im Gym erklaert.",
        "signature_elements": [
            "Verwendet 'Team' um Community anzusprechen",
            "Endet oft mit 'Wir sehen uns im naechsten Post'",
            "Nutzt Before/After Vergleiche"
        ],
        "writing_quirks": [
            "Verdoppelt manche Worte fuer Betonung ('Mehr. Mehr Gewicht.')",
            "Nutzt Klammern fuer Seitenkommentare",
            "Schreibt Zahlen oft aus ('drei Sets statt 3 Sets')"
        ],
        "audience_perception": "Authentisch, erreichbar, motivierend. Kein 'ueberperfekter' Fitness-Influencer, sondern jemand der mit seinem Publikum waechst.",
        "brand_voice_summary": "Alex ist der Trainingspartner, den jeder gerne haette. Direkt, motivierend, ohne aufgesetzten Guru-Ton. Glaubt an Konsistenz statt Perfektion und macht Fitness fuer jeden zugaenglich - egal ob Anfaenger oder erfahren.",
        "donts": [
            "Niemals herablassend klingen",
            "Keine unerreichbaren Versprechen ('Sixpack in 2 Wochen')",
            "Keine Body-Shaming Formulierungen",
            "Kein verkauferischer Ton",
            "Nie ohne wissenschaftliche Basis sprechen"
        ]
    }


def get_example_posts():
    """Liefert 3 vollstaendige Beispiel-Posts."""
    return [
        {
            "_demo": True,
            "platform": "TikTok",
            "title": "3 Uebungen die fast alle falsch machen",
            "hook": "Machst du diese 3 Fehler im Training? (ich auch, bis vor 3 Monaten)",
            "script": """Hast du das Gefuehl, dass deine Brust einfach nicht waechst?

Koennte an diesen 3 Fehlern liegen:

[Uebung 1: Bankdruecken]
Die meisten lassen die Ellbogen zu weit aussen. 90 Grad Winkel - nein nein. 45 Grad zur Seite. Deine Schultern werden es dir danken. Mehr. Mehr Stabilitaet.

[Uebung 2: Fliegende]
Zu viel Gewicht. Die Arme sind nur leicht gebeugt, nicht durchgestreckt. Kontrolliert runter, fuehl den Stretch. Langsam. Kontrolliert.

[Uebung 3: Dips]
Oberkoerper zu aufrecht. Vorbeugen! Brust raus! So triffst du wirklich die Brust und nicht nur die Trizeps.

Probier es beim naechsten Training aus. Form vor Gewicht. Immer.""",
            "caption": "Welchen Fehler machst du? Kommentar! Team, Form ist alles. Nicht das Gewicht auf der Stange - die Qualitaet der Bewegung zaehlt.",
            "hashtags": ["#brusttraining", "#fitnesstips", "#formuebergewicht", "#gymtok", "#muskelaufbau", "#trainingfueranfaenger"],
            "cta": "Folge fuer mehr Trainings-Tipps! Speicher diesen Post fuer dein naechstes Chest-Day",
            "estimated_duration": "55s",
            "mid_video_hook": "Der zweite Fehler hat meinen Fortschritt 2 Jahre gebremst...",
            "_quality": {
                "hook_check": True,
                "cta_check": True,
                "ai_tell_check": True,
                "length_check": True,
                "hashtag_check": True,
                "overall_score": 5,
                "warnings": []
            }
        },
        {
            "_demo": True,
            "platform": "Instagram",
            "title": "Mein Meal Prep Sonntag",
            "hook": "5 Mahlzeiten. 45 Minuten. 12 Euro. So sieht mein Meal Prep aus.",
            "content": """Ich hasse kochen.

Aber ich hasse es noch mehr, jeden Tag ueber Essen nachzudenken.

Deswegen: Meal Prep Sonntag. Seit 2 Jahren. Jede Woche.

Mein Setup:
Huhn (3kg auf einmal in den Ofen), Reis (Topf voll), Gemuese (TK-Mix - keine Scham, pragmatic over perfect), und mein Geheimtipp: selbstgemachtes Hummus.

5 Container. Fertig.

Die Ausrede 'ich hatte keine Zeit' zaehlt nicht mehr. Die Zeit investierst du am Sonntag - und holst sie dir Montag bis Freitag zurueck.

Progress, nicht Perfektion.

(Auch wenn das Gemuese manchmal TK ist. Shhh.)

Speicher dir das fuer deinen naechsten Sonntag.""",
            "caption": "SonnTags sind Prep-Tags. Wer von euch meal-prept auch? Drop dein Lieblings-Rezept in die Kommentare! Team, Ernaehrung ist das, was im Fitness am meisten unterschaetzt wird. Trainieren ist 1 Stunde am Tag. Essen ist 24/7.",
            "hashtags": ["#mealprep", "#fitnessernaehrung", "#gesundessen", "#proteinreich", "#fitnesslifestyle", "#bulkseason", "#mealprepsonntag"],
            "cta": "Teile diesen Post mit jemandem der Meal Prep braucht!",
            "_quality": {
                "hook_check": True,
                "cta_check": True,
                "ai_tell_check": True,
                "length_check": True,
                "hashtag_check": True,
                "overall_score": 5,
                "warnings": []
            }
        },
        {
            "_demo": True,
            "platform": "YouTube Shorts",
            "title": "Warum deine Muskeln nicht wachsen",
            "hook": "Trainierst du 5x die Woche und siehst keinen Fortschritt? Hier ist der wahrscheinlichste Grund.",
            "script": """Du trainierst hart. Jedes Workout ein Killer.

Aber deine Muskeln wachsen nicht?

Ich hab 2 Jahre gebraucht um das zu kapieren:

Muskeln wachsen nicht im Gym. Sie wachsen in der Erholung.

Wenn du jeden Tag alles gibst, gibst du deinem Koerper nie die Chance aufzubauen. Training ist der Reiz - aber das Wachstum passiert beim Schlafen, beim Essen, beim Ausruhen.

Mein Tipp: Weniger haert trainieren. Mehr haert erholen.

7-8 Stunden Schlaf. Protein-Target treffen. Und ja - auch mal einen Rest Day einlegen ohne schlechtes Gewissen.

Consistency is key. Aber Recovery ist der Schluessel.

Wie viele Stunden schlaeft ihr durchschnittlich? Ehrliche Antworten nur!""",
            "caption": "Die Wahrheit die niemand dir sagt: Ruhe ist genauso wichtig wie das Training selbst. Speicher dir das fuer deinen naechsten Rest Day.",
            "hashtags": ["#muskelaufbau", "#recovery", "#fitnesstips", "#shorts", "#gymmotivation", "#bodybuilding"],
            "cta": "ABONNIEREN fuer mehr kurze, knackige Fitness-Truths!",
            "estimated_duration": "48s",
            "mid_video_hook": "Ich hab 2 Jahre gebraucht um das zu kapieren...",
            "_quality": {
                "hook_check": True,
                "cta_check": True,
                "ai_tell_check": True,
                "length_check": True,
                "hashtag_check": True,
                "overall_score": 5,
                "warnings": []
            }
        }
    ]


def format_post_as_text(post, index):
    """Formatiert einen Post als lesbaren Text."""
    lines = []
    quality = post.get("_quality", {})
    score = quality.get("overall_score", "?")

    lines.append(f"\n{'='*60}")
    lines.append(f"  POST {index}: {post.get('platform', 'Unknown').upper()}")
    lines.append(f"  Quality Score: {score}/5")
    lines.append(f"{'='*60}")

    if post.get("title"):
        lines.append(f"\nTITEL:")
        lines.append(f"  {post['title']}")

    if post.get("hook"):
        lines.append(f"\nHOOK:")
        lines.append(f"  {post['hook']}")

    # Content (script, content oder caption)
    content_key = "script" if "script" in post else "content" if "content" in post else "caption"
    lines.append(f"\n{content_key.upper()}:")
    content = post.get(content_key, "")
    for line in content.split("\n"):
        if line.strip():
            lines.append(f"  {line}")
        else:
            lines.append("")

    if post.get("mid_video_hook"):
        lines.append(f"\nMID-VIDEO-HOOK:")
        lines.append(f"  {post['mid_video_hook']}")

    if post.get("caption") and content_key != "caption":
        lines.append(f"\nCAPTION:")
        lines.append(f"  {post['caption']}")

    hashtags = post.get("hashtags", [])
    if hashtags:
        lines.append(f"\nHASHTAGS:")
        lines.append(f"  {' '.join(hashtags)}")

    if post.get("cta"):
        lines.append(f"\nCTA (Call-to-Action):")
        lines.append(f"  {post['cta']}")

    if post.get("estimated_duration"):
        lines.append(f"\nGESCHAETZTE DAUER: {post['estimated_duration']}")

    # Quality Gates
    lines.append(f"\n--- QUALITY GATES ---")
    checks = [
        ("Hook Check", quality.get("hook_check", False)),
        ("CTA Check", quality.get("cta_check", False)),
        ("AI-Tell Check", quality.get("ai_tell_check", False)),
        ("Laengen-Check", quality.get("length_check", False)),
        ("Hashtag Check", quality.get("hashtag_check", False)),
    ]
    for name, passed in checks:
        status = "✓" if passed else "✗"
        lines.append(f"  {status} {name}")

    warnings = quality.get("warnings", [])
    if warnings:
        lines.append(f"\nWARNUNGEN:")
        for w in warnings:
            lines.append(f"  ! {w}")

    return "\n".join(lines)


def print_next_steps():
    print("\n" + "=" * 70)
    print("  WIE KOMMST DU JETZT ZU ECHTEN POSTS?")
    print("=" * 70)
    print("""
  1. API-Key einrichten:
     cp .env.example .env
     # OPENAI_API_KEY in .env eintragen

  2. Style-Profile erstellen (deine eigenen Posts analysieren):
     python style_analyzer.py --interactive

  3. Oder direkt mit Beispiel-Profile starten:
     python batch_producer.py \\
       --profile example_output/example_profile.json \\
       --niche fitness \\
       --platforms TikTok,Instagram \\
       --posts-per-platform 2

  4. Kosten checken:
     python cost_calculator.py

  ALLE MODULE AUCH EINZELN NUTZBAR:
     python style_analyzer.py --interactive
     python trend_injector.py --niche fitness --platform TikTok
     python post_generator.py --profile profil.json --topic "Protein" --platform TikTok
""")


def main():
    print_header()

    # Zeige Style-Profile
    profile = get_example_profile()
    print(f"\n{'='*60}")
    print(f"  STYLE-PROFILE: {profile['creator_name']}")
    print(f"{'='*60}")
    print(f"\n  Tone:        {profile['tone']}")
    print(f"  Satzlange:   {profile['sentence_length']}")
    print(f"  Emojis:      {profile['emoji_usage']}")
    print(f"  Hook-Stil:   {profile['hook_style']}")
    print(f"  CTA-Stil:    {profile['cta_style']}")
    print(f"\n  Brand Voice:")
    print(f"  {profile['brand_voice_summary'][:100]}...")

    # Zeige die 3 Beispiel-Posts
    posts = get_example_posts()

    for i, post in enumerate(posts, 1):
        formatted = format_post_as_text(post, i)
        print(formatted)

    # Gesamtzusammenfassung
    print(f"\n{'='*60}")
    print(f"  ZUSAMMENFASSUNG")
    print(f"{'='*60}")
    print(f"  Posts gezeigt:     {len(posts)}")
    print(f"  Plattformen:       {', '.join(set(p['platform'] for p in posts))}")
    print(f"  Durchschn. Score:  {sum(p['_quality']['overall_score'] for p in posts) / len(posts)}/5")
    print(f"  Kosten fuer Demo:  $0.00 (kein API-Key verbraucht)")

    # Speichere Demo-Output als Datei
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo_output")
    os.makedirs(output_dir, exist_ok=True)

    demo_file = os.path.join(output_dir, "demo_posts.txt")
    with open(demo_file, "w", encoding="utf-8") as f:
        f.write("CREATORFUEL - DEMO OUTPUT\n")
        f.write(f"Erstellt: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n")
        f.write(f"\nCreator: Alex FitCoach (Beispiel)\n")
        f.write(f"Nische: fitness\n")
        f.write(f"Plattformen: TikTok, Instagram, YouTube Shorts\n\n")

        profile = get_example_profile()
        f.write("--- STYLE PROFILE ---\n")
        f.write(json.dumps(profile, ensure_ascii=False, indent=2))
        f.write("\n\n--- GENERIERTE POSTS ---\n")

        for i, post in enumerate(posts, 1):
            f.write(format_post_as_text(post, i))
            f.write("\n")

    print(f"\n  Demo-Output gespeichert unter:")
    print(f"  {demo_file}")

    print_next_steps()

    # Speichere auch als JSON
    json_file = os.path.join(output_dir, "demo_posts.json")
    demo_output = {
        "demo": True,
        "creator": "Alex FitCoach",
        "niche": "fitness",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "profile": profile,
        "posts": posts
    }
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(demo_output, f, ensure_ascii=False, indent=2)

    print(f"  JSON-Version: {json_file}")
    print("=" * 70)


if __name__ == "__main__":
    main()
