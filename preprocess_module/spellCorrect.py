import os
import pkg_resources
from symspellpy import SymSpell
# from symspellpy import SymSpell, Verbosity
import logging
logging.basicConfig(level=logging.DEBUG)
dictionary_path__ = pkg_resources.resource_filename(
                    "symspellpy", "frequency_dictionary_en_82_765.txt")
bigram_path__ = pkg_resources.resource_filename(
                    "symspellpy", "frequency_bigramdictionary_en_243_342.txt")


class SpellCorrect():
    def __init__(self, 
                dictionary_path = dictionary_path__, 
                bigram_path = bigram_path__):
        
        self.sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)     
        if self.is_valid_path(dictionary_path) and self.is_valid_path(bigram_path):
            self.sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
            self.sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)
            self.load_status = True
        else:
            self.load_status = False    
        self.name = "Spell Corrector"
        
    
    def is_valid_path(self, path_file):
        if not os.path.exists(path_file):
            logging.error("The {} is not exists".format(path_file))
            return False
        return True
        
    def correct(self, sentence):
        if self.load_status:
            # max edit distance per lookup (per single word, not per whole input string)
            suggestions = self.sym_spell.lookup_compound(sentence, max_edit_distance=2)
            # display suggestion term, edit distance, and term frequency
            for suggestion in suggestions:
                return suggestion.term
        return self.load_status