import unittest

from main import *

class TestAssignment(unittest.TestCase):

    def test_part1(self):
        self.assertIsInstance(GRADE, dict, msg="GRADE is not a dict")
        for score, grade in GRADE.items():
            self.assertIsInstance(score, int,
                                  msg=f"GRADE key {score} should be {int}, got {type(score)}")
            self.assertGreaterEqual(score, 0,
                                    msg=f"GRADE key {score} should be between 0 to 100, got {score}")
            self.assertLessEqual(score, 100,
                                 msg=f"GRADE key {score} should be between 0 to 100, got {score}")
            self.assertIsInstance(grade, str,
                                  msg=f"GRADE value {grade} should be {str}, got {type(grade)}")
            self.assertEqual(len(grade), 1, msg="grade should be a single letter")

    def test_part2(self):
        studentdata = read_testscores('testscores.csv')
        for record in studentdata:
            self.assertIsInstance(
                record["class"], str,
                msg=f"'class' key should have a str value, got {type(record['class'])} instead"
            )
            self.assertIsInstance(
                record["name"], str,
                msg=f"'name' key should have a str value, got {type(record['name'])} instead"
            )
            self.assertIsInstance(
                record["overall"], int,
                msg=f"'overall' key should have an int value, got {type(record['overall'])} instead"
            )
            self.assertIsInstance(
                record["grade"], str,
                msg=f"'grade' key should have a str value, got {type(record['grade'])} instead"
            )
            self.assertIn(
                record["grade"], 'ABCDESU',
                msg=f"'grade' key should be A, B, C, D, E, S, or U. Got {record['grade']} instead"
            )

    def test_part3(self):
        studentdata = read_testscores('testscores.csv')
        analysis = analyze_grades(studentdata)
        for class_, grade_count in analysis.items():
            for grade, count in grade_count.items():
                ans = len(list(filter(
                    lambda rec: rec["class"] == class_ and rec["grade"] == grade,
                    studentdata
                )))
                self.assertEqual(count, ans,
                                 msg=f"class {class_} count of grade {grade} should be {ans}, got {count} instead")


if __name__ == '__main__':
    import os
    if not os.listdir("autograding"):
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
    unittest.main()
