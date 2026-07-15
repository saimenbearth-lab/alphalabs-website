# USER REQUIREMENTS — Was das Projekt leisten sollte

> Chronologische Aufzeichnung aller Ziele, Korrekturen und finalen Architekturentscheidungen.

---

## 1. Ursprüngliches Ziel (Stadium A, Anfang)

**Ziel:** Finde die größten unentdeckten Tech-Chancen für 2026 ("Goldgräber-Chancen") und baue daraus ein Portfolio von Einnahme-Maschinen.

**Konkret:**
- Systematische 10-Dimensionen-Recherche mit 250+ Web-Searches
- Identifikation von 7+ Investment-Chancen mit hohem Upside
- Erstellung eines professionellen Research-Reports (29 Seiten)
- Entwicklung von 5 unabhängigen "Geld-Maschinen" als Geschäftsmodelle

**Output:** Ein Venture-Builder-Portfolio, das von einer Person in 10-20 Stunden/Woche betrieben werden kann und €10.000-€50.000/Monat generiert.

---

## 2. Erste Korrektur: Von Research zu SaaS-Business

**Wann:** Während der 3-Perspektiven-Prüfung

**Erkenntnis:** Der Research-Report allein ist kein Geschäftsmodell. Die ursprüngliche M1 (AI Research Agency mit €499-€3.999 Reports) wurde als nicht lebensfähig bewertet:

> "Investoren, die €500-€4.000 für einen Report zahlen, haben bereits Bloomberg Terminal (€25.000/Jahr). [...] Ein Solo-Operator ohne Reputation kann keine 4000 EUR Reports verkaufen." — Dreifach-Prüfung

**Korrektur:** Statt Research-Reports zu verkaufen, wurde ein SaaS-Modell für Creator entwickelt (CreatorFuel). Der Research-Report wird als Content für den Newsletter (Alpha Signal) und als Lead-Magnet genutzt.

---

## 3. Zweite Korrektur: Adversariales Review → 3 Maschinen gestrichen

**Wann:** Adversariale Prüfung (nach der 3-Perspektiven-Prüfung)

**Ergebnis der adversarialen Prüfung:**

| Maschine | Urteil | Begründung |
|----------|--------|------------|
| M1 AI Research Agency | Radikal umstrukturieren | Keine Zahlungsbereitschaft bei €499-€3.999 |
| M2 Mastra Agent Factory | Sofort killen | €5K-€50K ohne Vertrieb/Case Studies = "Fantasie" |
| M3 Creator Content Engine | Nur mit Differentiator lebensfähig | AI-Content ist Commodity |
| M4 Nischen-Live-Commerce | Vielversprechend, aber zu langsam | SEO braucht 6-12 Monate |
| M5 EM Intelligence | Killen oder umfunktionieren | TAM zu klein, Preis absurd |

**Finale Architektur (Post-Adversarial, aus plan_freeze.md):**

| Neue Maschine | Entstanden aus | Rolle |
|---------------|----------------|-------|
| **CreatorFuel** | M3 Creator Engine + Teile von M1 | **PRIMARY LAUNCH** — Haupteinnahmequelle |
| **Alpha Signal** | M5 EM Newsletter + M1 Research | Content Engine + Lead Magnet |
| **NicheStream** | M4 Nischen-Commerce | SEO/Affiliate — passiv |
| **AgentSmith** | M2 Agent Factory (bedingt) | Upsell ab 20 CreatorFuel-Kunden |
| **M5 integriert** | EM-Themen als Special Editions | Teil von Alpha Signal |

---

## 4. Finale Architektur: 3 aktive Maschinen

### Maschine 1: CreatorFuel (Haupteinnahme, ~60% des Umsatzes)

**Zielgruppe:** TikTok/Instagram-Creator mit 50K-500K Followern, 20-35 Jahre, englisch- oder deutschsprachig

**Problem:** Creator brauchen täglich 3-5 Posts, das kostet 2-4 Stunden/Tag. Sie hassen es.

**Lösung:** KI-generiert 3-5 Posts/Tag im individuellen Style des Creators (Script + Caption + Hashtags + Hook). Der Creator kopiert, passt an, postet. 5 Minuten statt 2 Stunden.

**Preise:**
- Starter: €99/Monat (10 Posts/Monat, 1 Plattform)
- Pro: €249/Monat (30 Posts/Monat, 2 Plattformen)
- Agency: €499/Monat (60 Posts/Monat, alle Plattformen)

### Maschine 2: Alpha Signal (~25% des Umsatzes)

**Zielgruppe:** Tech-affine Investoren, Early-Adopter, Gründer

**Problem:** Zu viel Noise, zu wenig Signal. Jeden Tag 100 neue "Chancen", niemand filtert echt.

**Lösung:** Wöchentlicher Newsletter mit den 3 wichtigsten unentdeckten Tech-Chancen.

**Preise:**
- Free: €0 (wöchentlich)
- Pro: €49/Monat (täglich + monatlicher Deep-Dive)
- Premium: €149/Monat (Pro + Early Access + Discord)

### Maschine 3: NicheStream (~15%, passiv)

**Zielgruppe:** SEO-Traffic (organisch)

**Lösung:** 3-5 SEO-optimierte Nischen-Websites mit Affiliate-Links.

**Nischen:**
1. AI Tools für Creator (Affiliate für AI-Tools)
2. Emerging Tech Chancen (Affiliate für Broker)
3. K-Pop Merch/Tickets (Affiliate für Merch)

**Einkommen:** Affiliate-Provisionen (1-30%), Display Ads ab 10K Besucher/Monat

---

## 5. Nicht-funktionale Anforderungen

### Solo-Operator-Prinzip
- **Eine Person** betreibt alles
- **10-20 Stunden/Woche** maximaler Aufwand
- **Kein Coding** erforderlich für den Operator (nur Copy-Paste von Befehlen)
- **Keine Angestellten** in Phase 1 (erst ab 20 Kunden ein VA für €500/Monat)

### KI-macht-die-Arbeit-Prinzip
- 90%+ der Content-Produktion durch KI automatisiert
- Operator macht nur Quality-Check (30 Min/Woche) und Kunden-Support
- Research durch KI-Swarm (10 Agenten)
- Post-Generierung durch OpenAI API
- Style-Analyse durch KI

### Minimaler Tech-Aufwand
- Keine Full-Stack-App (nur Python-Skripte)
- Keine Datenbank (Google Sheets)
- Kein komplexes Hosting (GitHub Pages, kostenlos)
- Gesamtkosten: **€100-350/Monat** (OpenAI API + optionale Tools)

### Schneller Cashflow
- Erster Verkauf innerhalb von **7 Tagen** nach Launch
- Break-even in **Woche 2-4**
- Ziel: **10 Kunden in Monat 1** = €1.000-2.500 MRR

### Skalierbarkeit
- Phase 1 (1-10 Kunden): Manuell + KI
- Phase 2 (10-50 Kunden): Templates + Automatisierung
- Phase 3 (50+ Kunden): VA + KI komplett

---

## 6. Geplante Zielgruppen und Zielwerte

| Metrik | Ziel Monat 1 | Ziel Monat 3 | Ziel Monat 12 |
|--------|-------------|-------------|---------------|
| CreatorFuel Kunden | 5-10 | 15-25 | 50+ |
| Alpha Signal Abonnenten | 100-200 | 500+ | 2.000+ |
| Alpha Signal Pro-Kunden | 2-5 | 10-20 | 50+ |
| NicheStream Traffic/Monat | 0 | 1.000-5.000 | 10.000+ |
| MRR (CreatorFuel) | €500-1.000 | €2.500-5.000 | €10.000+ |
| MRR (Alpha Signal Pro) | €100-250 | €500-1.000 | €2.500+ |
| **Gesamt-MRR** | **€600-1.250** | **€3.000-6.000** | **€12.500+** |

---

## 7. Was sich geändert hat (und warum)

| Ursprünglich | Geändert zu | Grund |
|--------------|-------------|-------|
| 5 Maschinen (M1-M5) | 3 aktive + 1 bedingt | Adversariale Prüfung: 2 Maschinen unlebensfähig |
| €499-€3.999 Research-Reports | €99-€499 SaaS für Creator | Keine Zahlungsbereitschaft ohne Reputation |
| €5K-€50K Custom Agent-Dev | €299-€999 Templates | Solo-Operator kann keine Enterprise-Software liefern |
| €200/Monat EM-Newsletter | Kostenlos + €49/Monat | TAM zu klein, Preis unrealistisch |
| Full-Stack Webapp | Python-Skripte + Google Sheets | Minimaler Aufwand |
| 10 KI-Agenten Cross-Verify | 1 KI-System (OpenAI API) | Komplexitätstheater entfernt |

---

*Dokument erstellt aus: endergebnis.md, plan_freeze.md, dreifach_pruefung.md, adversarial_pruefung.md, alpha_labs_handbuch.md*
