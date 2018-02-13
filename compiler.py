# compiler.py

postag_dict = {
    'Ag':'形语素',
    'g':'语素',
    'ns':'地名',
    'u':'助词',
    'a':'形容词',
    'h':'前接成分',
    'nt':'机构团体',
    'vg':'动语素',
    'ad':'副形词',
    'i':'成语',
    'nz':'其他专名',
    'v':'动词',
    'an':'名形词',
    'j':'简称略语',
    'o':'拟声词',
    'vd':'副动词',
    'b':'区别词',
    'k':'后接成分',
    'p':'介词',
    'vn':'名动词',
    'c':'连词',
    'l':'习用语',
    'q':'量词',
    'w':'标点符号',
    'dg':'副语素',
    'm':'数词',
    'r':'代词',
    'x':'非语素字',
    'd':'副词',
    'Ng':'名语素',
    's':'处所词',
    'y':'语气词',
    'e':'叹词',
    'n':'名词',
    'tg':'时语素',
    'z':'状态词',
    'f':'方位词',
    'nr':'人名',
    't':'时间词',
    'un':'未知词',}

class Triple_Director:
    def __init__(self, word_list):
        self.token_list = [Token(word, i) for i, word in enumerate(word_list)]   # base tokens
        self.graph_token_list = []  # composite tokens
        self.relation_list = []
        self.relations = []
    
    def graph(self):
        for i, token in enumerate(self.token_list):
            deprel_func = getattr(self, token.deprel, None)
            if deprel_func is None: raise CompilerDepError("No this deprel-function " + token.deprel)
            deprel_func(token, self.HEAD(token))
            
        self.generate_relations()
        print(self.relation_list)
        print(self.graph_token_list)
        print(self.relations)


    def generate_relations(self):
        for relation in self.relation_list:
            comp_token = self.find_token_by_id(relation[1])
            # not exist composite token with relation first element's token id.
            if comp_token is None:  
                find_id = [relation[1]]
            else:
                find_id = comp_token.ids
            
            for find_relation in self.relation_list:
                if find_relation[0] in find_id:
                    self.relations.append( Triple(relation[0], find_relation[1], relation[1]))
    
    def HEAD(self, token):
        if token.head == -1: return None
        return self.token_list[token.head]

    def find_token_by_id(self, id):
        for comp_token in self.graph_token_list:
            if comp_token.contain_id(id):
                return comp_token
        return None
    
    # bug, should also find token2.id
    def composite(self, token1, token2):
        comp_token, comp_token2 = self.find_token_by_id(token1.id), self.find_token_by_id(token2.id)
        if comp_token is None and comp_token2 is None:
            self.graph_token_list.append(CompositeToken(token1) + CompositeToken(token2))
        elif comp_token:
            comp_token.ids.append(token2.id)
            comp_token.tokens.append(token2)
        else:
            comp_token2.ids.append(token1.id)
            comp_token2.tokens.append(token1)
        return len(self.graph_token_list) - 1

    
    """
    ADJ： 附加关系
    """
    def ADJ(self, token1, token2):
        pass
    
    # 当token2是核心词汇时，应当联合所有的修饰词adv。
    def ADV(self, token1, token2):
        self.composite(token1, token2)

    """
    ATT:定中关系,应当合并为一个词语。
    :param token*: token1 -> token2,
                 and token2
    """
    def ATT(self, token1, token2):
        id = self.composite(token1, token2)
        return id
    
    """uncom
    APP: 同位关系，我们/大家，
    本句话建立的关系应当是相同的。
    """
    def APP(self, token1, token2):
        pass

    """
    COO: 并列关系,奔腾/咆哮，
    应当合并为一个词语
    """
    def COO(self, token1, token2):
        self.composite(token1, token2)
    
    
    """
    FOB:前置定语，Head方向变换。
    """
    def FOB(self, token1, token2):
        self.relation_list.append((token2.id, token1.id))

    def HED(self, token1, token2):
        pass

    """
    QUN: 数量关系，三天，三<-天
    """
    def QUN(self, token1, token2):
        self.composite(token1, token2)


    def SBV(self, token1, token2):
        self.relation_list.append((token1.id, token2.id))

    def WP(self, token1, token2):
        pass

class Triple:
    """
    A Triple tuple contains 
    : token1, the subjective token's id
    : token2
    : relationship, token1-token2 relationship
    example:
        (Linus, Linux, father) is the meaning of "Linus is the father of Linux".
    """
    def __init__(self, token1, token2, relationship):
        self.token1 = token1
        self.token2 = token2
        self.relationship = relationship

    def __repr__(self):
        return "(%s, %s, %s)" % (self.token1, self.token2, self.relationship)

class Token:
    """
    Convert token to .
    :param token: is an element of word list.
    """
    def __init__(self, token, id):
        self.postag = token['postag']
        self.head = token['head'] - 1   # if it is -1, it will be non-head word.
        self.content = token['word']
        self.deprel = token['deprel']
        self.id = id

    def __repr__(self):
        return postag_dict[self.postag] + '\t' + self.content

    def merge(self, token):
        self.content += token.content
        return self

class CompositeToken:
    def __init__(self, token, id=None):
        if isinstance(token, Token):
            self.tokens = [token]
            self.ids = [token.id]
        elif isinstance(token, list):
            self.tokens = token
            self.ids = id

    def contain_id(self, id):
        return True if id in self.ids else False
        
    def __add__(self, other):
        if isinstance(other, CompositeToken):
            return CompositeToken(self.tokens + other.tokens, self.ids + self.ids)

    def __repr__(self):
        from functools import reduce
        return reduce(lambda x, y: x+y.content, self.tokens, '')

class CompilerDepError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
