# CreatorFuel — Onboarding-Template

**Zweck:** Strukturiertes Onboarding für neue CreatorFuel-Kunden
**Dauer:** 30-45 Minuten (Gespräch) + 15 Minuten (Setup)
**Ziel:** Kunde versteht das Produkt, Erwartungen sind abgestimmt, erster Post wird generiert

---

## PHASE 1: VOR DEM GESPRÄCH (Du)

### Checkliste
- [ ] Stripe Checkout-Link bereit
- [ ] Google Sheet "Kunden-Tracking" geöffnet
- [ ] Onboarding-Fragenbogen bereit (Kopie für Kunden)
- [ ] Beispiel-Style-Profil bereit (als Demo)

### Materialien
- Onboarding-Fragenbogen (siehe unten)
- Beispiel-Posts (zeige, wie die KI arbeitet)
- Preisübersicht
- FAQ-Liste

---

## PHASE 2: DAS ONBOARDING-GESPRÄCH (30-45 Min)

### Begrüßung (5 Min)

```
"Hi [Name], schön dass du Zeit nimmst. Kurz zum Ablauf: 
Wir reden 30 Minuten über deinen Content, deine Ziele und deinen Stil. 
Danach habe ich alles, was ich brauche — und deine ersten Posts sind 
in 24 Stunden ready."
```

### Teil 1: Ziele & Erwartungen (10 Min)

**Fragen:**
1. "Was ist dein Hauptziel? Mehr Reichweite, mehr Engagement, mehr Verkäufe?"
2. "Wie oft postest du aktuell? Wie oft würdest du gerne posten?"
3. "Was ist dein größter Pain Point beim Content erstellen?"
4. "Hast du schonmal KI-Tools ausprobiert? Was war gut/schlecht?"

**Ziel:** Verstehen, was der Kunde wirklich braucht — nicht was er sagt.

### Teil 2: Stil-Analyse (15 Min)

**Aufforderung:**
```
"Schick mir jetzt die Links zu deinen 20 besten Posts — die mit den 
meisten Likes, Shares oder Kommentaren. Ich analysiere deinen Tonfall, 
deine Hooks und deine wiederkehrenden Formate. Das wird das 
Style-Profil, nach dem die KI arbeitet."
```

**Alternativ:** Kunde teilt Bildschirm und zeigt seine Posts.

**Während der Analyse (live):**
- Notiere wiederkehrende Muster
- Frage nach: "Warum hat dieser Post so gut performt?"
- Identifiziere "Secret Sauce" — was macht den Kunden einzigartig?

### Teil 3: Format & Plattform (10 Min)

**Fragen:**
1. "Auf welchen Plattformen bist du aktiv?"
2. "Welche Content-Formate nutzt du am häufigsten?" (Reels, Carousels, Stories, Text-Posts)
3. "Soll ich Hashtags mitliefern? Wie viele?"
4. "Sollen die Posts sofort veröffentlicht werden oder willst du sie vorher sehen?"
5. "Gibt es Tabus oder Themen, die ich vermeiden soll?"

### Teil 4: Abschluss & Nächste Schritte (5 Min)

```
"Perfekt, ich habe alles was ich brauche. Nächste Schritte:

1. Du zahlst über den Stripe-Link (den schicke ich dir nach dem Call)
2. Ich erstelle dein Style-Profil (heute Abend fertig)
3. Deine ersten Posts sind morgen um [Uhrzeit] in deinem Postfach
4. Jeden Morgen bekommst du die Posts für den Tag

Fragen?"
```

**Wichtig:** Keine Garantien für virale Posts! Realistische Erwartungen setzen.

---

## PHASE 3: NACH DEM GESPRÄCH (Du)

### Sofort (15 Min)

- [ ] Stripe Checkout-Link an Kunden senden
- [ ] Kundendaten in Google Sheet eintragen
- [ ] Style-Analyse mit KI durchführen
- [ ] Style-Profil als JSON speichern

### Innerhalb von 24 Stunden

- [ ] Erste 7 Posts generieren
- [ ] Posts reviewen und anpassen
- [ ] Per Email an Kunden senden
- [ ] Bestätigungs-Email schreiben

---

## ONBOARDING-FRAGENBOGEN

**(An Kunden senden — kann vor oder während des Gesprächs ausgefüllt werden)**

```
CREATORFUEL — ONBOARDING-FRAGENBOGEN

BASICS
1. Dein Name / Brand Name: ___________________
2. Deine Plattformen: □ TikTok □ Instagram □ YouTube □ Twitter/X □ LinkedIn □ Other: ___
3. Follower-Zahlen (pro Plattform):
   TikTok: _____ Instagram: _____ YouTube: _____ Twitter: _____
4. Deine Nische (so spezifisch wie möglich): ___________________

ZIELE
5. Dein Hauptziel (wähle eines):
   □ Mehr Reichweite (Views, Impressions)
   □ Mehr Engagement (Likes, Kommentare, Shares)
   □ Mehr Verkäufe (Produkte, Kurse, Coaching)
   □ Community-Aufbau
   □ Andere: ___________________

6. Wie oft postest du aktuell? _______ Wie oft willst du posten? _______

CONTENT
7. Was sind deine 3 besten Posts aller Zeiten? (Links)
   1. ___________________
   2. ___________________
   3. ___________________

8. Was ist dein "Secret Sauce"? Was macht deinen Content einzigartig?
   ___________________

9. Was soll ich NICHT tun? (Tabus, No-Gos, vermeidete Themen)
   ___________________

ZIELGRUPPE
10. Wer ist deine perfekte Zuschauerin/Zuschauer? (Alter, Interessen, Pain Points)
    ___________________

LOGISTIK
11. Soll ich Hashtags mitliefern? □ Ja □ Nein
12. Willst du Posts vor Veröffentlichung sehen? □ Ja □ Nein
13. Wie möchtest du die Posts erhalten? □ Email □ WhatsApp □ Discord □ Other: ___
14. Beste Zeit für den Post-Versand: ___________________
```

---

## BEISPIEL-STYLE-PROFIL

**(Zeige dies als Demo während des Onboardings)**

```json
{
  "creator_name": "Lena K.",
  "niche": "Fitness & Lifestyle",
  "tonality": "motivierend, persönlich, etwas sarkastisch",
  "hook_types": ["Frage-Hook", "Zahlen-Hook", "Kontrast-Hook"],
  "sentence_style": "kurze Sätze, viele Absätze, direkte Anrede",
  "emoji_frequency": "3-5 pro Post",
  "top_emojis": ["💪", "🔥", "✨", "😅"],
  "hashtag_count": 5,
  "hashtag_style": "Nischen-Hashtags + 1-2 breite",
  "cta_style": "Frage an Community",
  "content_pillars": ["Workouts", "Ernährung", "Mindset", "Behind the Scenes"],
  "unique_markers": "Nutzt oft 'Mädels' als Anrede, beendet mit rhetorischen Fragen"
}
```

---

## ERSTE-POSTS-EMAIL-TEMPLATE

```
Betreff: Deine ersten CreatorFuel Posts sind ready! 🎉

Hi [Name],

hier sind deine ersten 7 Posts — eine Woche Vorrat:

---
MONTAG — [Plattform]
[Post-Text]

---
DIENSTAG — [Plattform]
[Post-Text]

---
[... weitere Tage ...]

---

WICHTIG:
• Diese Posts basieren auf deinem Style-Profil. Je mehr Feedback du gibst, 
  desto besser werden sie.
• Schick mir gerne Änderungswünsche — ich passe das Profil an.
• Ab morgen bekommst du täglich deine Posts um [Uhrzeit].

Fragen? Einfach antworten!

[Dein Name]
CreatorFuel by Alpha Labs
```

---

## FEHLER, DIE DU VERMEIDEN SOLLTEST

| Fehler | Warum | Lösung |
|--------|-------|--------|
| Zu viel versprechen | Kunde erwartet Wunder | Realistische Erwartungen setzen |
| Style-Profil zu oberflächlich | Posts klingen generisch | Mindestens 20 Posts analysieren |
| Keine Tabus klären | Kunde ist geschockt | Immer nach No-Gos fragen |
| Kein Follow-up | Kunde fühlt sich vergessen | Nach 3 Tagen nachfragen |
| Zu technisch erklären | Kunde versteht nicht | Einfach halten: "Ich mache das für dich" |

---

**→ Ein gutes Onboarding ist der Unterschied zwischen einem Kunden, der nach 1 Monat kündigt — und einem, der für Jahre bleibt.**
