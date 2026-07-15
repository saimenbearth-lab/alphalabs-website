# CreatorFuel - KI-Post-Generator fuer Content Creators

> **Erzeugt taeglich 3-5 Social-Media-Posts (TikTok, Instagram, YouTube Shorts) im individuellen Schreibstil des Creators - inkl. Style-Analyse, Trend-Injektion und Qualitaets-Checks.**

---

## Schnellstart (3 Befehle)

```bash
# 1. Abhaengigkeiten installieren
pip install -r requirements.txt

# 2. API-Key einrichten
cp .env.example .env
# -> OPENAI_API_KEY in .env eintragen (https://platform.openai.com/api-keys)

# 3. Ersten Post generieren
python demo.py                    # Offline-Demo (kein API-Key noetig)
# oder direkt mit API:
python batch_producer.py --creator "Alex" --niche fitness --platforms TikTok,Instagram --posts-per-platform 2
```

**Das ist alles.** Generierte Posts landen automatisch in `posts/YYYY-MM-DD/batches/` als `.txt` (kopierfertig) und `.json` (weiterverarbeitbar).

---

## Was brauchst du?

| Voraussetzung | Details |
|---------------|---------|
| **Python 3.10+** | Pruefen: `python --version` |
| **OpenAI Account** | Anmelden: https://platform.openai.com/signup |
| **€5 Guthaben** | Aufladen: https://platform.openai.com/settings/organization/billing/overview |

> **Tipp:** Mit €5 kannst du **500-1000 Posts** generieren. Mehr als genug zum Testen.

---

## Kosten pro Post

| Modell | Geschaetzt pro Post | Details |
|--------|-------------------|---------|
| **GPT-4o Mini** (empfohlen) | **$0.001 - $0.01** (~€0.001 - €0.01) | Schnell, guenstig, gut |
| **GPT-4o** (Premium) | **$0.01 - $0.05** (~€0.01 - €0.05) | Hoechste Qualitaet |

```bash
# Kosten fuer dein Szenario berechnen
python cost_calculator.py --scenario --creators 1 --posts-per-day 5
```

---

## Naechster Schritt nach der Installation

```bash
# Option A: Offline-Demo anschauen (kein API-Key noetig)
python demo.py

# Option B: Style-Profile aus deinen eigenen Posts erstellen
python style_analyzer.py --interactive

# Option C: Direkt mit Standard-Profile loslegen
python batch_producer.py \
  --creator "DeinName" \
  --niche fitness \
  --platforms TikTok,Instagram \
  --posts-per-platform 2
```

Alle generierten Posts werden mit **Quality Score (1-5)** bewertet und findest du unter:
```
posts/YYYY-MM-DD/batches/
  -> creator_batch.txt    (kopierfertig)
  -> creator_batch.json  (maschinenlesbar)
```

---

## Module im Ueberblick

```
creatorfuel/
  style_analyzer.py      # Analysiert deine Posts -> Style-Profile
  post_generator.py      # Generiert Posts mit OpenAI
  trend_injector.py      # Findet aktuelle Trends & Hashtags
  batch_producer.py      # Orchestriert alles: Tagesbatch mit einem Befehl
  cost_calculator.py     # Kostenkalkulation & Business-Szenarien
  demo.py                # Offline-Demo (kein API-Key noetig)
  SOP.md                 # Vollstaendiges Handbuch (Schritt-fuer-Schritt)
```

---

## Vollstaendige Dokumentation

Das gesamte Handbuch mit allen Details findest du in **[SOP.md](SOP.md)**:
- Erste Einrichtung (Schritt fuer Schritt)
- System ausfuehren
- Creator hinzufuegen
- Posts reviewen
- Prompts anpassen
- Troubleshooting
- Kostentransparenz

---

**Made with ❤️ for Creators who value authentic content.**
