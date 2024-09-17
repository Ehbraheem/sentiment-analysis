import unittest
from sentiment_analyzer import analyze

class TestSentimentAnalyzer(unittest.TestCase):
    def test_analyze(self):
        result = analyze('I love working with Python')
        self.assertEqual(result['label'], 'SENT_POSITIVE')

        result = analyze('I hate working with Python')
        self.assertEqual(result['label'], 'SENT_NEGATIVE')

        result = analyze('I am neutral on Python')
        self.assertEqual(result['label'], 'SENT_NEUTRAL')


if __name__ == '__main__':
    unittest.main()
