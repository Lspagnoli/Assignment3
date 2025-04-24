class GradeSystem:
    def __init__(self):
        self.students = [
            {"name": "Alice", "grade": 85},
            {"name": "Bob", "grade": 92},
            {"name": "Charlie", "grade": 78},
            {"name": "Diana", "grade": 88},
            {"name": "Joane", "grade": 91},
            {"name": "Marta", "grade": 74},
            {"name": "James", "grade": 95},
            {"name": "Michael", "grade": 89},
        ]


        self.name_to_grade = {student["name"]: student["grade"] for student in self.students}
        self.average_grade = self.calculate_average()
        self.highest_grade = max(student["grade"] for student in self.students)
        self.lowest_grade = min(student["grade"] for student in self.students)
        self.a_students = [student["name"] for student in self.students if student["grade"] >= 90]
        self.names_string = ", ".join(student["name"] for student in self.students)
        self.sorted_students = sorted(self.students, key=lambda s: s["grade"], reverse=True)
        self.everyone_passed = all(student["grade"] >= 50 for student in self.students)

    def calculate_average(self):
        total = sum(student["grade"] for student in self.students)
        count = len(self.students)
        return total / count if count > 0 else 0

    def display_summary(self):
        print("All Students and Grades:")
        for student in self.students:
            print(f"{student['name']}: {student['grade']}")

        print("\nStudent to Grade Map:", self.name_to_grade)
        print("Average Grade:", self.average_grade)
        print("Highest Grade:", self.highest_grade)
        print("Lowest Grade:", self.lowest_grade)
        print("Students with A (90+):", self.a_students)
        print("All Names:", self.names_string)
        print("Sorted by Grade:", [(s['name'], s['grade']) for s in self.sorted_students])
        print("Everyone Passed:", self.everyone_passed)


import unittest

class TestGradeSystem(unittest.TestCase):
    def setUp(self):
        self.gs = GradeSystem()

    def test_average_grade(self):
        expected_avg = sum(s["grade"] for s in self.gs.students) / len(self.gs.students)
        self.assertAlmostEqual(self.gs.average_grade, expected_avg)
        print("test_average_grade [PASSED]")

    def test_name_to_grade_map(self):
        for student in self.gs.students:
            self.assertEqual(self.gs.name_to_grade[student["name"]], student["grade"])
        print("test_name_to_grade_map [PASSED]")

    def test_highest_grade(self):
        self.assertEqual(self.gs.highest_grade, max(s["grade"] for s in self.gs.students))
        print("test_highest_grade [PASSED]")

    def test_lowest_grade(self):
        self.assertEqual(self.gs.lowest_grade, min(s["grade"] for s in self.gs.students))
        print("test_lowest_grade [PASSED]")

    def test_a_students(self):
        expected_a_students = [s["name"] for s in self.gs.students if s["grade"] >= 90]
        self.assertListEqual(self.gs.a_students, expected_a_students)
        print("test_a_students [PASSED]")

    def test_everyone_passed(self):
        self.assertTrue(self.gs.everyone_passed)
        print("test_everyone_passed [PASSED]")

    def test_sorted_students(self):
        grades = [s["grade"] for s in self.gs.sorted_students]
        self.assertEqual(grades, sorted(grades, reverse=True))
        print("test_sorted_students [PASSED]")

if __name__ == '__main__':
    unittest.main()
