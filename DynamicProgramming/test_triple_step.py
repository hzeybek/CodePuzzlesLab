import unittest

from triple_step import TripleStep

class TripleStepTest(unittest.TestCase):
    def setUp(self):
        self.triple_step = TripleStep()

    def test_solution(self):
        # Test cases where n <= 2
        self.assertEqual(self.triple_step.solution(1), 1)
        self.assertEqual(self.triple_step.solution(2), 2)
        self.assertEqual(self.triple_step.solution(3), 3)

        # Test cases where n > 2
        self.assertEqual(self.triple_step.solution(4), 6)
        self.assertEqual(self.triple_step.solution(5), 11)
        self.assertEqual(self.triple_step.solution(6), 20)
        self.assertEqual(self.triple_step.solution(7), 37)
        self.assertEqual(self.triple_step.solution(8), 68)
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()



