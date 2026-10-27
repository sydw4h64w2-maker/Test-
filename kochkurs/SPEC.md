# SPEC – Mias Küche, Folge 1: Pfannkuchen

GOAL:    Kinder und Eltern wollen nach 60 s selbst Pfannkuchen machen und morgen die nächste Folge sehen.
OUTPUT:  HyperFrames, 1920 x 1080, 30 fps
TIME:    60 s x 30 = 1800 frames. Kein Musikbett (kein Anbieter verfügbar), Geräusche auf sichtbaren Aktionen.

LOOK:    Gezeichnete Bilderbuch-Küche, flache Vektorformen mit 6 px Konturen in Tinte.
         Wand: mintgrüne Fliesen #BFE3D0, Fugen #F4FBF7 4 px, Kachel 120 px.
         Arbeitsfläche: Holz #D9965F mit Maserung #C07F4A (Linien 3 px, 35 % Deckkraft).
         Tinte #3A2418 (jede lesbare Schrift, alle Konturen). Akzent Tomatenrot #E8553D:
         nur Mias Schürze, das Rezept-Wort im Titel, die Endkarte.
         Schrift: Nunito 900, Titel 96 px (8,9 % Höhe), Tracking -1 %; Zutaten-Etiketten Nunito 800 44 px.
         Schatten: weich, 0 12 px 0 rgba(58,36,24,.18) (flach, Bilderbuch), keine Unschärfe-Glows.

OBJECTS: Mia (6 J.): braune Locken mit zwei Puffs, rotes Haarband, gelbes Shirt, rote Schürze mit Tasche,
         Sommersprossen, Wangen #F59E8B. Rig: Kopf, Augen (blinzeln), 4 Münder (lächeln, offen, grinsen, kauen),
         Arme an Schulter-Pivots.
         Papas Hand: große Hand #E8B48F, blauer Ärmel #4D7CC2 – er hält die Pfanne (Sicherheit).
         Rezeptbuch rot mit „REZEPTE"; Mehltüte (Papier, „MEHL"), Milchflasche (Glas, blauer Deckel), Eier (braun),
         Salzstreuer, Zuckerdose, Butter in Papier; Rührschüssel (Steingut weiß mit blauem Rand), Schneebesen;
         gusseiserne Pfanne mit Holzgriff; Teller mit Pfannkuchenstapel und Sirup.

MOTION:  Ankunft expo.out / back.out(1.6) für Dinge, die fallen (verspielt, Dämpfung ~0.5);
         Kamera power2.inOut; Abgänge power3.in, 40 % kürzer. Wörter 0.07 s Stagger, blur 6→0.
         Figur: Kopf führt, Arme folgen 3–5 Frames später; nie beide Arme gleich.

SHOTS:
 1  0.0–7.0   Intro, Frontal: Buch fällt ab Frame 0 und knallt (0.4 s) auf die Fläche, Mia beugt sich vor, Mund offen.
              „Heute:" / „Pfannkuchen!" (Akzent) ab 1.0 s, hält bis 5.6 s. Ton: Buch-Knall.
              Übergabe: Kamera stößt ins Buch (5.9–7.0 s), die Seite füllt das Bild.
 2  7.0–21.0  Zutaten, Draufsicht: Buchseite fliegt nach oben weg und gibt die Arbeitsfläche frei.
              Kinderhand legt nacheinander ab: 200 g Mehl, 300 ml Milch, 2 Eier, 1 Prise Salz, 1 EL Zucker,
              Butter zum Braten (alle ~1.8 s), Etikett erscheint mit Pop. Zum Schluss Schüssel in die Mitte.
              Übergabe: Schüssel bleibt gleich groß an gleicher Stelle (Match Cut).
 3 21.0–33.0  Rühren, Draufsicht Schüssel: „Mehl, Zucker, Salz" rieselt hinein, „2 Eier" (Eigelb erscheint),
              „Milch dazu – rühren!" Schneebesen kreist, Teig wird glatt. 29.6 s Mehlwolke füllt Bild weiß,
              dann Großaufnahme Mia mit Mehl auf der Nase, lacht. Übergabe: Wisch nach links.
 4 33.0–46.0  Braten, Frontal: Herd, Papa hält die Pfanne, Mia auf Hocker daneben, zeigt.
              Zeile „Am Herd hilft immer ein Großer". Teig fließt, Blasen, wird goldbraun.
              40.5 s Wenden: Pfannkuchen fliegt im Bogen, dreht sich, landet. Mia jubelt. Ton: Whoosh.
              Übergabe: Pfannkuchen gleitet nach rechts auf den Stapel.
 5 46.0–54.0  Probieren, Frontal: Stapel mit Sirup, Mia nimmt einen Bissen, kaut, Augen zu – „Mmmh!" mit Glitzer.
              Übergabe: Rote Farbflut (Schürzenrot) aus der Mitte.
 6 54.0–60.0  Endkarte: Rot, „Mias Küche" baut sich Buchstabe für Buchstabe, darunter „Morgen: Pizza-Schnecken",
              Mia winkt. Hält 2.5 s. Ton: Chime.

BANNED:  dunkler Hintergrund; Glows, Partikel als Deko; lila/blaue Verläufe; Glaskarten;
         Creme-Papier + Serif; alles zentriert und gleichzeitig eingeblendet; Titel, die nach der Landung treiben;
         Eckenlabels, Logo in der Ecke; drei Karten in einer Reihe; Zutatenliste als Aufzählung.
QA:      0.0 (Thumbnail: Buch + Mia), 3.0 (Titel lesbar), 15.0 (Zutaten mit Etiketten), 27.0 (Teig + Schneebesen),
         31.5 (Mehlnase), 41.0 (Pfannkuchen in der Luft), 51.0 (Mmmh), 58.5 (Endkarte).
