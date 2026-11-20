import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from main import load_grades, analyze_grades


class TestLoadGrades(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.file_path = Path(self.temp_dir.name) / "grades.csv"

    def test_loads_valid_csv(self):
        self.file_path.write_text(
            "subject,grade\nMathematik,4\nInformatik,5\n",
            encoding="utf-8"
        )

        result = load_grades(self.file_path)

        self.assertEqual(
            result,
            [("Mathematik", 4), ("Informatik", 5)]
        )

    def test_unusable_file(self):
        missing_file = Path(self.temp_dir.name) / "missing.csv"

        with self.subTest("missing file"):
            with self.assertRaises(FileNotFoundError):
                load_grades(missing_file)

        with self.subTest("empty file"):
            self.file_path.write_text("", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "CSV-Datei ist leer"):
                load_grades(self.file_path)

    def test_missing_required_columns(self):
        self.file_path.write_text(
            "name,score\nMathematik,4\n",
            encoding="utf-8"
        )

        with self.assertRaisesRegex(ValueError, "fehlende Pflichtspalte"):
            load_grades(self.file_path)

    def test_invalid_grade(self):
        with self.subTest("out of range"):
            self.file_path.write_text(
                "subject,grade\nMathematik,6\n",
                encoding="utf-8"
            )

            with self.assertRaisesRegex(ValueError, "zwischen 2 und 5"):
                load_grades(self.file_path)

        with self.subTest("not a number"):
            self.file_path.write_text(
                "subject,grade\nMathematik,excellent\n",
                encoding="utf-8"
            )

            with self.assertRaisesRegex(ValueError, "Ungültige Note"):
                load_grades(self.file_path)


class TestAnalyzeGrades(unittest.TestCase):
    def test_analyze_grades_output(self):
        grades = [
            ("Mathematik", 4),
            ("Informatik", 5),
            ("Englisch", 5),
        ]

        output = io.StringIO()
        with redirect_stdout(output):
            analyze_grades(grades)

        result = output.getvalue()

        self.assertIn("Durchschnittsnote: 4.67", result)
        self.assertIn("Beste Note: 5", result)
        self.assertIn("Schlechteste Note: 4", result)
        self.assertIn("Note 5: 2 Fächer", result)
        self.assertIn("Note 5: 2 Fächer (66.7%)", result)

    def test_empty_grades_list(self):
        output = io.StringIO()
        with redirect_stdout(output):
            analyze_grades([])

        self.assertEqual(
            output.getvalue().strip(),
            "Keine Noten gefunden."
        )


if __name__ == "__main__":
    unittest.main()
