import unittest

from src.high_scores import latest, personal_best, personal_top_three, highest_to_lowest

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [5, 7, 12, 45, 100, 15, 52, 23]
        self.scores_tie = [5, 7, 12, 45, 100, 100, 52, 23]
        self.short_list = [3, 5]

    # Tests

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        last = latest(self.scores)
        self.assertEqual(23, last)

    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        best = personal_best(self.scores)
        self.assertEqual(100, best)

    # Test top three from list of scores
    def test_top_thee(self):
        top = personal_top_three(self.scores)
        self.assertEqual([100, 52, 45], top)

    # Test ordered from highest tp lowest
    def test_highest_to_lowest(self):
        h_to_l = highest_to_lowest(self.scores)
        self.assertEqual(100, self.scores[0])

    # Test top three when there is a tie
    def test_top_three_is_tie(self):
        top3 = personal_top_three(self.scores_tie)[0:3]
        self.assertEqual([100, 100, 52], top3)

    # Test top three when there are less than three
    def less_than_three(self):
        self.assertEqual([5, 3], highest_to_lowest(self.short_list))

    # Test top three when there is only one
