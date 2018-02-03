import unittest

from api import *
class TestReader(unittest.TestCase):
    def test_wordEmbedding(self):
        self.assertEqual(get_wordEmbedding('张飞哈哈'), None)
        self.assertEqual('vec' in get_wordEmbedding('张飞'), True)

    def test_lexer(self):
        print(get_lexer("我是你爸爸！"))

if __name__ == "__main__":
    unittest.main()