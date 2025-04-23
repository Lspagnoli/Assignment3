import unittest
class GradeSystem:
    def __init__(self):
        self.L1 = ["Alice", "Bob", "Charlie", "Diana", "Joane", "Marta", "James", "Michael"]
        self.L2 = [85, 92, 78, 88, 91, 74, 95, 89]
        self.L3 = []
        for i in range(len(self.L1)):
            x = self.L1[i]
            y = self.L2[i]
            self.L3.append((x, y))
        self.L4 = {}
        for pair in self.L3:
            self.L4[pair[0]] = pair[1]
        self.L5 = sum(self.L2)
        self.L6 = len(self.L2)
        self.L7 = self.L5 / self.L6 if self.L6 != 0 else 0
        self.L8 = max(self.L2)
        self.L9 = min(self.L2)
        self.L10 = []
        for i in range(self.L6):
            if self.L2[i] >= 90:
                self.L10.append(self.L1[i])
        self.L11 = ""
        for n in self.L1:
            self.L11 += n + ", "
        self.L12 = sorted(self.L3, key=lambda z: z[1], reverse=True)
        self.L13 = [z[0] for z in self.L12]
        self.L14 = [z[1] for z in self.L12]
        self.L15 = True if all(g >= 50 for g in self.L2) else False

    def display_all(self):
        print("All Students and Grades:", self.L3)
        print("Student to Grade Map:", self.L4)
        print("Average Grade:", self.L7)
        print("Highest Grade:", self.L8)
        print("Lowest Grade:", self.L9)
        print("Students with A (90+):", self.L10)
        print("Names in one string:", self.L11)
        print("Sorted Names (by Grade):", self.L13)
        print("Sorted Grades:", self.L14)
        print("Everyone Passed:", self.L15)

class TestGradeSystem(unittest.TestCase):
    def setUp(self):
        self.gs = GradeSystem()

    def test_average_grade(self):
        self.assertAlmostEqual(self.gs.L7, sum(self.gs.L2) / len(self.gs.L2))

    def test_students_with_A(self):
        self.assertListEqual(self.gs.L10, ["Bob", "Joane", "James"])

    def test_all_passed(self):
        self.assertTrue(self.gs.L15)

if __name__ == '__main__':
    unittest.main()
