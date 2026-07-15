# Stripe Setup für Alpha Labs

**Zweck:** Zahlungsabwicklung für CreatorFuel und Alpha Signal Pro
**Zeitaufwand:** 30-45 Minuten (einmalig)
**Kosten:** Keine monatlichen Gebühren, nur pro Transaktion (1.5% + €0.25)

---

## SCHRITT 1: ACCOUNT ERSTELLEN

1. Auf [stripe.com](https://stripe.com) gehen
2. "Start now" oder "Sign up" klicken
3. Email-Adresse eingeben (Geschäfts-Email empfohlen)
4. Vollständigen Namen eingeben
5. Land auswählen (Deutschland / Österreich / Schweiz)
6. Passwort erstellen
7. Email verifizieren (Link in Email klicken)

---

## SCHRITT 2: KONTO VERIFIZIEREN

**Wichtig:** Ohne Verifizierung kannst du keine Zahlungen empfangen.

### Geschäftsinformationen

1. Im Dashboard: "Activate your account" oder "Get started"
2. Folgende Informationen eingeben:

| Feld | Was eingeben |
|------|-------------|
| Business type | "Individual" oder "Sole proprietorship" (Einzelunternehmer) |
| Business name | "Alpha Labs" oder dein Name |
| Business website | alphalabs.io (oder falls noch nicht live: "In development") |
| Industry | "Software" oder "Digital services" |
| Business description | "AI-powered content generation for social media creators" |

### Persönliche Informationen

| Feld | Was eingeben |
|------|-------------|
| Legal name | Dein vollständiger Name |
| Geburtsdatum | Dein Geburtsdatum |
| Adresse | Deine vollständige Adresse |
| Telefonnummer | Deine Handynummer (für Verifizierung) |

### Bankkonto verknüpfen

1. "Add bank account" klicken
2. IBAN eingeben
3. Bank bestätigen

**Wichtig:** Das Bankkonto muss auf deinen Namen laufen (oder den Firmennamen, falls du eine Firma hast).

### Identitätsverifizierung

1. Dokument auswählen: Personalausweis oder Reisepass
2. Foto des Dokuments hochladen (Vorder- und Rückseite)
3. Optional: Selfie für Gesichtserkennung

**Bearbeitungszeit:** In der Regel innerhalb von 24 Stunden. Manchmal sofort.

---

## SCHRITT 3: PRODUKTE ERSTELLEN

### CreatorFuel — Starter (€99/Monat)

1. Im Dashboard: "Products" → "Add product"
2. Name: "CreatorFuel Starter"
3. Description: "1 Post/Tag, 1 Plattform, Email-Support"
4. "Add pricing" klicken
5. Preis: €99.00
6. "Recurring" auswählen
7. Billing period: "Monthly"
8. "Save product"

### CreatorFuel — Pro (€249/Monat)

1. "Add product"
2. Name: "CreatorFuel Pro"
3. Description: "3 Posts/Tag, 3 Plattformen, Priority-Support, Trend-Reports"
4. Preis: €249.00
5. "Recurring", "Monthly"
6. "Save product"

### CreatorFuel — Agency (€499/Monat)

1. "Add product"
2. Name: "CreatorFuel Agency"
3. Description: "5 Posts/Tag, alle Plattformen, Dedicated Support, Strategie-Calls"
4. Preis: €499.00
5. "Recurring", "Monthly"
6. "Save product"

### Alpha Signal Pro (€49/Monat)

1. "Add product"
2. Name: "Alpha Signal Pro"
3. Description: "Deep Dives, Market Maps, Early Access, Private Community"
4. Preis: €49.00
5. "Recurring", "Monthly"
6. "Save product"

---

## SCHRITT 4: CHECKOUT-LINKS ERSTELLEN

Checkout-Links sind die einfachste Möglichkeit, Kunden zur Zahlung zu schicken.

### Für CreatorFuel Starter

1. Auf "CreatorFuel Starter" klicken
2. "Create payment link" klicken
3. Einstellungen prüfen:
   - Collect tax: "Automatic" (Stripe berechnet MwSt. automatisch)
   - Allow promotion codes: Optional (für Rabatte)
4. "Create link"
5. Link kopieren → speichern in Google Sheet

**Der Link sieht so aus:**
`https://buy.stripe.com/xxxxx/xxxxx`

### Für alle anderen Produkte wiederholen

Wiederhole den Prozess für:
- CreatorFuel Pro
- CreatorFuel Agency
- Alpha Signal Pro

---

## SCHRITT 5: DASHBOARD-ÜBERSICHT

### Wichtige Metriken im Blick behalten

| Metrik | Wo finden | Bedeutung |
|--------|----------|-----------|
| **MRR** | Dashboard → Home | Monthly Recurring Revenue — deine monatlichen Einnahmen |
| **Active Subscriptions** | Dashboard → Customers | Wie viele aktive Kunden |
| **Churn Rate** | Dashboard → Analytics | Wie viele kündigen pro Monat (Ziel: < 5%) |
| **Failed Payments** | Dashboard → Payments | Zahlungen, die nicht durchgingen |

### Kunden verwalten

1. "Customers" im Menü
2. Hier siehst du alle Kunden mit:
   - Email
   - Subscription-Status
   - Zahlungshistorie
   - Möglichkeit: Subscription pausieren/kündigen

---

## SCHRITT 6: EMAIL-BENACHRICHTIGUNGEN EINRICHTEN

### Wichtige Events, bei denen du benachrichtigt werden solltest

1. "Settings" → "Account settings" → "Email notifications"
2. Folgende aktivieren:
   - [ ] Successful payments
   - [ ] Failed payments
   - [ ] Subscription cancellations
   - [ ] Disputes (Chargebacks)
   - [ ] Payouts (Auszahlungen)

---

## SCHRITT 7: TEST-TRANSAKTION

**Wichtig:** Vor dem Live-Betrieb solltest du eine Test-Zahlung durchführen.

### Test-Modus nutzen

1. Im Dashboard: Rechts oben "Test mode" togglen
2. Einen Checkout-Link im Test-Modus erstellen
3. Mit Test-Kreditkarte bezahlen:
   - Kartennummer: `4242 4242 4242 4242`
   - Ablaufdatum: Ein beliebiges zukünftiges Datum
   - CVC: Beliebige 3 Ziffern
4. Prüfen, ob die Subscription im Dashboard erscheint

### Von Test zu Live

1. "Test mode" togglen (aus)
2. Neue Checkout-Links im Live-Modus erstellen
3. Diese Links an echte Kunden senden

---

## GEBÜHREN & AUSZAHLUNGEN

### Transaktionsgebühren

| Art | Gebühr |
|-----|--------|
| Europäische Karten | 1.5% + €0.25 |
| Nicht-europäische Karten | 3.25% + €0.25 |

**Beispiel:** €99 Zahlung
- Gebühr: €99 × 1.5% + €0.25 = €1.49 + €0.25 = €1.74
- Du erhältst: €99 - €1.74 = €97.26

### Auszahlungen

- Automatisch auf dein Bankkonto
- Täglich, wöchentlich oder monatlich (einstellbar)
- Bearbeitungszeit: 2-7 Werktage
- Minimum: Kein Minimum

**Einstellung:**
1. "Settings" → "Account settings" → "Payout schedule"
2. "Automatic" wählen
3. Frequenz: "Daily" (täglich) oder "Weekly" (wöchentlich)

---

## STEUERHINWEISE

### MwSt. (Deutschland)

- Digitalleistungen an EU-Kunden: MwSt. fällig an
- Stripe kann MwSt. automatisch berechnen und abführen
- Einstellung: "Settings" → "Tax" → "Stripe Tax" aktivieren

### Einnahmen versteuern

- Einnahmen müssen in der Steuererklärung angegeben werden
- Gewerbe anmelden (wenn nicht schon geschehen)
- Steuerberater empfohlen ab €5.000/Monat

---

## WICHTIGE STRIPE-FUNKTIONEN

### Subscription-Management

- Kunden können selbst kündigen (Customer Portal)
- Du kannn Subscriptions pausieren (z.B. für Urlaub)
- Upgrades/Downgrades automatisch berechnet

### Rechnungen

- Automatische Rechnungen generieren
- "Settings" → "Account settings" → "Invoice settings"
- Kunden erhalten Rechnung per Email

### Rückerstattungen

1. "Payments" → Zahlung finden
2. "Refund" klicken
3. Vollständig oder teilweise
4. Grund angeben

---

## SICHERHEIT

### Zwei-Faktor-Authentifizierung (2FA)

**Unbedingt aktivieren!**

1. "Settings" → "Account settings" → "Two-step authentication"
2. Authentifizierungs-App wählen (Google Authenticator, Authy)
3. QR-Code scannen
4. Backup-Codes speichern (an sicherem Ort)

### API-Key (für Entwickler)

Falls du Stripe API nutzen willst:
1. "Developers" → "API keys"
2. "Standard keys" → "Secret key" (nur im Test-Modus!)
3. Für Live: "Restricted keys" erstellen

---

## FEHLERBEHEBUNG

| Problem | Lösung |
|---------|--------|
| Verifizierung abgelehnt | Dokumente prüfen, klare Fotos machen, Support kontaktieren |
| Zahlung fehlgeschlagen | Kunde hat ungültige Karte → neuen Link senden |
| Keine Auszahlung | Bankkonto prüfen, Auszahlungsplan checken |
| MwSt. nicht berechnet | Stripe Tax aktivieren, Steuereinstellungen prüfen |
| Kunde will kündigen | Customer Portal Link senden oder im Dashboard kündigen |

---

## ZUSAMMENFASSUNG

| Schritt | Status | Zeit |
|---------|--------|------|
| Account erstellen | ☐ | 5 min |
| Konto verifizieren | ☐ | 15 min |
| Produkte erstellen | ☐ | 10 min |
| Checkout-Links erstellen | ☐ | 10 min |
| Test-Transaktion | ☐ | 5 min |
| 2FA aktivieren | ☐ | 5 min |
| Email-Benachrichtigungen | ☐ | 5 min |

**Gesamtzeit: ~60 Minuten**

---

**→ Stripe ist jetzt eingerichtet. Du kannst Zahlungen empfangen. Weiter zum ersten Kunden!**
