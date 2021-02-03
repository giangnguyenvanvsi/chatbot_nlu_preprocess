import os
import csv
import logging
logging.basicConfig(level=logging.DEBUG)

my_path = os.path.abspath(os.path.dirname(__file__))
path_acronym_file__ = os.path.join(my_path, "acronym_/acronym_file.csv")




class AcronymModule():
    def __init__(self,
                path_acronym_file = None):
        
        self.name = "Acronym Module"
        
        if path_acronym_file != None and self.__check_valid_path(path_acronym_file):
            self.path_acronym_file = path_acronym_file
        else:
            self.path_acronym_file = path_acronym_file__
        
        self.dict_acronym_word = self.__load_dictionary()
        self.field_names = ['word', 'semantic']
        
                    
    def __check_valid_path(self, path_file):
        if not os.path.exists(path_file):
            logging.error("{} is not a file or directory.".format(path_file))
            return False
        else:
            return True
            
    
    def __load_dictionary(self):
        dict_acronym_word = {}
        with open(self.path_acronym_file, 'r') as data: 
            for line in csv.DictReader(data): 
                word = line['word']
                full_word = line['semantic']
                dict_acronym_word[word] = full_word
                # print(line) 
        return dict_acronym_word

    def __update_dictionary_file(self, acronym):
        # Open file in append mode
        
        # Open file in append mode
        with open(self.path_acronym_file, 'a+', newline='\n') as wf:
            # Create a writer object from csv module
            dict_writer = csv.DictWriter(wf, fieldnames=self.field_names)
            # Add dictionary as wor in the csv
            dict_writer.writerow(acronym)

    
    def insert_acronym(self, acronym):
        word = list(acronym.keys())[0]
        full_word = acronym[word]        
        acronym_dict = {'word':word, 'semantic':full_word}
        if word not in self.dict_acronym_word:
            logging.debug("Insert acronym to dictionary succesfully")
            self.__update_dictionary_file(acronym_dict)
            self.dict_acronym_word[word] = full_word
            return True
        else:
            logging.error("Insert acronym to dictionary not succesfully.\nNote: The acronym is exists in the dictionary")
            return False
                
    def convert(self, tokens):
        tokens_out = []
        for token in tokens:
            if token in self.dict_acronym_word:
                # full_word = self.dict_acronym_word[token]
                # words = full_word.split(' ')                
                # tokens_out += words
                tokens_out.append(self.dict_acronym_word[token])
            else:
                tokens_out.append(token)
        return tokens_out