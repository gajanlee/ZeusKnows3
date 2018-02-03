# Write all reader as interface.
# TODO: be a base class.

import json
from api import *
from bs4 import BeautifulSoup

BASE_PATH = '/home/lee/Workspace/pyproj/ZeusKnow/raw/'
TRAIN_PATH = BASE_PATH + 'trainset/zhidao.train.json'


def zhidao_train_reader():
    """
    It requires a zhidao train data iterator.
    """
    def process_data(data):
        if data['question_type'] == 'ENTITY':
            return know_graph(''.join(data['documents'][0]['paragraphs']))
        return ''

    def reader():
        with open(TRAIN_PATH) as f:
            for i, l in enumerate(f):
                if i == 147:
                    yield process_data(json.loads(l))               
    return reader()


def know_graph(text):
    """
    generate a list of triple tuple as knowledge graph
    answer entity questions

    :param text: a paragraph text.
    :return : a list
    """
    text = clean_text(text) 
    #print(text)
    tokens = get_lexer(text)
    print(tokens)
    for item in tokens['items']:
        if item['pos'] in ['c', 'u', 'xc', 'w']:
            continue
        
    return tokens

def clean_text(text):
    return BeautifulSoup(text, 'html.parser').text