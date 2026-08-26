import unittest
from custanalysis.SentimentAnalysis import text_to_analyze

class TestSentimentAnalysis(unittest.TestCase):
    def test_sentiment_analysis(self):
        # Test Case 1 - SENT_POSITIVE
        self.assertEqual(text_to_analyze('I love working with Python'), 'SENT_POSITIVE')
        
        # Test Case 2 - SENT_NEGATIVE
        self.assertEqual(text_to_analyze('I hate working with Python'), 'SENT_NEGATIVE')
        
        # Test Case 3 - SENT_NEUTRAL
        self.assertEqual(text_to_analyze('I am neutral on Python'), 'SENT_NEUTRAL')

unittest.main()