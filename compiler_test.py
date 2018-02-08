import api, compiler, unittest

class TestCompiler(unittest.TestCase):
    def test_Token(self):
        word_list = api.get_dependency('他什么书都读。')
        for word in word_list:
            token = compiler.Token(word)
            self.assertEqual(token.content, word['word'])

    def test_deprel_Funcs(self):
        word_list = api.get_dependency('他什么书都读。')
        td = compiler.Tripe_Director(word_list)
        print(td.graph())

if __name__ == "__main__":
    unittest.main()
