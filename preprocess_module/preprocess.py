import csv
import os

from .acronym import AcronymModule
from .lemilizer import Limelizer
from .tokenizer import Tokenizer
from .spellCorrect import SpellCorrect
# from .segmentText import SegmentText
import re

my_path = os.path.abspath(os.path.dirname(__file__))
path_dict_zip__ = os.path.join(my_path, "wordninja_/dict_update_2021_00.txt.gz")
    
    
class PreProcessModule():
    def __init__(self, 
                path_dict_zip_ = path_dict_zip__,
                path_acronym_file = None):
        self.name = "Preprocess Module"
        self.corrector = SpellCorrect()
        self.tokenizer = Tokenizer(path_dict_zip=path_dict_zip_)
        self.limelizer = Limelizer()
        self.acronymer = AcronymModule(path_acronym_file=path_acronym_file)
        
        
    def rebuild_tokenizer(self):
        self.tokenizer = Tokenizer(path_dict_zip=None)    
        
    def correct_sentence(self, sentence):
        return self.corrector.correct(sentence)

    def process(self, sentence, mode='acronym'):        
        sentence = sentence.lower()
        if mode == 'acronym':
            tokens = self.tokenizer.split(sentence)
            tokens = self.limelizer.correct(tokens)
            tokens = self.acronymer.convert(tokens)
        else:
            sentence = re.sub(r"[^a-zA-Z0-9 ]","",sentence)
            
            #             tokens_ = tokenizer.simple_tokenizer(sentence)
            #             tokens = []
            #             for word in tokens_:
            #                 tokens.append(self.corrector(word))
            
            new_sentence = self.corrector.correct(sentence)
            tokens = self.tokenizer.simple_tokenizer(new_sentence)            
            tokens = self.limelizer.correct(tokens)
        return tokens
    
    
    def update_acronym_words(self, acronym):
        # add a acronym word in dictionary
        
        for key in acronym.keys():
            acronym_word = key
            # acronym_detail = acronym[acronym_word]
            if self.acronymer.insert_acronym(acronym):
                path_dict_zip = self.tokenizer.update_dictionary([acronym_word])
                self.tokenizer.update_spliter(path_dict_zip)
                
     # Preprocess Function
    def process_sent(self, sentence, print_stt=False):
        tokens = self.process(sentence)
        output = " ".join(word for word in tokens)
        output_2 = self.correct_sentence(output)
        if output != output_2:
            tokens = self.process(sentence, mode = 'non_acronym')
            output = " ".join(word for word in tokens)
        if print_stt:
            print("Input: {}\nOutput: {}\n---------------------\n".format(sentence, output))
        return output  
