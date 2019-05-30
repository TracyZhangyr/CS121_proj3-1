from Document import Document
import WordList
from collections import defaultdict
import json

def get_list_of_document(document_path)->list:
    list_of_Document = []
    d = load_dict(document_path)
    for k, v in d.items():
        list_of_Document.append(Document(k, v))
    return list_of_Document


def indexing(index_dict:dict,doc_list:["Document"])->None:
    total_doc_num = len(doc_list)
    for doc in doc_list:
        WordList.update_index_dict(index_dict,doc)
    WordList.calculate_tfidf(index_dict,total_doc_num)

def write_dict(d:dict, file_name:str)->None:
	js = json.dumps(d)   
	file = open(file_name, 'w+')  
	file.write(js)  
	file.close()

def load_dict(file_name:str)->dict:
	file = open(file_name, 'r') 
	js = file.read()
	d = json.loads(js)    
	file.close() 
	return d


if __name__ == "__main__":
	new_list = get_list_of_document("WEBPAGES_RAW\\bookkeeping.json")
	
	#dict{"word":{"docID":{"tf-idf":float,"line_num":[int],"cite":int}}}
	index_dict = defaultdict(dict)
	indexing(index_dict,new_list)
	write_dict(index_dict, "WordList.txt")
	d = load_dict("WordList.txt")