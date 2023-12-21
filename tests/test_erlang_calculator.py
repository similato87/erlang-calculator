import unittest

from src.erlang_calculator import erlangB, erlangC


class TestErlangFunctions(unittest.TestCase):

    def test_erlangB(self):
        # Test cases for erlangB function
        # Format: (A, N, expected_result)
        test_cases = [
            (10, 5, 0.56395),
            (20, 10, 0.53796),
            # Add more test cases as needed
        ]

        for A, N, expected in test_cases:
            with self.subTest(A=A, N=N):
                result = float(erlangB(A, N))
                self.assertAlmostEqual(result, expected, places=5)

    def test_erlangC(self):
        # Test cases for erlangC function
        # Format: (A, N, expected_result)
        test_cases = [
            (10, 5, 8.81834),
            (20, 10, 14.17066),
            # Add more test cases as needed
        ]

        for A, N, expected in test_cases:
            with self.subTest(A=A, N=N):
                result = float(erlangC(A, N))
                self.assertAlmostEqual(result, expected, places=5)

if __name__ == '__main__':
    unittest.main()
