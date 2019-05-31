from nltk.corpus import stopwords
from main import load_dict
import math

STOPWORDS = set(stopwords.words('english'))

class Cosine_computation:
    def __init__(self, query_list:[], word_list: dict):
        self.query_list = self.eliminate_stop_words(query_list)
        self.word_dict = load_dict("WordList.txt")
        
    def cosine_scores(self):
        for query in self.query_list:
             if query in word_dict.keys():
                 pass
    
    def eliminate_stop_words(self, query_list):
        new_list = []
        for query in query_list:
            if (query not in STOPWORDS):
                new_list.append(query)
        return new_list
    
    def compute_query_frequency(self, input_query: str):
        frequency = 0
        for query in self.query_list:
            if query == input_query:
                frequency += 1
        return (1 + math.log10(frequency))