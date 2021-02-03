from itertools import islice
import pkg_resources
from symspellpy import SymSpell
import os

import logging
logging.basicConfig(level=logging.DEBUG)



class SegmentText():
    def __init__(self, 
                 dictionary_path = None, 
                 bigram_path = None):
        
        self.name = "SegmenText"
        self.sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
        # dictionary_path = pkg_resources.resource_filename(
        #     "symspellpy", "frequency_dictionary_en_82_765.txt")
        if dictionary_path != None:
            self.dictionary_path = dictionary_path
        else:
            self.dictionary_path = os.path.join("./symspellfre_", "frequency_dictionary_en_82_765.txt")
    
        if bigram_path != None:
            self.bigram_path = bigram_path
        else:
            self.bigram_path = os.path.join("./symspellfre_", "frequency_bigramdictionary_en_243_342.txt")
            # self.bigram_path = pkg_resources.resource_filename("symspellpy", "frequency_bigramdictionary_en_243_342.txt")
        self.sym_spell.load_dictionary(self.dictionary_path, term_index=0, count_index=1)
        self.sym_spell.load_bigram_dictionary(self.bigram_path, term_index=0, count_index=2)

    
    def split(self, sentence):
        # lookup suggestions for multi-word input strings (supports compound
        # splitting & merging)
        # input_term = ("in te dhird qarter oflast jear he hadlearned ofca sekretplan")
        # input_term = ("in te dhird qarter oflast jear he hadlearned ofca sekretplan eoy")
        # max edit distance per lookup (per single word, not per whole input string)
        suggestions = self.sym_spell.lookup_compound(sentence, max_edit_distance=2)
        # display suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
            print(suggestion)
        return suggestions