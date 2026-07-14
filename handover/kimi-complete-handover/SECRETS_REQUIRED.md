# SECRETS REQUIRED - Alpha Labs Projekt

**Dokument fuer:** Projekt-Betreiber / Solo-Operator  
**Zweck:** Uebersicht ALLER Secrets, API-Keys und Zugangsdaten die fuer den Betrieb benoetigt werden  
**Stand:** Juli 2026

---

## PFLICHT-SECRETS (Ohne diese funktioniert das System NICHT)

### 1. OPENAI_API_KEY

| Feld | Details |
|------|---------|
| **Was** | OpenAI API Key fuer KI-Content-Generierung |
| **Wofuer** | CreatorFuel Post-Generator, Style-Analyzer, Trend-Injection, Newsletter-Generierung |
| **Wo holen** | https://platform.openai.com/api-keys |
| **Kosten** | Pay-per-use, ca. $0.001-0.03 pro Post (je nach Modell) |
| **Format** | `sk-...` (beginnt mit `sk-`, ca. 50 Zeichen) |
| **Wo eintragen** | `creatorfuel/.env` (aus .env.example kopieren) |
| **Wichtig** | Key NIEMALS in Git committen! |

**Schritt-fuer-Schritt:**
1. Account erstellen auf https://platform.openai.com/
2. Zahlungsmethode hinzufuegen (Kreditkarte)
3. Auf "API Keys" -> "Create new secret key" klicken
4. Key kopieren (nur EINMAL sichtbar!)
5. In `creatorfuel/.env` einfuegen:
   ```
   OPENAI_API_KEY=sk-proj-XXXXXXXXXXXXXXXXXXXXXXXX
   ```

**Geschätzte monatliche Kosten:**
| Szenario | Kosten/Monat |
|----------|-------------|
| 1 Creator, gpt-4o-mini, ~50 Posts | $5-15 |
| 5 Creator, gpt-4o-mini, ~250 Posts | $25-50 |
| 10 Creator, gpt-4o, ~500 Posts | $200-400 |

---

## EMPFOHLENE SECRETS (Fuer erweiterte Funktionen)

### 2. STRIPE ACCOUNT (Zahlungsabwicklung)

| Feld | Details |
|------|---------|
| **Was** | Stripe-Account fuer Zahlungsabwicklung |
| **Wofuer** | CreatorFuel Produkte verkaufen, Alpha Signal Pro Abos, One-Time-Payments |
| **Wo holen** | https://dashboard.stripe.com/register |
| **Kosten** | Kostenlos einrichten, 1.5% + 0.25 EUR pro Transaktion |
| **Format** | Stripe Dashboard Login (Email + Passwort) |
| **Wo eintragen** | Keine API-Keys noetig - Payment Links im Dashboard erstellen |

**Benoetigte Payment Links (erstellen im Stripe Dashboard):**

| Produkt | Preis | Link einfuegen in |
|---------|-------|-------------------|
| CreatorFuel Starter | 99 EUR (One-time) | `alphalabs/index.html` Zeile ~1377 |
| CreatorFuel Pro | 249 EUR (One-time) | `alphalabs/index.html` Zeile ~1393 |
| CreatorFuel Agency | 499 EUR (One-time) | `alphalabs/index.html` Zeile ~1408 |
| Alpha Signal Pro | 49 EUR/Monat (Recurring) | Newsletter Landingpage |

**Anleitung siehe:** `launch/stripe_setup.md`

---

### 3. TWITTER/X API (Optional - fuer Alpha Signal Marketing)

| Feld | Details |
|------|---------|
| **Was** | Twitter API Access fuer automatisiertes Posting |
| **Wofuer** | Alpha Signal Threads posten, Outreach DMs, Lead-Generierung |
| **Wo holen** | https://developer.twitter.com/en/portal/dashboard |
| **Kosten** | Free Tier: 1,500 Tweets/Monat; Basic: $100/Monat |
| **Format** | `Bearer AAAAAAAAAA...` oder API Key + Secret |
| **Wo eintragen** | Noch nicht im Code implementiert - manuelles Posting empfohlen |

**Hinweis:** Das aktuelle System postet manuell (Copy & Paste). API-Integration ist fuer Phase 2 geplant.

---

### 4. EMAIL-POSTFACH (Kundenkommunikation)

| Feld | Details |
|------|---------|
| **Was** | Geschaeftliche E-Mail-Adresse |
| **Wofuer** | Kunden-Onboarding, Content-Versand, Support, Newsletter |
| **Wo holen** | Google Workspace, Zoho Mail, oder eigener Hosting-Provider |
| **Kosten** | Google Workspace: $6-12/Monat; Zoho: $1-4/Monat |
| **Format** | z.B. `hello@creatorfuel.de` |
| **Wo eintragen** | Email-Templates in `operations/alpha_labs_handbuch.md` |

---

## OPTIONALE SECRETS (Fuer erweiterte Features)

### 5. BEEHIIV / SUBSTACK API (Newsletter-Plattform)

| Feld | Details |
|------|---------|
| **Was** | Newsletter-Versand-Plattform |
| **Wofuer** | Alpha Signal Newsletter automatisch versenden |
| **Wo holen** | https://www.beehiiv.com/ oder https://substack.com/ |
| **Kosten** | Beehiiv: Kostenlos bis 2.500 Subscriber; Substack: 10% Provision |
| **Wo eintragen** | Noch nicht im Code - manueller Versand empfohlen bis 100 Abonnenten |

---

### 6. GOOGLE ANALYTICS / SEARCH CONSOLE (SEO-Tracking)

| Feld | Details |
|------|---------|
| **Was** | Website-Analytics und SEO-Tracking |
| **Wofuer** | NicheStream Traffic-Tracking, Landingpage-Performance |
| **Wo holen** | https://analytics.google.com/ |
| **Kosten** | Kostenlos |
| **Wo eintragen** | Tracking-Code in `alphalabs/index.html` und `landing_page/index.html` einfuegen |

---

### 7. ZAPIER (Automatisierung - Phase 2)

| Feld | Details |
|------|---------|
| **Was** | No-Code Automatisierungs-Plattform |
| **Wofuer** | Stripe-Zahlung -> automatisch Kunden-Onboarding, Email-Trigger |
| **Wo holen** | https://zapier.com/ |
| **Kosten** | Free: 100 Tasks/Monat; Professional: $20-50/Monat |

---

## SECRET-UEBERSICHT (Kurzform)

| # | Secret | Pflicht | Kosten/Monat | Wo holen | Wo eintragen |
|---|--------|---------|-------------|----------|--------------|
| 1 | OpenAI API Key | **JA** | $5-400 | platform.openai.com | `creatorfuel/.env` |
| 2 | Stripe Account | **JA** | Transaktionsgeb. | stripe.com | Dashboard |
| 3 | Twitter/X API | Nein | $0-100 | developer.twitter.com | Phase 2 |
| 4 | Email-Postfach | **JA** | $1-12 | Google/Zoho | Handbuch |
| 5 | Beehiiv/Substack | Nein | $0+ | beehiiv.com | Phase 2 |
| 6 | Google Analytics | Nein | Kostenlos | analytics.google.com | HTML-Head |
| 7 | Zapier | Nein | $0-50 | zapier.com | Phase 2 |

---

## KOSTEN-ZUSAMMENFASSUNG

### Minimal-Betrieb (Phase 1)
| Posten | Kosten/Monat |
|--------|-------------|
| OpenAI API (1 Creator, gpt-4o-mini) | ~$10 |
| Stripe (Transaktionsgebuehren) | Variabel |
| Email (Zoho/Google) | ~$1-6 |
| **Gesamt** | **~$11-16/Monat** |

### Vollbetrieb (Phase 3)
| Posten | Kosten/Monat |
|--------|-------------|
| OpenAI API (10 Creator, gemischt) | ~$100-200 |
| Stripe (Transaktionsgebuehren) | Variabel |
| Email | ~$6-12 |
| Newsletter (Beehiiv) | ~$0-39 |
| Zapier | ~$20-50 |
| **Gesamt** | **~$126-301/Monat** |

---

## SICHERHEITS-HINWEISE

1. **Keys NIEMALS in Git committen** - immer .env-Datei verwenden
2. **.env in .gitignore eintragen** - verhindert Accidental Commits
3. **Keys rotieren** - bei Verdacht auf Leck sofort neuen Key generieren
4. **Minimale Berechtigungen** - bei Stripe: nur Payment Links, keine Admin-Rechte verteilen
5. **Zwei-Faktor-Authentifizierung** - fuer alle Accounts aktivieren
6. **Kosten-Alarme** - bei OpenAI und Stripe Spending-Limits setzen

---

*Letzte Aktualisierung: Juli 2026*
