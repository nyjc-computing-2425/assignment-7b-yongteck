import unittest

class TestRun:
    def __init__(self,
                 testcase: unittest.TestCase,
                 ans: Any,
                 func: Callable,
                 call_args: Tuple[Any] = tuple()) -> None:
        self.testcase = testcase
        self.func = func
        self.call_args = call_args
        self.ans = ans
        self.result = func(*call_args)
    
    def callstr(self) -> str:
        return (
            f"{self.func.__name__}"
            f"({', '.join(repr(self.call_args) for arg in self.call_args)})"
        )
    
    def test(self) -> None:
        callstr = self.callstr()
        if self.ans is not None:
            self.testcase.assertIsNotNone(
                self.result,
                msg=f"{callstr} returned None"
            )
        self.testcase.assertIsInstance(
            self.result, type(self.ans),
            msg=f"{callstr} returned {type(self.result)}, expected {type(self.ans)}"
        )
        self.testcase.assertEqual(
            self.result, self.ans,
            msg=f"{callstr}: Got {self.result!r}, expected {self.ans!r}"
        )
        # Check docstring
        self.testcase.assertTrue(hasattr(self.func, "__doc__"), msg=f"{callstr} has no docstring")
        self.testcase.assertTrue(self.func.__doc__, msg=f"{callstr} has no docstring")


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
    unittest.main()
