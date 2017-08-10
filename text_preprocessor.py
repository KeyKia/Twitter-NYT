"""
Written by Benyamin Bashari
"""

import string
import collections
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords


class TextPreprocessor(object):

    stop = set(stopwords.words('english'))
    punctuation = set(string.punctuation)
    sno_stem = SnowballStemmer('english')

    """
    get a string as input
    returns a dictionary of (word :count) of that string
    """
    @staticmethod
    def preprocess(text, stem=True, punctuation=True, stopwords=True,  ret_lst=True):
        text = text.lower()
        if punctuation:
            text = TextPreprocessor.__remove_punctuation(text)
        text = TextPreprocessor.__remove_non_ascii(text)
        text = TextPreprocessor.__remove_digits(text)
        lst = word_tokenize(text, 'english')

        if stopwords:
            lst = TextPreprocessor.__remove_stopwords(lst)
        if stem:
            lst = TextPreprocessor.__stemmer(lst)
        if ret_lst:
            return lst
        return collections.Counter(lst)

    @staticmethod
    def __remove_punctuation(text):
        ret = ""
        for ch in text:
            if ch not in TextPreprocessor.punctuation:
                ret += ch
            else:
                ret += ' '
        return ret

    @staticmethod
    def __remove_non_ascii(text):
        ret = ''
        for ch in text:
            if 0 <= ord(ch) <= 127:
                ret += ch
        return ret

    @staticmethod
    def __remove_digits(text):
        ret = ''
        for ch in text:
            if not( ord('0') <= ord(ch) <= ord('9') ):
                ret += ch
        return ret

    @staticmethod
    def __remove_stopwords(lst):
        return filter(lambda x: x not in TextPreprocessor.stop, lst)


    @staticmethod
    def __stemmer(text_as_list):
        ret = []
        for word in text_as_list:
            ret.append(TextPreprocessor.sno_stem.stem(word))
        return ret







