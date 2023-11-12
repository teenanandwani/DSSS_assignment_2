import unittest
from math_quiz import generate_random_int, generate_random_operator, perform_operation


class TestMathGame(unittest.TestCase):

    def test_generate_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the random operator generated is from the specified list [-,+,*]
        corr_operator = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            operator = generate_random_operator()
            self.assertIn(operator, corr_operator)
        pass

    def test_perform_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (9, 4, '*' , '9 * 4', 36),
                (10, 6, '-', '10 - 6', 4),
                (7, 1, '+', '7 + 1', 8),
                (3, 8, '*' , '3 * 8', 24),
                (10, 1, '-', '10 - 1', 9),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = perform_operation(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
            pass

if __name__ == "__main__":
    unittest.main()


