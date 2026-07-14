# CLAIMS VS REALITY — Behauptungen und ihre Faktenlage

> Jede Behauptung im Projekt geprüft: Was ist belegt? Was ist nur eine Behauptung? Was ist widerlegt?

---

## Architektur-Behauptungen

| # | Behauptung | Quelle | Status | Realität |
|---|-----------|--------|--------|----------|
| 1 | "5 autonome Einnahme-Systeme" wurden definiert | endergebnis.md | ARCHIVIERT | Ursprünglich definiert, durch adversariale Prüfung auf 3 reduziert |
| 2 | "Post-Adversarial-Architektur: 3 aktive Maschinen" | plan_freeze.md | BELEGT | 3 Maschinen (CreatorFuel, Alpha Signal, NicheStream) + 1 bedingt (AgentSmith) |
| 3 | "M2 (AgentSmith) wird erst ab 20 Kunden aktiviert" | plan_freeze.md | NICHT GETESTET | Bedingung nie erreicht (0 Kunden). Theoretisch definiert, nie validiert |
| 4 | "M5 (EM Newsletter) wird in Alpha Signal integriert" | plan_freeze.md | NICHT BELEGT | Nur als Konzept beschrieben, nie umgesetzt |

---

## Finanz-Behauptungen

| # | Behauptung | Quelle | Status | Realität |
|---|-----------|--------|--------|----------|
| 5 | "€99/€249/€499 Preisstruktur" | plan_freeze.md, index.html | DEFINIERT | Preise sind überall konsistent dokumentiert. Aber: Nie getestet ob Zahlungsbereitschaft existiert |
| 6 | "Gesamtkosten €100-350/Monat" | plan_freeze.md | NICHT VERIFIZIERT | Kosten nur geschätzt. OpenAI API-Kosten hängen von Nutzung ab. Stripe-Kosten pro Transaktion. Keine tatsächlichen Kosten aufgelaufen |
| 7 | "Break-even in Woche 2-4" | plan_freeze.md | NICHT BELEGT | Theoretische Schätzung, nie getestet |
| 8 | "10 Kunden in Monat 1 = €1.000-2.500 MRR" | plan_freeze.md | NICHT BELEGT | Rechnung: 10 x €99-249 = €990-2.490. Mathematisch korrekt, aber keine Kunden akquiriert |
| 9 | "Monat 12: €12.500+ MRR" | plan_freeze.md | NICHT BELEGT | Projektion ohne empirische Basis. "Optimistisches Szenario" genannt |
| 10 | "Stripe nimmt 1.5% + €0.25 pro Transaktion" | plan_freeze.md | NICHT VERIFIZIERT | Stripe-Gebühren variieren nach Land und Kartenart. Sollte vor Rechnungsstellung geprüft werden |

---

## Tech-Behauptungen

| # | Behauptung | Quelle | Status | Realität |
|---|-----------|--------|--------|----------|
| 11 | "KI-System generiert 5 Posts pro Stunde" | README.md | NICHT GETESTET | Batch-Producer kann 5 Posts generieren, aber noch nie live ausgeführt. Dauer hängt von API-Latenz ab |
| 12 | "Cost Calculator zeigt exakte API-Kosten pro Kunde" | README.md | THEORETISCH | Formel ist implementiert, aber nie mit echten API-Aufrufen validiert |
| 13 | "Style-Analyzer analysiert Creator-Stil" | README.md | TEILWEISE FALSCH | README gibt zu: "Gib eine URL ein, sie ist aber NICHT wirklich verbunden". Funktioniert nur mit manuellem Input |
| 14 | "Trend-Injektor findet aktuelle Trends" | README.md | TEILWEISE FALSCH | README: "Trend-Detektor-Simulation". Keine echte Trend-Datenquelle angebunden |
| 15 | "€0.30 pro Post mit GPT-4o Mini" | README.md | NICHT VERIFIZIERT | GPT-4o Mini Preis: ~$0.60/1M Input-Tokens. Bei ~500 Tokens/Post = ~$0.0003. Mit Ausgabe-Tokens realistisch $0.001-0.01/Post. €0.30 scheint hoch gegriffen |
| 16 | "GPT-4o Mini gibt schnellere & bessere Ergebnisse" | README.md | NICHT VERIFIZIERT | GPT-4o Mini ist schneller als GPT-4o, aber Qualität ist niedriger. Behauptung "bessere Ergebnisse" ist widersprüchlich |
| 17 | "Single-Page-HTML reicht für alle Funktionen" | index.html | BELEGT (für Landing Page) | Website rendert korrekt, ist responsiv. Aber: Kein Kunden-Login, keine Self-Service-Funktionen |
| 18 | "Python-Skripte + Google Sheets = ausreichend" | plan_freeze.md, alpha_labs_handbuch.md | NICHT GETESTET | System existiert, aber nie produktiv eingesetzt. Skalierbarkeit über 50 Kunden fraglich |

---

## Business-Behauptungen

| # | Behauptung | Quelle | Status | Realität |
|---|-----------|--------|--------|----------|
| 19 | "Solo-Operator in 10-20 Stunden/Woche" | alpha_labs_handbuch.md | NICHT BELEGT | Arbeitszeit nie gemessen. Bei 0 Kunden sind 10-20h unrealistisch wenig (mehr Outreach nötig) |
| 20 | "KI macht 90% der Arbeit" | plan_freeze.md | NICHT BELEGT | KI generiert Text, aber Outreach, Quality-Check, Kunden-Support, Strategie = menschlich |
| 21 | "Creator brauchen täglich 3-5 Posts, kostet 2-4h/Tag" | plan_freeze.md | NICHT BELEGT | Plausible Annahme, aber keine Primärquelle zitiert. Keine Creator direkt befragt |
| 22 | "Creator zahlen €99-499 für KI-Posts" | plan_freeze.md | NICHT GETESTET | Preisannahme basiert auf Wettbewerbsanalyse (FeedHive €19/Monat, aiCarousels €17.50/Monat). Alpha Labs ist deutlich teurer |
| 23 | "20 DMs/Tag führen zu 2-5 Antworten und 0-1 Calls" | alpha_labs_handbuch.md | NICHT BELEGT | Typische DM-Konvertierung, aber nie getestet in diesem Kontext |
| 24 | "SEO braucht 6-12 Monate bis Traffic" | plan_freeze.md | PLAUSIBEL | Allgemein bekanntes SEO-Phänomen, nicht spezifisch getestet |
| 25 | "Erster Verkauf in 7 Tagen" | 7day_launch.md | NICHT ERREICHT | Launch wurde nie gestartet |
| 26 | "Newsletter-Plattform ist kostenlos (ChatGPT)" | plan_freeze.md | WIDERSPRÜCHLICH | Launch-Plan nennt Beehiiv, Handbuch nennt Substack. ChatGPT kann keine E-Mails versenden |

---

## Research-Behauptungen

| # | Behauptung | Quelle | Status | Realität |
|---|-----------|--------|--------|----------|
| 27 | "250+ Web-Searches durchgeführt" | goldgraeber_report_2026.md | NICHT BELEGT | Report existiert und ist detailliert, aber keine Aufzeichnung der einzelnen Searches |
| 28 | "10-Dimensionen-Analyse" | goldgraeber_report_2026.md | BELEGT (als Dokument) | Report hat 10 Dimensionen mit Quellen. Aber: Quellen nicht alle unabhängig verifiziert |
| 29 | "7 unentdeckte Tech-Chancen identifiziert" | goldgraeber_report_2026.md | BELEGT | 7 Unternehmen detailliert beschrieben (Mastra, Dabba, Chowdeck, BIGC, Limitless, Mirai, Normal Computing) |
| 30 | "Mastra: Kategorie-Definierendes Neuland" | goldgraeber_report_2026.md | BEWERTUNG | Subjektive Einschätzung. Tatsache: Mastra ist ein Open-Source AI-Agent-Framework |
| 31 | "Dabba: Vollständig automatisiertes Wachstum" | goldgraeber_report_2026.md | BEWERTUNG | Subjektive Einschätzung mit finanziellen Projektionen ohne primäre Quellen |
| 32 | "Cross-Verification durch ≥2 unabhängige Quellen" | endergebnis.md | NICHT BELEGT | Im Research-Report sind Quellen genannt, aber keine Metadaten über Cross-Verification vorhanden |

---

## Operations-Behauptungen

| # | Behauptung | Quelle | Status | Realität |
|---|-----------|--------|--------|----------|
| 33 | "Täglicher Workflow: 10 DMs + 1 Post + Quality Check" | alpha_labs_handbuch.md | NICHT GETESTET | Workflow ist dokumentiert, aber nie ausgeführt |
| 34 | "30 Min/Woche Quality Check" | alpha_labs_handbuch.md | NICHT GETESTET | Bei 0 Kunden nicht relevant. Bei 10+ Kunden vermutlich mehr als 30 Minuten |
| 35 | "VA für €500/Monat ab 20 Kunden" | plan_freeze.md | NICHT RELEVANT | Nie erreicht |
| 36 | "Google Sheets als CRM ausreichend" | alpha_labs_handbuch.md | NICHT GETESTET | Template wird erwähnt, aber nicht im Projekt vorhanden |
| 37 | "Content-Multiplikator wandelt Posts in Newsletter + SEO" | alpha_labs_handbuch.md | NICHT UMGESETZT | Konzept beschrieben, aber kein automatisierter Prozess implementiert |

---

## Website-Behauptungen

| # | Behauptung | Quelle | Status | Realität |
|---|-----------|--------|--------|----------|
| 38 | "Dark Theme mit Gold-Akzenten (#d4af37)" | index.html | BELEGT | Visuell korrekt implementiert |
| 39 | "Responsive Design für Mobile/Tablet/Desktop" | index.html | BELEGT | CSS-Breakpoints vorhanden (576px, 768px, 992px) |
| 40 | "Newsletter-Formular funktioniert" | index.html | NICHT FUNKTIONSFÄHIG | Formular hat kein Backend. Einträge gehen ins Leere |
| 41 | "Stripe Payment Links sind verfügbar" | index.html | NICHT FUNKTIONSFÄHIG | Platzhalter-Links oder gar keine Links. Stripe-Account nicht erstellt |
| 42 | "FAQ-Accordion interaktiv" | index.html | BELEGT | JavaScript funktioniert lokal |

---

## Zusammenfassung nach Kategorie

| Kategorie | Anzahl | Belegt | Unbelegt | Widerlegt |
|-----------|--------|--------|----------|-----------|
| Architektur | 4 | 1 | 2 | 1 (archiviert) |
| Finanzen | 6 | 1 (definiert) | 5 | 0 |
| Technik | 8 | 1 | 5 | 2 |
| Business | 8 | 1 (plausibel) | 6 | 1 |
| Research | 6 | 2 | 3 | 1 |
| Operations | 5 | 0 | 4 | 1 |
| Website | 5 | 3 | 2 | 0 |
| **GESAMT** | **42** | **9** | **27** | **6** |

**Legende:**
- **Belegt:** Faktisch nachweisbar aus Projektdateien
- **Unbelegt:** Behauptung ohne empirische Grundlage
- **Widerlegt:** Behauptung widerspricht anderen Quellen oder der Realität
- **Archiviert:** Frühere Behauptung, die durch neuere Entscheidungen überholt wurde

---

## Kritische Erkenntnis

**Von 42 geprüften Behauptungen sind nur 9 (21%) faktisch belegt. 27 (64%) sind unbelegt, 6 (14%) sind widerlegt oder archiviert.**

Das Projekt hat eine solide strategische Planungsphase durchlaufen, aber die Ausführungsphase (Stadium B) wurde nie begonnen. Fast alle Business-Behauptungen (Preise, Konvertierung, Arbeitszeit) wurden nie validiert.

Die größten Risiken liegen in:
1. **Preisgestaltung:** €99-€499 sind deutlich teurer als Wettbewerb (FeedHive €19, aiCarousels €17.50)
2. **Style-Analyzer:** Funktioniert nicht wie beschrieben (keine echte URL-Analyse)
3. **Trend-Injektor:** Arbeitet mit simulierten statt echten Daten
4. **Kostenkalkulation:** €0.30/Post scheint deutlich über Schätzung

---

*Dokument erstellt aus: plan_freeze.md, endergebnis.md, adversarial_pruefung.md, dreifach_pruefung.md, alpha_labs_handbuch.md, 7day_launch.md, index.html, README.md, goldgraeber_report_2026.md*
