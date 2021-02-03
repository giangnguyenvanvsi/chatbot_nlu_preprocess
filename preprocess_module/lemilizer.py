# Lemmatize with POS Tag
import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet
import logging
logging.basicConfig(level=logging.DEBUG)


class Limelizer():
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        
    def __get_wordnet_pos(self, word):
        """Map POS tag to first character lemmatize() accepts"""
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        return tag_dict.get(tag, wordnet.NOUN)
    
    def correct(self, tokens):
        return [self.lemmatizer.lemmatize(w, self.__get_wordnet_pos(w)) for w in tokens]
        