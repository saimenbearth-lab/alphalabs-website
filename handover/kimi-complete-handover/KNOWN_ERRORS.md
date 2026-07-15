# KNOWN ERRORS & TECHNISCHE SCHULDEN

> Alles, was nicht funktioniert, unfertig ist oder bekannte Probleme hat.

---

## Kritische Fehler (blockieren Launch)

### 1. Kein Stripe-Account eingerichtet
- **Status:** UNBEKANNT — Keine Stripe-Anmeldedaten im Projekt vorhanden
- **Impact:** Kein Zahlungseingang möglich. Alle Preis-Modelle sind rein theoretisch.
- **Lösung:** Stripe-Account erstellen, 3 Payment Links für CreatorFuel-Tarife anlegen
- **Aufwand:** 2-3 Stunden

### 2. Kein API-Key in CreatorFuel
- **Status:** README.md sagt "API_KEY notwendig, aber nicht im Code" und "Nicht direkt im Code speichern"
- **Impact:** System kann nicht ohne gültigen OpenAI API-Key ausgeführt werden
- **Lösung:** .env-Datei erstellen mit OPENAI_API_KEY
- **Aufwand:** 5 Minuten

### 3. Keine Domain gekauft / Website nicht deployed
- **Status:** index.html existiert lokal, ist aber nirgendwo live
- **Impact:** Keine öffentliche Landing Page, keine Kundenakquise möglich
- **Lösung:** Domain kaufen + auf GitHub Pages/Hostinger deployen
- **Aufwand:** 1-2 Stunden

---

## Wichtige Fehler (behindernd, aber nicht blockierend)

### 4. Style-Analyzer ist simuliert
- **Status:** In README.md steht unter Style-Analyzer: "Gib eine URL ein, sie ist aber NICHT wirklich verbunden, sondern in der generate_styles_guide als Platzhalter vorgesehen"
- **Impact:** Style-Analyse funktioniert nicht wie beschrieben. Der Analyzer kann nicht tatsächlich von einer URL lesen.
- **Lösung:** Ersetzen durch echte Instagram/TikTok-Scraper-Integration oder manuellen Input
- **Aufwand:** 2-4 Stunden

### 5. Trend-Injektor ohne echte Trend-Daten
- **Status:** "Trend-Detektor-Simulation" — Keine Anbindung an Google Trends, Twitter API oder echte Trend-Quellen
- **Impact:** Trends werden simuliert/geraten, nicht echt ermittelt
- **Lösung:** Google Trends API oder RSS-Feeds für Trend-Begriffe integrieren
- **Aufwand:** 2-3 Stunden

### 6. Newsletter-Formular ohne Backend
- **Status:** Die Landing Page hat ein Newsletter-Formular, aber kein Backend das die Einträge speichert
- **Impact:** Newsletter-Anmeldungen gehen verloren
- **Lösung:** Beehiiv/Substack-Einbettung oder Formspree/Mailchimp-Integration
- **Aufwand:** 30 Minuten

### 7. Newsletter-Plattform-Widerspruch
- **Status:** Plan Freeze sagt "ChatGPT" für Newsletter, Launch-Plan sagt "Beehiiv", Operations-Handbuch sagt "Substack"
- **Impact:** Unklar, welche Plattform tatsächlich genutzt werden soll
- **Lösung:** Entscheidung treffen und konsistent umsetzen
- **Aufwand:** 1 Stunde Entscheidung + Einrichtung

### 8. Kein wirkliches Onboarding-Formular
- **Status:** "Landing Page mit Stripe Payment Links" wird beschrieben, aber kein Formular für Kunden-Informationen (Handle, Style-Präferenzen) existiert
- **Impact:** Nach Zahlung weiss der Operator nicht, welchen Stil der Kunde will
- **Lösung:** Google Formular oder Typeform erstellen
- **Aufwand:** 1-2 Stunden

---

## Technische Schulden

### 9. Python-Skripte sind lokal, nicht cloud-basiert
- **Status:** System läuft nur auf dem lokalen Rechner des Operators
- **Impact:** Operator muss am Computer sitzen um Posts zu generieren. Keine automatisierte Auslieferung an Kunden.
- **Langfristig:** Cloud-Deployment (z.B. Replit, Heroku, VPS) für automatisierte Generierung
- **Aufwand (cloud):** 4-8 Stunden

### 10. Keine Datenbank — Google Sheets als "DB"
- **Status:** Google Sheets wird als Kunden-Tracking und Content-Management-System genutzt
- **Impact:** Skaliert nicht über 50 Kunden hinaus. Keine automatisierten Abfragen möglich.
- **Langfristig:** Echte Datenbank (Supabase/Firebase) oder Airtable
- **Aufwand:** 4-8 Stunden Migration

### 11. Kein Error-Handling im Python-Code
- **Status:** Kein try/except in den Hauptfunktionen sichtbar. Keine Retry-Logik bei API-Fehlern.
- **Impact:** Skript crasht bei API-Timeout oder Rate-Limit. Keine graceful degradation.
- **Langfristig:** Robuste Fehlerbehandlung einbauen
- **Aufwand:** 2-3 Stunden

### 12. Kein Logging-System
- **Status:** Kein Logging von API-Aufrufen, Kosten, Fehlern
- **Impact:** Keine Nachverfolgung was generiert wurde, keine Kostenkontrolle
- **Langfristig:** Logging in Datei oder Google Sheets
- **Aufwand:** 1-2 Stunden

---

## Getestet vs. Nicht getestet

### Was getestet wurde
| Komponente | Test-Status | Details |
|------------|------------|---------|
| Landing Page HTML | Visuell getestet | Renders korrekt, responsive Design |
| Preise-Struktur | Konsistenz-Check | 3 Tarife mit Features in allen Dokumenten identisch |
| Operations-Workflow | Dokumentiert, nicht live getestet | Täglicher Ablauf beschrieben, aber nicht ausgeführt |

### Was NICHT getestet wurde
| Komponente | Grund |
|------------|-------|
| OpenAI API-Integration | Kein API-Key vorhanden im Projekt |
| Erste Post-Generierung | System nie ausgeführt |
| Stripe-Payment-Flow | Stripe-Account nicht erstellt |
| Website-Deployment | Nicht deployed |
| Newsletter-Verteilung | Keine Plattform eingerichtet |
| Creator-Outreach | Noch nicht gestartet |
| SEO-Nischen-Strategie | Keine Website gebaut |
| Kunden-Onboarding | Keine Kunden |

---

## Unstimmigkeiten zwischen Dokumenten

| Thema | Dokument A sagt | Dokument B sagt | Status |
|-------|-----------------|-----------------|--------|
| Newsletter-Plattform | ChatGPT (kostenlos) | Beehiiv (Launch-Plan) | Unaufgelöst |
| Website-Hosting | Hostinger (Plan Freeze) | GitHub Pages (implizit, index.html) | Unaufgelöst |
| Google Sheets | "CRM + CMS" (Handbuch) | Nicht erwähnt in anderen | UNKLAR ob erstellt |
| Preisgestaltung | €99/€249/€499 (Plan Freeze) | Gleich in allen | Konsistent ✓ |
| Launch-Reihenfolge | M1 zuerst, M2 nach 2 Wochen | Gleich im Launch-Plan | Konsistent ✓ |

---

*Dokument erstellt aus: README.md, index.html, plan_freeze.md, alpha_labs_handbuch.md, 7day_launch.md*
