# OPEN TASKS — Noch offene Arbeiten

> Priorisierte Aufgabenliste für den Projektabschluss und Launch.

---

## DRINGEND (Blockieren den Launch — müssen VOR Go-Live erledigt werden)

### T1. Stripe Account erstellen & Payment Links einrichten
- **Beschreibung:** Stripe-Business-Account anlegen. 3 Payment Links für Starter (€99), Pro (€249), Agency (€499) erstellen. Links in Landing Page einbauen.
- **Abhängigkeiten:** Keine
- **Geschätzter Aufwand:** 2-3 Stunden
- **Referenz:** plan_freeze.md ("Stripe Payment Links für alle Preise"), alpha_labs_handbuch.md ("Stripe Account" in Launch Week)

### T2. OpenAI API-Key einrichten & Demo-Post generieren
- **Beschreibung:** API-Key in .env-Datei hinterlegen. Alle 6 Python-Module testen (style_analyzer → post_generator → trend_injector → batch_producer → cost_calculator → demo). Ersten echten Demo-Post generieren.
- **Abhängigkeiten:** T1 (optional, kann parallel)
- **Geschätzter Aufwand:** 1-2 Stunden
- **Referenz:** README.md ("Schnellstart" Sektion)

### T3. Landing Page deployen
- **Beschreibung:** index.html auf GitHub Pages oder Hostinger hochladen. Domain verbinden (oder GitHub-Subdomain nutzen). SSL prüfen.
- **Abhängigkeiten:** T1 (Stripe-Links müssen eingebaut sein)
- **Geschätzter Aufwand:** 1-2 Stunden
- **Referenz:** index.html, plan_freeze.md ("Hosting: Hostinger")
- **Hinweis:** Plan Freeze sagt Hostinger, aber GitHub Pages wäre kostenlos. Entscheidung nötig.

### T4. Newsletter-Plattform entscheiden & einrichten
- **Beschreibung:** Entscheidung zwischen Beehiiv, Substack oder ChatGPT-E-Mail. Account erstellen. Erste 3 Newsletter-Themen aus Research-Report ableiten. Landing-Page-Formular mit Plattform verbinden.
- **Abhängigkeiten:** T3 (Website muss live sein)
- **Geschätzter Aufwand:** 2-3 Stunden (inkl. Entscheidung)
- **Referenz:** 7day_launch.md ("Beehiiv Account"), plan_freeze.md ("ChatGPT"), alpha_labs_handbuch.md ("Substack" als Newsletter-Plattform)

---

## WICHTIG (Erhöhen Erfolgswahrscheinlichkeit — sollten in Woche 1 erledigt werden)

### T5. Erste 20 Creator identifizieren & anschreiben
- **Beschreibung:** 20 TikTok/Instagram-Creator (50K-500K Follower) in der Zielgruppe finden. Persönliche DMs verfassen (nicht copy-paste). 10/Tag schicken.
- **Abhängigkeiten:** T3 (Website muss live sein)
- **Geschätzter Aufwand:** 3-4 Stunden (Research + Outreach)
- **Referenz:** 7day_launch.md (Day 3-5: Outreach), alpha_labs_handbuch.md (Customer Acquisition: 20 DMs/Tag)

### T6. Kunden-Onboarding-Prozess definieren
- **Beschreibung:** Google Formular erstellen für Kunden-Infos (Handle, Plattformen, Stil-Präferenzen, Content-Kategorien). Onboarding-E-Mail-Template schreiben. Ablauf dokumentieren.
- **Abhängigkeiten:** T2 (KI-System muss funktionieren)
- **Geschätzter Aufwand:** 2-3 Stunden
- **Referenz:** alpha_labs_handbuch.md (Customer Onboarding)

### T7. Analytics einrichten
- **Beschreibung:** Google Analytics 4 oder Plausible auf Website installieren. Stripe-Dashboard für Conversions. UTM-Parameter für verschiedene Kanäle.
- **Abhängigkeiten:** T3 (Website muss live sein)
- **Geschätzter Aufwand:** 1 Stunde
- **Referenz:** 7day_launch.md ("Analytics Dashboard" in Day 1)

### T8. Erste 3 Alpha Signal Newsletter-Editionen schreiben
- **Beschreibung:** Aus dem Research-Report (goldgraeber_report_2026.md) 3 Newsletter-Ausgaben ableiten. Jede: 3 Chancen, datengestützt, 500-800 Wörter.
- **Abhängigkeiten:** T4 (Plattform muss stehen)
- **Geschätzter Aufwand:** 4-6 Stunden (2-3h pro Ausgabe)
- **Referenz:** alpha_labs_handbuch.md (Content Production: Alpha Signal Newsletter)

---

## NICE-TO-HAVE (Verbessern das Produkt — können nach Launch folgen)

### T9. Style-Analyzer mit echter URL-Anbindung
- **Beschreibung:** Statt simulierter Analyse: Instagram/TikTok-Scraper oder API-Integration für echte Content-Analyse. Alternativ: Manuellen Input ermöglichen (Screenshot-Upload, Text-Eingabe).
- **Abhängigkeiten:** T2
- **Geschätzter Aufwand:** 4-8 Stunden
- **Referenz:** README.md ("Gib eine URL ein, sie ist aber NICHT wirklich verbunden")

### T10. Trend-Injektor mit echten Daten
- **Beschreibung:** Google Trends API, Twitter-Trending-API oder RSS-Feeds für tatsächliche Trends integrieren. Trends automatisch in Post-Generierung einfliessen lassen.
- **Abhängigkeiten:** T2
- **Geschätzter Aufwand:** 3-4 Stunden
- **Referenz:** README.md ("Trend-Detektor-Simulation")

### T11. Error-Handling & Logging im Python-Code
- **Beschreibung:** Try/except-Blöcke in allen API-Aufrufen. Retry-Logik mit Exponential Backoff. Logging in Datei oder Google Sheets. Kosten-Tracking pro Kunde.
- **Abhängigkeiten:** T2
- **Geschätzter Aufwand:** 3-4 Stunden

### T12. NischeStream erste Website bauen
- **Beschreibung:** Erste Nischen-Website (z.B. AI Tools für Creator) mit Hugo/WordPress. 10 SEO-Artikel schreiben. Affiliate-Links einbauen. Google Search Console anmelden.
- **Abhängigkeiten:** T3, T7
- **Geschätzter Aufwand:** 8-12 Stunden (pro Nische)
- **Referenz:** plan_freeze.md (NischeStream), alpha_labs_handbuch.md (SEO Keyword Check)

### T13. AgentSmith Templates vorbereiten
- **Beschreibung:** 3 KI-Agenten-Templates vorbereiten: Content Automation (€299), Research Analyst (€499), Support Assistant (€999). Nur wenn >20 CreatorFuel-Kunden.
- **Abhängigkeiten:** 20 CreatorFuel-Kunden
- **Geschätzter Aufwand:** 8-12 Stunden
- **Referenz:** plan_freeze.md ("Revenue-basierte Freigabe: 20 CreatorFuel Kunden")

### T14. Automatisierter Content-Delivery-Workflow
- **Beschreibung:** Automatisierte E-Mail-Versendung der generierten Posts an Kunden. Zapier/Make.com-Integration. Kalender-basierte Auslieferung.
- **Abhängigkeiten:** T6 (Onboarding steht), T2 (KI funktioniert)
- **Geschätzter Aufwand:** 4-6 Stunden
- **Referenz:** alpha_labs_handbuch.md (Weekly Review: Delivery Check)

### T15. Content-Multiplikator aktivieren
- **Beschreibung:** Erfolgreiche Posts in Newsletter-Ausgaben und NischeStream-Artikel umwandeln. Systematischer Content-Reuse.
- **Abhängigkeiten:** T8 (erste Newsletter stehen)
- **Geschätzter Aufwand:** 2-3 Stunden/Monat
- **Referenz:** alpha_labs_handbuch.md (Content Multiplication)

---

## Zeitplan-Vorschlag

| Woche | Fokus | Aufgaben |
|-------|-------|----------|
| **Woche 1** | Launch-Vorbereitung | T1, T2, T3, T4, T7 |
| **Woche 1-2** | Erste Kunden | T5, T6 |
| **Woche 2-3** | Content & Newsletter | T8 |
| **Woche 3-4** | Automatisierung | T9, T10, T11 |
| **Monat 2-3** | Skalierung | T12, T14 |
| **>20 Kunden** | Expansion | T13 |

---

*Dokument erstellt aus: plan_freeze.md, alpha_labs_handbuch.md, 7day_launch.md, README.md, index.html*
