# compiler.py

class Tripe_Director:
    def __init__(self, word_list):
        self.word_list = self.convert_word(word_list)
    
    """
    Convert HTTP Api word list to 'Token' instance list.
    """
    def convert_word(self, word_list):
        pass


class Tripe:
    """
    A Triple tuple contains 
    : token1, the subjective token
    : token2
    : relationship, token1-token2 relationship
    example:
        (Linus, Linux, father) is the meaning of "Linus is the father of Linux".
    """
    def __init__(self, token1, token2, relationship):
        pass

class Token:
    """
    Convert token to .
    :param token: is an element of word list.
    """
    def __init__(self, token):
        pass

    def __repr__(self):
        pass


