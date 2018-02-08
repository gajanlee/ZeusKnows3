import unittest

from api import *
class TestReader(unittest.TestCase):
    def test_wordEmbedding(self):
        self.assertEqual(get_wordEmbedding('张飞哈哈'), None)
        self.assertEqual(get_wordEmbedding('张飞').shape, (1024,))

    def test_lexer(self):
        self.assertEqual(len(get_lexer("我是你爸爸!")['items']), 5)

    def test_module(self):
        self.assertEqual(module(np.array([3, 4])), 5)
        self.assertRaises(AssertionError, module, np.array([[1, 2, 3], [4, 5, 6]])) # Warning: module is callable...
        
    def test_cos_similarity(self):
        self.assertTrue(get_wordSimilarity("字体", "宋体") > 0)   # 0.22
        self.assertTrue(get_wordSimilarity("父亲", "儿子") > 0)   #0.40
    
    def test_dependency(self):
        #print(get_dependency('票面：发票。文字：宋体、黑体。发票号码：采用异型(采用哥特字体)字体印刷，号码为8位，位于发票的右上角。发票编码：发票编码为10位阿拉伯数字。'))
        word_list = get_dependency('他什么书都读。')

if __name__ == "__main__":
    unittest.main()




def proper_analy(token, word_list):
    """
    It should be callable recursively.
    :param token: dependency token
    """
    if token["deprel"] == "SBV":
        return (token, SBV(word_list[token['head']]))
