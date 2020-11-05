import unittest
from utils import calculate


class TestCalculate(unittest.TestCase):

    def test_calculate_case_add(self):
        test_data = [
            {"op1": 1, "op2": 2, "operator": "+", "output": 3},
            {"op1": -7, "op2": 15, "operator": "+", "output": 8}
        ]

        for test_case in test_data:
            self.assertAlmostEqual(calculate(test_case["op1"], test_case["op2"],
                                             test_case["operator"]),
                                   test_case["output"])

    def test_calculate_case_subtract(self):
        test_data = [
            {"op1": 1, "op2": 2, "operator": "-", "output": -1},
            {"op1": -7, "op2": 15, "operator": "-", "output": -22}
        ]

        for test_case in test_data:
            self.assertAlmostEqual(calculate(test_case["op1"], test_case["op2"],
                                             test_case["operator"]),
                                   test_case["output"])

    def test_calculate_case_multiply(self):
        test_data = [
            {"op1": 1, "op2": 2, "operator": "*", "output": 2},
            {"op1": -7, "op2": 15, "operator": "*", "output": -105}
        ]

        for test_case in test_data:
            self.assertAlmostEqual(calculate(test_case["op1"], test_case["op2"],
                                             test_case["operator"]),
                                   test_case["output"])

    def test_calculate_case_divide(self):
        test_data = [
            {"op1": 5, "op2": 3, "operator": "/", "output": 1.66666666667},
            {"op1": -7, "op2": 15, "operator": "/", "output": -0.46666666666}
        ]

        for test_case in test_data:
            self.assertAlmostEqual(calculate(test_case["op1"], test_case["op2"],
                                             test_case["operator"]),
                                   test_case["output"])

    def test_calculate_operands(self):
        self.assertRaises(TypeError, calculate, '4', 5, '+')

    def test_calculate_case_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, calculate, 2, 0, '/')


if __name__ == '__main__':
    unittest.main(argv=['-v'], verbosity=2)
