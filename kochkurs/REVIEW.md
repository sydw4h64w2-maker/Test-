# REVIEW – Mias Küche, Folge 1: Pfannkuchen

**Gebaut:** Storyline A („Mias Küche"), gezeichneter Bilderbuch-Stil, 60 s, 1920×1080, 30 fps.
Nicht gebaut: B („Baby-Chef"), C („Eine Einstellung") – siehe STORYLINES.md.

## Entscheidungen
- Kostenlos gezeichnet statt realistisch: für echt wirkende Aufnahmen fehlt ein HeyGen-Zugang.
- Sicherheit: Am Herd hält Papa die Pfanne, Zeile „Am Herd hilft immer ein Großer".
- Echtes Grundrezept: 200 g Mehl, 300 ml Milch, 2 Eier, 1 Prise Salz, 1 EL Zucker, Butter zum Braten.
- GSAP liegt lokal in assets/lib (CDN ist aus dem Render-Browser nicht erreichbar).
- CLI 0.8.208 statt der vom Plugin gepinnten 0.8.209 (noch nicht auf npm).

## Geprüft
- `check`: 0 Fehler. Übrige Layout-Warnungen = Zutaten/Hände, die außerhalb des Bildes auf ihren Auftritt warten (gewollt).
- Snapshots aller Szenen, Übergänge und Beats angesehen; Schüssel- und Pfannen-Animationen nach erstem Durchgang korrigiert.
- Ton gemessen, nicht gehört: Treffer liegen auf den Aktionen, −18.8 LUFS, True Peak −6 dB, kein Clipping.

## Schwächen / nächste Schritte
- Keine Musik (kein Musik-Anbieter in dieser Sitzung); nur Effekt-Sounds aus der Standardbibliothek
  (Pop/Whoosh/Glitzer/Chime) – keine echten Küchengeräusche (Openverse nicht erreichbar).
- Schwächste Szene: Zutaten – die Hand legt alles gleich ab; Etiketten sind auf dem Handy klein.
- Mia winkt auf der Endkarte nur kurz.
