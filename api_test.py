import unittest

from api import *
class TestReader(unittest.TestCase):
    def test_wordEmbedding(self):
        self.assertEqual(get_wordEmbedding('张飞哈哈'), None)
        self.assertEqual(get_wordEmbedding('张飞').shape, (1024,))

    def test_lexer(self):
        print(get_lexer("我是你爸爸！"))

    def test_module(self):
        self.assertEqual(module(np.array([3, 4])), 5)
        
    def test_cos_similarity(self):
        print(get_wordSimilarity("big", "large"))   # 0.19
        print(get_wordSimilarity("字体", "宋体"))   # 0.22
        print(get_wordSimilarity("中国", "北京"))   #0.16
        print(get_wordSimilarity("父亲", "儿子"))   #0.40
        #self.assertTrue(get_wordSimilarity("big", "large") > 0.8)
        #self.assertTrue(get_wordSimilarity("字体", "宋体") > 0.7)
        #self.assertTrue(get_wordSimilarity("颜色", "绿色") > 0.6)


if __name__ == "__main__":
    unittest.main()