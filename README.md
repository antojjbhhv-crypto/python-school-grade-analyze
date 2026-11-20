# School Grade Analyzer

Ein kleines Python-Projekt zur Analyse von Schulnoten aus einer CSV-Datei.

Das Projekt wurde als selbstständiges Lernprojekt entwickelt, um meine Kenntnisse in Python, Datenverarbeitung und Softwaretests zu verbessern.

## Funktionen

- Laden von Noten aus einer CSV-Datei
- Überprüfung der Eingabedaten
- Berechnung der durchschnittlichen Note
- Ermittlung der besten und schlechtesten Note
- Anzeige der Notenverteilung
- Berechnung der prozentualen Verteilung
- Behandlung von ungültigen Eingaben
- interaktives Menü
- Auswahl einer eigenen CSV-Datei

## Technologien

- Python 3
- CSV
- pathlib
- unittest

Das Projekt verwendet ausschließlich Python-Standardbibliotheken.

## Projektstruktur

```text
python-grade-analyzer/
├── main.py
├── test_main.py
├── grades.csv
├── README.md
└── .gitignore
```

## Installation

Python 3 muss installiert sein.

Repository herunterladen oder klonen.

## Verwendung

Das Programm starten:

```bash
py main.py
```

Danach erscheint ein Menü:

```text
1 - Noten analysieren
2 - Andere CSV-Datei wählen
0 - Beenden
```

Mit `1` werden die Noten der aktuellen Datei analysiert, mit `2` kann ein
anderer Pfad zu einer CSV-Datei eingegeben werden, mit `0` wird das Programm
beendet.

Beispielausgabe:

```text
NOTENANALYSE
==============================
Anzahl der Noten: 5
Durchschnittsnote: 3.60
Beste Note: 5 (Informatik)
Schlechteste Note: 2 (Chemie)

NOTENVERTEILUNG
==============================
Note 5: 1 Fach (20.0%)
Note 4: 2 Fächer (40.0%)
Note 3: 1 Fach (20.0%)
Note 2: 1 Fach (20.0%)
```

## Beispieldaten

Die Datei `grades.csv` enthält fünf fiktive Beispieldatensätze:

```csv
subject,grade
Mathematik,4
Physik,3
Informatik,5
Englisch,4
Chemie,2
```

Die Noten werden nach dem russischen Fünf-Punkte-System ausgewertet.

## Tests

Die automatischen Tests starten:

```bash
py -m unittest -v
```

Aktuell enthält das Projekt sechs Tests.

Die Tests überprüfen unter anderem:

- gültige CSV-Dateien
- fehlende oder leere Dateien
- ungültige Noten
- falsche CSV-Spalten
- die Berechnung der Notenstatistik
- leere Notenlisten

## Lernziele

Mit diesem Projekt möchte ich meine Kenntnisse in folgenden Bereichen erweitern:

- Python-Programmierung
- Funktionen und Datenstrukturen
- Fehlerbehandlung
- CSV-Verarbeitung
- Automatisierte Tests
- Git und GitHub

## Projektstatus

Version 1.4 – Notenanalyse, interaktives Menü, Auswahl einer eigenen CSV-Datei und automatisierte Tests implementiert.

Das Projekt wird im Rahmen meiner Vorbereitung auf eine Ausbildung zum Fachinformatiker für Anwendungsentwicklung weiterentwickelt.
