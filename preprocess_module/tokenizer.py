import wordninja
from datetime import datetime, date
import gzip
import logging
logging.basicConfig(level=logging.DEBUG)
import os
import nltk
# nltk.download("all")
from nltk.tokenize import word_tokenize 

my_path = os.path.abspath(os.path.dirname(__file__))
path_dict_zip__ = os.path.join(my_path, "wordninja_/dict_update_2021_00.txt.gz")

path_dict_zip_default__ = os.path.join(my_path, "wordninja_/wordninja_words.txt.gz")


class Tokenizer():
    def __init__(self,
                path_dict_zip = path_dict_zip__):
        self.name_class = 'TOKENIZER'
        self.status_update = False
        if path_dict_zip != None and self.__check_valid_path(path_dict_zip):            
            self.path_dict_zip = path_dict_zip
            logging.debug("The module load input dictionary succesfully")
        else:
            self.path_dict_zip = path_dict_zip_default__# note            
            logging.debug("If you don't change the input path_dict_zip, the module will use the default spliter")
        
        # print(os.path.join(os.path.abspath, self.path_dict_zip))
        self.spliter = wordninja.LanguageModel(self.path_dict_zip)
            
    
    def simple_tokenizer(self, sentence):
        #return sentence.split(' ')        
        return word_tokenize(sentence)
        
            
    def __check_valid_path(self, path_file):
        if not os.path.exists(path_file):
            logging.error("{} is not a file or directory.".format(path_file))
            return False
        else:
            return True
            
        
    def split(self, sentence):
        return self.spliter.split(sentence)
        
    def update_dictionary(self,
                          words):
        
        # get date time information
        today = date.today()
        now = datetime.now()
        day = today.strftime("%Y_%M")
        # curr = now.strftime("%H_%M")
        path_dict_zip_old = self.path_dict_zip
        self.path_dict_zip = path_dict_zip__
        
        # insert new word in gzip file
        with gzip.open(self.path_dict_zip, "at") as wf:
            for word in words:
                wf.write(word+'\n')
            
            with gzip.open(path_dict_zip_old, 'rb') as rf2:
                lines2 = rf2.readlines()
                for line2 in lines2:
                    line2 = line2.decode("utf-8")                     
                    wf.write(line2)                    
        return self.path_dict_zip            
    
    
    def update_spliter(self, path_dict_zip):
        self.spliter = wordninja.LanguageModel(self.path_dict_zip)
