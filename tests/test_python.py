"""Behavioral tests, including strict boundary and real CLI input."""
import math
import os
from pathlib import Path
import subprocess
import sys
import unittest

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))
from mygroup import average_mark, filter_students, groupmates


class PythonTasksTests(unittest.TestCase):
    def run_program(self, name, input_text=None):
        return subprocess.run([sys.executable, str(SRC / name)], input=input_text,
                              capture_output=True, text=True, encoding="utf-8",
                              env=dict(os.environ, PYTHONIOENCODING="utf-8"), timeout=10)

    def test_hello_world(self):
        result = self.run_program("helloworld.py")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello world!")

    def test_group_data(self):
        self.assertEqual(len(groupmates), 6)
        self.assertEqual((groupmates[0]["surname"], groupmates[0]["name"],
                          groupmates[0]["patronymic"], groupmates[0]["group"]),
                         ("Морозов", "Алексей", "Ильич", "БСТ0001"))
        for student in groupmates:
            self.assertEqual(set(student), {"name", "surname", "patronymic", "group", "exams", "marks"})
            self.assertEqual(student["group"], "БСТ0001")
            self.assertEqual(len(student["exams"]), len(student["marks"]))
            self.assertTrue(all(2 <= mark <= 5 for mark in student["marks"]))

    def test_strict_boundary_and_order(self):
        self.assertEqual([s["surname"] for s in filter_students(groupmates, 4)],
                         ["Смирнов", "Соколова", "Волков"])

    def test_upper_boundary_empty(self):
        self.assertEqual(filter_students(groupmates, 5), [])

    def test_lower_boundary_all(self):
        self.assertEqual(filter_students(groupmates, 0), groupmates)

    def test_decimal_threshold(self):
        self.assertEqual([s["surname"] for s in filter_students(groupmates, 4.5)],
                         ["Смирнов", "Соколова"])

    def test_empty_input_and_no_mutation(self):
        self.assertEqual(filter_students([], 4), [])
        original = repr(groupmates)
        filter_students(groupmates, 4)
        self.assertEqual(repr(groupmates), original)

    def test_empty_marks_rejected(self):
        with self.assertRaises(ValueError):
            average_mark({"marks": []})

    def test_nonfinite_threshold_rejected(self):
        for value in (math.nan, math.inf, -math.inf):
            with self.assertRaises(ValueError):
                filter_students(groupmates, value)

    def test_keyboard_input(self):
        result = self.run_program("mygroup.py", "4\n")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Найдено студентов: 3", result.stdout)
        self.assertIn("Морозов Алексей Ильич", result.stdout)
        self.assertIn("БСТ0001", result.stdout)

    def test_bad_input_retried_and_decimal_comma(self):
        result = self.run_program("mygroup.py", "abc\nnan\ninf\n-1\n6\n4,5\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.count("Ошибка:"), 5)
        self.assertIn("Найдено студентов: 2", result.stdout)

    def test_eof_returns_error(self):
        result = self.run_program("mygroup.py", "")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Ввод отменён", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
