import unittest
import sys

from reader import *
class TestReader(unittest.TestCase):
    def test_zhidao_train(self):
        reader = zhidao_train_reader()
        #print(next(reader))

    def test_lexer_docs(self):
        reader = zhidao_train_reader()
        sys.stdout.write(str(next(reader)))        

if __name__ == "__main__":
    unittest.main()