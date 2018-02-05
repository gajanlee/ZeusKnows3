#!/usr/bin/python3
from aip import AipNlp
import numpy as np

APP_ID = '10791703'
API_KEY = 'YNMY6eSAz6QlDCeM7KB9GKHC'
SECRET_KEY = 'tSqTt0OikFiYXVIt5kAXZyL0FdciRp5t'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def get_wordEmbedding(word):
    we = client.wordEmbedding(word)
    return np.array(we['vec']) if 'vec' in we else None

def module(vec):
    assert len(vec.shape) == 1, "Can't module with more than one dimension"
    from functools import reduce
    import math
    return math.sqrt( reduce(lambda x, y: x+math.pow(y, 2), vec, 0))

def get_wordSimilarity(word1, word2):
    w1, w2 = get_wordEmbedding(word1), get_wordEmbedding(word2)
    if w1 is None or w2 is None: return None
    return float(np.dot(w1, w2)) / (module(w1) * module(w2))
    
def get_lexer(text):
    return client.lexer(text)

def get_dependency(text):
    """
    :param text: prepare to analysis the dependecy of tokens
    :return word_list: a list which id is the subscript and the content is a dict with word's information
    
    options represent:
        mode 0: web model, for written text, default
        mode 1: query model, for colloquial language
    """
    # later, we need cut long sentence into multiply short sentences.
    # dependency doesn't consider about ':'.
    text = text.replace('：', '为')
    word_list = []
    for i, word in enumerate(client.depParser(text, options={"mode": 0})["items"], 1):
        print(i, word)
        word_list.append(word)              # id will increase 1
    graph(word_list)
    return word_list

def graph(word_list):
    pass