import csv
from pathlib import Path

DATA_FILE = Path(__file__).with_name("grades.csv")

MENU = """
1 - Noten analysieren
2 - Andere CSV-Datei wählen
0 - Beenden
"""


def load_grades(file_path: Path) -> list[tuple[str, int]]:
    """Read and validate grades from a CSV file."""
    grades: list[tuple[str, int]] = []

    with file_path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        if not reader.fieldnames:
            raise ValueError("CSV-Datei ist leer.")

        missing = {"subject", "grade"} - set(reader.fieldnames)
        if missing:
            raise ValueError(
                "CSV-Datei enthält fehlende Pflichtspalte(n): "
                f"{', '.join(sorted(missing))}."
            )

        for line_number, row in enumerate(reader, start=2):
            subject = (row.get("subject") or "").strip()
            grade_text = (row.get("grade") or "").strip()

            if not subject or not grade_text:
                raise ValueError(f"Leerer Wert in CSV-Zeile {line_number}.")

            try:
                grade = int(grade_text)
            except ValueError as error:
                raise ValueError(
                    f"Ungültige Note in CSV-Zeile {line_number}."
                ) from error

            if grade < 2 or grade > 5:
                raise ValueError(
                    f"Note muss zwischen 2 und 5 liegen. "
                    f"Zeile: {line_number}."
                )

            grades.append((subject, grade))

    return grades


def analyze_grades(grades: list[tuple[str, int]]) -> None:
    """Print statistics about the grades."""
    if not grades:
        print("Keine Noten gefunden.")
        return

    average = sum(grade for _, grade in grades) / len(grades)
    best_grade = max(grade for _, grade in grades)
    worst_grade = min(grade for _, grade in grades)

    best_subjects = [
        subject for subject, grade in grades if grade == best_grade
    ]
    worst_subjects = [
        subject for subject, grade in grades if grade == worst_grade
    ]

    print("\nNOTENANALYSE")
    print("=" * 30)
    print(f"Anzahl der Noten: {len(grades)}")
    print(f"Durchschnittsnote: {average:.2f}")
    print(f"Beste Note: {best_grade} ({', '.join(best_subjects)})")
    print(f"Schlechteste Note: {worst_grade} ({', '.join(worst_subjects)})")

    grade_counts = {}
    for subject, grade in grades:
        grade_counts[grade] = grade_counts.get(grade, 0) + 1

    print("\nNOTENVERTEILUNG")
    print("=" * 30)
    for grade in sorted(grade_counts, reverse=True):
        count = grade_counts[grade]
        percentage = count / len(grades) * 100
        unit = "Fach" if count == 1 else "Fächer"
        print(f"Note {grade}: {count} {unit} ({percentage:.1f}%)")


def run_menu(file_path: Path) -> None:
    """Show the menu until the user chooses to quit."""
    while True:
        print(f"\nDatei: {file_path}")
        print(MENU)
        choice = input("Auswahl: ").strip()

        if choice == "1":
            try:
                analyze_grades(load_grades(file_path))
            except (OSError, ValueError) as error:
                print(f"Fehler: {error}")
        elif choice == "2":
            answer = input("Pfad zur CSV-Datei: ").strip()
            if answer:
                file_path = Path(answer)
            else:
                print("Kein Pfad eingegeben, Datei bleibt unverändert.")
        elif choice == "0":
            print("Programm beendet.")
            return
        else:
            print("Ungültige Auswahl. Bitte 0, 1 oder 2 eingeben.")


def main() -> None:
    run_menu(DATA_FILE)


if __name__ == "__main__":
    main()
