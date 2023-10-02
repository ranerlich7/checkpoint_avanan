import unittest
import time
from app import count_word, get_words, count_and_update, get_events, words  # Replace with your actual file name

class TestApp(unittest.TestCase):

    def test_count_word(self):
        test_cases = [
            ([(995, 2), (999, 1), (1000, 1)], 997, 2),  # Expected: 1 + 1 = 2
            ([(990, 2), (995, 1), (1000, 1)], 990, 4),  # Expected: 2 + 1 + 1 = 4
            ([(900, 2), (930, 1), (940, 1)], 990, 0),  # Expected: 0
        ]

        for word_arr, interval, expected in test_cases:
            with self.subTest(word_arr=word_arr, interval=interval, expected=expected):
                self.assertEqual(count_word(word_arr, interval), expected)


    def test_get_words(self):
        words['email'] = [(1, 2), (3, 1), (5, 1)]
        interval = 2
        expected_data = {
            'email': 2,  # 1 + 1 + 1 = 3
            'checkpoint': 0,
            'avanan': 0,
            'security': 0
        }
        self.assertEqual(get_words(interval), expected_data)

    def test_count_and_update(self):
        sentence = "email is email"
        phrase = "email"
        now_time = int(time.time())
        count_and_update(sentence, phrase, now_time)
        self.assertEqual(words['email'][-1], (now_time, 2))  # 'email' occurs 2 times in the sentence

    def test_get_events(self):
        sentence = "email is email"
        current_time = int(time.time())
        get_events(sentence, current_time)
        self.assertEqual(words['email'][-1], (current_time, 2))  # 'email' occurs 2 times in the sentence
        self.assertEqual(words['checkpoint'], [])  # 'checkpoint' occurs 0 times in the sentence
        self.assertEqual(words['avanan'], [])  # 'avanan' occurs 0 times in the sentence
        self.assertEqual(words['security'], [])  # 'security' occurs 0 times in the sentence


if __name__ == '__main__':
    unittest.main()
