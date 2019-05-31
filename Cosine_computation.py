from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

class Cosine_computation:
    def __init__(self, query_list, word_list: dict):
        self.query_list = self.eliminate_stop_words(query_list)
        self.word_dict = word_list
        
    def cosine_scores():
        for query in query_list:
            pass 
    
    def eliminate_stop_words(self, query_list):
        new_list = []
        for query in query_list:
            if (query not in STOPWORDS):
                new_list.append(query)
        return new_list