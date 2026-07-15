# DECISION LOG — Alle wichtigen Architekturentscheidungen

> Jede wichtige Entscheidung mit Datum, Alternativen und Begründung.

---

## Entscheidung 1: 5 Geld-Maschinen statt reines Research

| Feld | Inhalt |
|------|--------|
| **Datum** | Unklar (Phase 2, Anfang Juli 2026) |
| **Entscheidung** | Aus dem Research-Report werden 5 unabhängige Einnahme-Maschinen (M1-M5) mit je 16 verbindlichen Parametern abgeleitet |
| **Alternative** | Research-Report als PDF verkaufen oder als Newsletter-Inhalt nutzen |
| **Begründung** | "Statt 'ein Business zu starten', baust du ein Portfolio von 5 autonomen Einnahme-Systemen" — höhere Diversifikation, höhere Gesamt-Ertragschance |
| **Impact** | Maximaler Umfang: 5 parallele Geschäftsmodelle, extrem komplex für Solo-Operator |

---

## Entscheidung 2: 3-Perspektiven-Validierung

| Feld | Inhalt |
|------|--------|
| **Datum** | Unklar (Phase 2) |
| **Entscheidung** | Jede der 5 Maschinen wird durch drei unabhängige Subagenten geprüft: Käufer & Cashflow, Operator & Ausführung, System & Risiko |
| **Alternative** | Einzelne Experten-Reviews oder keine formale Prüfung |
| **Begründung** | "Keine Maschine startet, ohne dass ALLE 3 Fragen mit 'JA' beantwortet sind" — systematische Risikoreduzierung |
| **Impact** | Identifikation gravierender Schwächen in M1 und M2 vor Launch |

---

## Entscheidung 3: Adversariale Prüfung

| Feld | Inhalt |
|------|--------|
| **Datum** | Unklar (nach 3-Perspektiven-Prüfung) |
| **Entscheidung** | Separater Subagent im Teufelsadvokat-Modus greift jede Maschine systematisch an. Frage: "Warum stirbt diese Maschine?" |
| **Alternative** | Keine weitere Prüfung, direkt zu Bauen |
| **Begründung** | "Jede andere Prüfung ist ein Circle-Jerk." — Gruppen-Denken vermeiden durch explizit antagonistische Perspektive |
| **Impact** | 2 von 5 Maschinen als "nicht lebensfähig" identifiziert (M2, M5). Massive Reduktion des Portfolios. |

---

## Entscheidung 4: 5 Maschinen → 3 aktive + 1 bedingt

| Feld | Inhalt |
|------|--------|
| **Datum** | 14. Juli 2026 (Plan Freeze) |
| **Entscheidung** | Post-Adversarial-Architektur: M2 (Agent Factory) und M5 (EM Newsletter) werden gestrichen. M4 (Nischen-Commerce) wird bedingt aktiviert (ab 20 Kunden). |
| **Alternative** | Alle 5 Maschinen bauen, aber langsamer |
| **Begründung** | "Der Unterschied zwischen einem Solo-Operator, der €10K/Monat macht, und einem, der €50K versucht und bei €0 landet, ist exakt dieser Punkt." — Focus auf was funktioniert |
| **Impact** | Portfolio-Reduktion von 5 auf 3 aktive Maschinen. Erhebliche Reduktion der Komplexität. |

---

## Entscheidung 5: CreatorFuel als PRIMARY LAUNCH

| Feld | Inhalt |
|------|--------|
| **Datum** | 14. Juli 2026 (Plan Freeze) |
| **Entscheidung** | M3 (Creator Content Engine) wird zur primären Maschine "CreatorFuel" umgestaltet. Launch-Reihenfolge: M1 zuerst, M2 nach 2 Wochen, M3 nach 4 Wochen. |
| **Alternative** | Alpha Signal als PRIMARY LAUNCH (größere Zielgruppe) |
| **Begründung** | "Bevor man erklärt warum jede andere Maschine zurückgestuft wird." — M3 hat höchste Bewertung (6.3/10), schnellster Cashflow, klare Zielgruppe. Creator-Markt ist emotional und zahlungsbereit. |
| **Impact** | Ressourcen-Fokus auf die Maschine mit der höchsten Erfolgswahrscheinlichkeit |

---

## Entscheidung 6: Alpha Signal als Newsletter statt Research-Reports

| Feld | Inhalt |
|------|--------|
| **Datum** | 14. Juli 2026 (Plan Freeze) |
| **Entscheidung** | M1 (Research Agency mit €499-€3.999 Reports) wird komplett verworfen. Die Inhalte fliessen in M2 (Alpha Signal) als Free Newsletter + €49/Monat Pro ein. |
| **Alternative** | Research-Reports für niedrigeren Preis (€99-€499) anbieten |
| **Begründung** | "Investoren, die €500-€4.000 für einen Report zahlen, haben bereits Bloomberg Terminal (€25.000/Jahr)." — Keine Zahlungsbereitschaft ohne Reputation. Newsletter-Modell erlaubt Skalierung über Free-Content. |
| **Impact** | Research-Report wird zum Lead-Magnet statt Hauptprodukt. Niedrigerer ARPU aber höhere Skalierbarkeit. |

---

## Entscheidung 7: Stripe Payment Links statt Full-Integration

| Feld | Inhalt |
|------|--------|
| **Datum** | 14. Juli 2026 (Plan Freeze) |
| **Entscheidung** | Für alle Maschinen werden Stripe-Payment-Links verwendet statt einer eingebauten Zahlungsabwicklung |
| **Alternative** | Full-Stack-App mit eingebautem Checkout |
| **Begründung** | "Stripe Payment Links für alle Preise → Kunde zahlt → du schickst manuell (erste 10)" — Minimaler Tech-Aufwand, schnellste Time-to-First-Sale |
| **Impact** | Kein Backend-Code für Zahlungen nötig. Operator schickt Inhalte manuell in Phase 1. |

---

## Entscheidung 8: Hostinger statt Kimi Hosting

| Feld | Inhalt |
|------|--------|
| **Datum** | 14. Juli 2026 (Plan Freeze) |
| **Entscheidung** | Hosting über Hostinger (€3.99/Monat) statt Kimi (kostenlos) |
| **Alternative** | Kimi als kostenloses Hosting nutzen |
| **Begründung** | "Hostinger: €3.99/Monat, verfügt über kostenlose Domain, SSL-Zertifikat und unbegrenzte Bandbreite, schnelleres Laden als Kimi, auch SEO-freundlich" — Professioneller Eindruck, schnellere Ladezeiten |
| **Impact** | NICHT UMGESETZT. Tatsächlich wurde GitHub Pages als Hosting-Lösung in der Landing Page verwendet (siehe index.html). UNKLAR welches Hosting genutzt werden soll. |

---

## Entscheidung 9: Single-Page-HTML statt Full-Stack-App

| Feld | Inhalt |
|------|--------|
| **Datum** | Unklar (nach Plan Freeze) |
| **Entscheidung** | Landing Page als handgeschriebenes HTML/CSS (30KB) statt React/Vue/Next.js |
| **Alternative** | Full-Stack-Webapp mit Auth, Dashboard, Backend |
| **Begründung** | "Kein Coding erforderlich" — Solo-Operator kann nur Copy-Paste. Statisches HTML erfordert kein Hosting-Knowhow und keine Wartung. |
| **Impact** | Website ist fertig und funktioniert. Keine Backend-Abhängigkeiten. Aber: Keine dynamischen Inhalte, kein Kunden-Login, keine automatisierte Content-Auslieferung. |

---

## Entscheidung 10: Python-Skripte statt SaaS-Plattform

| Feld | Inhalt |
|------|--------|
| **Datum** | Unklar (nach Plan Freeze) |
| **Entscheidung** | CreatorFuel als Python-Skripte (OpenAI API) statt als Cloud-SaaS-Plattform |
| **Alternative** | SaaS-Plattform mit Web-Interface, Auth, Datenbank |
| **Begründung** | "€100-350/Monat Gesamtkosten [...] Python-Skripte + Google Sheets" — Minimaler Aufwand, keine DevOps, keine Wartung |
| **Impact** | System ist lokal lauffähig. Keine Cloud-Infrastruktur nötig. Aber: Kein Self-Service für Kunden, Operator muss Posts manuell generieren und verschicken. |

---

## Entscheidung 11: Newsletter via ChatGPT statt Newsletter-Plattform

| Feld | Inhalt |
|------|--------|
| **Datum** | 14. Juli 2026 (Plan Freeze) |
| **Entscheidung** | "Newsletter-Software → Begründung: KOSTENLOS → Wir nutzen ChatGPT, um die Inhalte zu erstellen" |
| **Alternative** | Beehiiv, Substack oder Mailchimp |
| **Begründung** | Kostenminimierung in der Startphase |
| **Impact** | UNKLAR — Im Launch-Plan wird Beehiiv als Newsletter-Plattform genannt. Widerspruch zur Plan-Freeze-Entscheidung. Nicht aufgelöst. |

---

## Entscheidung 12: 10 KI-Agenten → 1 OpenAI API

| Feld | Inhalt |
|------|--------|
| **Datum** | Unklar (zwischen adversarialer Prüfung und Asset-Produktion) |
| **Entscheidung** | CreatorFuel nutzt direkte OpenAI API (GPT-4o Mini/GPT-4o) statt 10 Cross-verifizierender Agenten |
| **Alternative** | Komplexes Multi-Agent-System mit 10 spezialisierten Agenten (wie im Research) |
| **Begründung** | Die adversariale Prüfung identifizierte den 10-Agenten-Ansatz als "Komplexitätstheater" — übermässig für die Content-Produktion |
| **Impact** | Einfacheres System, schnellere Ausführung, niedrigere Kosten. Aber: Weniger Fehlererkennung, kein Cross-Check. |

---

## Entscheidung 13: Wartebedingung für AgentSmith

| Feld | Inhalt |
|------|--------|
| **Datum** | 14. Juli 2026 (Plan Freeze) |
| **Entscheidung** | AgentSmith (KI-Agenten-Templates) wird erst aktiviert wenn >20 CreatorFuel-Kunden erreicht sind |
| **Alternative** | Sofort bauen und als Upsell anbieten |
| **Begründung** | "Revenue-basierte Freigabe: 20 CreatorFuel Kunden → AgentSmith wird aktiviert" — Erst Validierung des Kerngeschäfts, dann Erweiterung |
| **Impact** | Vermeidet Ressourcen-Verschwendung auf ein Produkt ohne bewiesene Nachfrage. AgentSmith ist nur als Konzept auf der Landing Page sichtbar ("Coming Soon"). |

---

## Zusammenfassung der Entscheidungsketten

```
Research (10 Agenten) → 5 Maschinen definiert
  → 3-Perspektiven-Prüfung → Schwächen identifiziert
    → Adversariale Prüfung → 2 Maschinen gestrichen, 1 bedingt
      → Plan Freeze (14. Juli) → 3 aktive Maschinen, Launch-Reihenfolge
        → Asset-Produktion → Landing Page, KI-System, Handbuch, Launch-Plan
          → [Stadium B NICHT GESTARTET]
```

---

*Dokument erstellt aus: plan_freeze.md, endergebnis.md, adversarial_pruefung.md, dreifach_pruefung.md, alpha_labs_handbuch.md, index.html, README.md*
