#!/usr/bin/python3
from aip import AipNlp

APP_ID = '10791703'
API_KEY = 'YNMY6eSAz6QlDCeM7KB9GKHC'
SECRET_KEY = 'tSqTt0OikFiYXVIt5kAXZyL0FdciRp5t'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def get_wordEmbedding(word):
    we = client.wordEmbedding(word)
    return we if 'vec' in we else None

def get_lexer(text):
    return client.lexer(text)