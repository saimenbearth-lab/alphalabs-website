# CreatorFuel - Operations-Handbuch (SOP)

> **Version:** 1.0
> **Letzte Aktualisierung:** 2024
> **Voraussetzung:** Python 3.10+, OpenAI API Key

---

## Inhaltsverzeichnis

1. [Erste Einrichtung](#1-erste-einrichtung)
2. [System ausfuhren](#2-system-ausfuhren)
3. [Neuen Creator hinzufugen](#3-neuen-creator-hinzufugen)
4. [Posts reviewen](#4-posts-reviewen)
5. [Prompts anpassen](#5-prompts-anpassen)
6. [Troubleshooting](#6-troubleshooting)
7. [Kostentransparenz](#7-kostentransparenz)

---

## 1. Erste Einrichtung

### Schritt 1: Python installieren (falls nicht vorhanden)

```bash
# Prufe ob Python installiert ist
python --version
# oder
python3 --version

# Sollte 3.10 oder hoher anzeigen
```

Falls nicht installiert: https://www.python.org/downloads/

### Schritt 2: Repository klonen oder Dateien kopieren

```bash
# Alle Dateien sollten in diesem Verzeichnis sein:
# /mnt/agents/output/creatorfuel/
#   style_analyzer.py
#   post_generator.py
#   trend_injector.py
#   batch_producer.py
#   cost_calculator.py
#   prompts/
#   .env.example
```

### Schritt 3: Abhangigkeiten installieren

```bash
# Navigiere ins Projektverzeichnis
cd /mnt/agents/output/creatorfuel/

# Installiere benotigte Pakete
pip install openai python-dotenv requests emoji
```

### Schritt 4: API-Key einrichten

```bash
# Kopiere die Beispiel-.env Datei
cp .env.example .env

# Offne .env in einem Texteditor und trage deinen Key ein
# Unter Windows: notepad .env
# Unter Mac:     nano .env
```

In der `.env` Datei:
```
OPENAI_API_KEY=sk-dein-echter-api-key-hier-einfugen
OPENAI_MODEL=gpt-4o-mini
DEFAULT_LANGUAGE=both
```

**Wo bekomme ich den API-Key?**
1. Gehe zu https://platform.openai.com/api-keys
2. Melde dich an (oder erstelle Account)
3. Klicke "Create new secret key"
4. Kopiere den Key in die .env Datei

**Wichtig:** Der API-Key kostet Geld bei Nutzung. Neue Accounts erhalten oft ein Startguthaben.

### Schritt 5: Testlauf

```bash
# Teste die Installation
python cost_calculator.py
```

Wenn eine Kostenubersicht erscheint, ist alles bereit!

---

## 2. System ausfuhren

### Option A: Vollautomatischer Daily-Batch (Empfohlen)

Der einfachste Weg - alles auf einmal:

```bash
cd /mnt/agents/output/creatorfuel/

python batch_producer.py \
  --profile creator_profile.json \
  --niche fitness \
  --platforms TikTok,Instagram \
  --posts-per-platform 2 \
  --language both
```

**Parameter erklart:**
- `--profile`: Pfad zum Style-Profile des Creators
- `--niche`: Themen-Nische (z.B. fitness, business, tech)
- `--platforms`: Komma-getrennte Liste der Plattformen
- `--posts-per-platform`: Wie viele Posts pro Plattform (1-5)
- `--language`: Sprache (de / eng / both)

### Option B: Interaktiver Modus

Fuhre den interaktiven Assistenten aus:

```bash
cd /mnt/agents/output/creatorfuel/

python batch_producer.py \
  --interactive \
  --creator "Max Mustermann" \
  --niche fitness \
  --platforms TikTok,Instagram \
  --posts-per-platform 2
```

Das System fragt dich nach den Creator-Posts und erstellt automatisch ein Style-Profile.

### Option C: Schritt fur Schritt (Manuell)

Falls du jeden Schritt kontrollieren mochtest:

**Schritt 1: Style-Analyse**
```bash
python style_analyzer.py \
  --input creator_posts.txt \
  --creator "Max Mustermann"
```

**Schritt 2: Trends recherchieren**
```bash
python trend_injector.py \
  --niche fitness \
  --platform TikTok
```

**Schritt 3: Posts generieren**
```bash
python post_generator.py \
  --profile max_mustermann_profile.json \
  --topic "Proteinriegel selber machen" \
  --platform TikTok \
  --count 3 \
  --language de
```

### Ausgabe

Alle Dateien werden automatisch gespeichert unter:
```
/mnt/agents/output/creatorfuel/posts/YYYY-MM-DD/
  profiles/          -> Style-Profiles
  posts/             -> Einzelne Posts
  batches/           -> Komplette Tagesbatches
```

Jeder Batch enthalt:
- `.json` Datei (maschinenlesbar)
- `.txt` Datei (menschlich lesbar, zum Kopieren)

---

## 3. Neuen Creator hinzufugen

### Methode A: Mit existierenden Posts (Empfohlen)

**Schritt 1:** Erstelle eine Textdatei mit den letzten 20 Posts des Creators.
Trenne jeden Post mit `---`:

```
Post 1 Text hier...
---
Post 2 Text hier...
---
Post 3 Text hier...
```

Speichere als `creatorname_posts.txt`.

**Schritt 2:** Style-Analyse durchfuhren

```bash
python style_analyzer.py \
  --input creatorname_posts.txt \
  --creator "Vorname Nachname"
```

Das System erstellt automatisch ein `vorname_nachname_profile.json`.

**Schritt 3:** Mit dem neuen Profile Posts generieren

```bash
python batch_producer.py \
  --profile vorname_nachname_profile.json \
  --niche [NISCHE] \
  --platforms TikTok,Instagram,YouTube \
  --posts-per-platform 2
```

### Methode B: Interaktiv (ohne Datei)

```bash
python style_analyzer.py --interactive
```

Das System fragt nach:
1. Creator-Name
2. Posts (einfach in die Konsole kopieren)
3. Erstellt automatisch das Profile

### Methode C: Manuelles Profile (Experten)

Erstelle eine JSON-Datei manuell:

```json
{
  "creator_name": "Max Mustermann",
  "tone": "casual",
  "tone_description": "Lockerer, freundschaftlicher Ton",
  "sentence_length": "short",
  "emoji_usage": "moderate",
  "hook_style": "question",
  "cta_style": "soft",
  "vocabulary_level": "simple",
  "common_phrases": ["einfach machen", "pro Tipp", "das Beste"],
  "brand_voice_summary": "Authentisch und nahbar",
  "donts": ["Niemals verkauferisch klingen", "Keine langen Satze"]
}
```

Speichere als `max_mustermann_profile.json`.

---

## 4. Posts reviewen

### Nach der Generierung

Jeder generierte Post hat einen **Quality-Score (1-5)**:

| Score | Bedeutung | Aktion |
|-------|-----------|--------|
| 5/5 | Perfekt | Sofort verwenden |
| 4/5 | Gut | Kleine Anpassungen |
| 3/5 | OK | Uberarbeitung empfohlen |
| 2/5 | Schlecht | Neugenerierung oder manuelle Uberarbeitung |
| 1/5 | Unbrauchbar | Ignorieren |

### Quality-Gates (was wird gepruft)

1. **Hook vorhanden?** - Erster Satz packt in 3 Sekunden
2. **CTA vorhanden?** - Call-to-Action am Ende
3. **Keine AI-Tells?** - Keine offensichtlichen KI-Formulierungen
4. **Richtige Lange?** - Plattform-optimale Wortanzahl
5. **Hashtags vorhanden?** - Mindestens 3 relevante Hashtags

### Warnungen beachten

Im Output werden Warnungen angezeigt:
```
WARNUNGEN:
  ! AI-Tells gefunden: ['es ist wichtig']
  ! Wortanzahl (45) ausserhalb der Empfehlung (50-150)
```

**Haufige Probleme und Losungen:**

| Problem | Losung |
|---------|--------|
| AI-Tells gefunden | In der .txt Datei die markierten Phrasen ersetzen |
| Zu kurz/lang | Im Prompt "Schranker einhalten" hinzufugen |
| Keine Hashtags | Manuell 3-5 relevante Hashtags erganzen |
| Generischer Sound | Im Style-Profile mehr "donts" hinzufugen |

### Review-Workflow

1. Offne die `.txt` Datei im Batch-Ordner
2. Gehe jeden Post durch
3. Prufe den Quality-Score
4. Lies Warnungen
5. Kopiere gute Posts direkt
6. Uberarbeite Posts mit Score < 4
7. Speichere finale Version

---

## 5. Prompts anpassen

### Prompt-Dateien

Die Prompts liegen in `/mnt/agents/output/creatorfuel/prompts/`:

```
prompts/
  tiktok_prompt.txt       -> TikTok-Videos
  instagram_prompt.txt    -> Instagram Posts/Reels
  youtube_prompt.txt      -> YouTube Shorts
```

### Was kann ich anpassen?

**1. Ton/Stil andern**

Offne die gewunschte Prompt-Datei und finde den Abschnitt:
```
## STYLE-PROFILE DES CREATORS
{style_profile}
```

Daruber kannst du globale Anweisungen hinzufugen:
```
## ZUSATZLICHE ANWEISUNGEN
- Sei immer freundlich und ermutigend
- Verwende humorvolle Vergleiche
- Keine negativen Formulierungen
```

**2. Qualitatsanforderungen andern**

Im Bereich `## QUALITY GATES` kannst du Anforderungen anpassen:

```
## QUALITY GATES
1. Hook packt in 2 Sekunden? (vorher: 3)
2. Wortanzahl zwischen 30-100? (vorher: 50-150)
3. Mindestens 5 relevante Hashtags? (vorher: 3)
```

**3. Verbotene Elemente erganzen**

Im Bereich `## VERBOTENE ELEMENTE`:

```
## VERBOTENE ELEMENTE (AI-Tell Check)
- Keine generischen Phrasen wie "Hier sind..."
- Kein Wort "einfach" verwenden
- Keine Fragezeichen in der Uberschrift
- KEINE EMOJIS (wenn gewunscht)
```

**4. Output-Format anpassen**

Das JSON-Format kann angepasst werden:

```json
{{
  "posts": [
    {{
      "platform": "TikTok",
      "hook": "...",
      "script": "...",
      "caption": "...",
      "hashtags": ["..."],
      "cta": "...",
      "estimated_duration": "45s",
      "mood": "happy",           // NEUES FELD
      "music_suggestion": "..."  // NEUES FELD
    }}
  ]
}}
```

### Achtung beim Anpassen

- **JSON-Syntax beachten:** Anfuhrungszeichen, Kommas, Klammern
- **Platzhalter nicht loschen:** `{style_profile}`, `{trends}`, etc.
- **Backup erstellen:** Kopiere die Originaldatei vorher
- **Testen:** Nach jeder Anderung einen Testlauf machen

### Prompt-Testing

```bash
# Kurzer Test nach Prompt-Anderung
python post_generator.py \
  --profile test_profile.json \
  --topic "Test" \
  --platform TikTok \
  --count 1 \
  --language de
```

---

## 6. Troubleshooting

### Fehler: "No module named 'openai'"

**Ursache:** Python-Paket nicht installiert

**Losung:**
```bash
pip install openai python-dotenv requests emoji
```

Falls das nicht funktioniert:
```bash
pip3 install openai python-dotenv requests emoji
# oder
python -m pip install openai python-dotenv requests emoji
```

### Fehler: "OPENAI_API_KEY nicht gesetzt"

**Ursache:** API-Key fehlt oder .env Datei nicht gefunden

**Losung:**
1. Prufe ob `.env` Datei existiert:
   ```bash
   ls -la .env
   ```

2. Prufe ob der Key eingetragen ist:
   ```bash
   cat .env
   ```

3. Alternative: Key als Umgebungsvariable setzen:
   ```bash
   # Windows (Command Prompt)
   set OPENAI_API_KEY=sk-dein-key

   # Windows (PowerShell)
   $env:OPENAI_API_KEY="sk-dein-key"

   # Mac/Linux
   export OPENAI_API_KEY=sk-dein-key
   ```

### Fehler: "API-Fehler: Rate limit exceeded"

**Ursache:** Zu viele Anfragen in kurzer Zeit

**Losung:**
- Warte 60 Sekunden und versuche erneut
- Reduziere `--count` (weniger Posts pro Aufruf)
- Prufe dein OpenAI-Guthaben: https://platform.openai.com/usage

### Fehler: "JSON Decode Error"

**Ursache:** KI hat kein valides JSON zuruckgegeben

**Losung:**
- Versuche es erneut (nicht-deterministisch)
- Wechsle zu GPT-4o (zuverlassiger)
- Prufe ob das Prompt-Template korrekt ist

### Fehler: "Trend-Suche fehlgeschlagen"

**Ursache:** Internetverbindung oder Web-Suche nicht verfugbar

**Losung:**
- Prufe Internetverbindung
- Das System arbeitet auch ohne Trends (Fallback-Hashtags)
- Trends konnen manuell ubergeben werden

### Langsame Generierung

**Ursache:** GPT-4o ist langsamer als Mini

**Losung:**
- Wechsle zu `gpt-4o-mini` in der `.env` Datei
- Reduziere `--count`
- Weniger Plattformen auf einmal

### Hohe Kosten

**Losung:**
```bash
# Wechsle zu gpt-4o-mini (10x gunstiger)
# In .env Datei:
OPENAI_MODEL=gpt-4o-mini

# Kosten uberwachen
python cost_calculator.py --scenario
```

### Post-Qualitat ist schlecht

**Losungen:**
1. Besseres Style-Profile erstellen (mehr Posts analysieren)
2. Im Style-Profile mehr "donts" hinzufugen
3. Prompt-Template anpassen (siehe Kapitel 5)
4. Auf GPT-4o wechseln fur bessere Qualitat
5. Temperatur im Code anpassen (niedriger = konsistenter)

---

## 7. Kostentransparenz

### Preise pro Modell

| Modell | Input/1K Tokens | Output/1K Tokens | Status |
|--------|-----------------|------------------|--------|
| GPT-4o Mini | $0.00015 | $0.00060 | **Empfohlen** |
| GPT-4o | $0.00250 | $0.01000 | Premium |
| GPT-4 | $0.03000 | $0.06000 | Legacy |

### Geschatzte Kosten pro Post

**Mit GPT-4o Mini (Ziel: <$0.50/Post):**
```
Style-Analyse (einmalig):     ~$0.0005
Trend-Recherche:              ~$0.0005
Post-Generierung (pro Post):  ~$0.0003
------------------------------------------
Gesamt pro Post (bei 5 Posts): ~$0.0015
Gesamt pro Post (bei 1 Post):  ~$0.0040
```

**Mit GPT-4o (Ziel: <$2.00/Post):**
```
Style-Analyse (einmalig):     ~$0.008
Trend-Recherche:              ~$0.008
Post-Generierung (pro Post):  ~$0.012
------------------------------------------
Gesamt pro Post (bei 5 Posts): ~$0.016
Gesamt pro Post (bei 1 Post):  ~$0.028
```

> **Hinweis:** Die tatsachlichen Kosten sind oft noch niedriger als die Ziele!

### Monatliche Kosten berechnen

```bash
# Beispiel: 10 Creator, 5 Posts/Tag, 22 Arbeitstage
python cost_calculator.py \
  --scenario \
  --creators 10 \
  --posts-per-day 5 \
  --model gpt-4o-mini
```

### Kosten senken

| Methode | Einsparung |
|---------|-----------|
| gpt-4o-mini statt gpt-4o | ~90% |
| Mehr Posts pro API-Call | ~50% |
| Style-Profile wiederverwenden | ~20% |
| Trends cachen (nicht jedes Mal suchen) | ~10% |

### Kosten-Monitoring

Kosten werden in jeder Output-JSON gespeichert:
```json
{
  "generation_info": {
    "api_cost_usd": 0.0012,
    "total_tokens": 2450
  }
}
```

OpenAI-Dashboard fur detaillierte Ubersicht:
https://platform.openai.com/usage

---

## Schnell-Referenz: Haufige Befehle

```bash
# Einrichtung
pip install openai python-dotenv requests emoji
cp .env.example .env
# -> API-Key in .env eintragen

# Style-Analyse
python style_analyzer.py --interactive

# Full Daily Batch
python batch_producer.py \
  --profile creator.json \
  --niche fitness \
  --platforms TikTok,Instagram \
  --posts-per-platform 2

# Kosten checken
python cost_calculator.py
python cost_calculator.py --scenario --creators 10

# Trends anzeigen
python trend_injector.py --niche fitness --platform TikTok
```

---

**Fragen oder Probleme?**
- Prufe die Warnungen in der Output-Datei
- Starte mit `cost_calculator.py` um Kosten zu prufen
- Verwende `--interactive` fur gefuhrte Prozesse

*CreatorFuel - Von Creators, fur Creators.*
