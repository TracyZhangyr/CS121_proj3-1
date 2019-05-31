from Document import Document
import WordList
from collections import defaultdict
import json
from builtins import input
import Cosine_computation

def get_list_of_document(document_path: str)->list:
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

#return ["url","description"]
def get_url_and_descrip(docID:str)->["url","descrip"]:
    result = []
    path = "WEBPAGES_RAW\\" + docID.replace('/', '\\')
    doc_dict = load_dict(path)
    url = doc_dict[docID]
    result.append(url)
    doc = Document(docID,url)
    descrip = ""
    for line in doc.content:
        if len(descrip) < 100:
            descrip += line
        else:
            break
    result.append(descrip)
    return result
            
def generate_top_urls(docIDs:["docID"])->[["url","descrip"]]:
    return [get_url_and_descrip(docID) for docID in docIDs]  

def write_report_part_2(file_name:str,result:[("query",["docID"])]):
    output = open(file_name,'w+')
    for pair in result:
        query = pair[0]
        docID_list = pair[1]
        print("Query: {}".format(query),file=output)
        print("Number of URLs retrieved: {}".format(len(docID_list)),file=output)
        print("Top 20 URLs:",file=output)
        if(len(docID_list) >= 20):
            for docID in docID_list[:20]:
                url = get_url_and_descrip(docID)[0]
                print(url,file=output)
        print("\n",file=output)
    output.close()

#Need to complete      
def generate_report_part_2(file_name:str):
    report_query_list = ["Informatics","Mondego","Irvine",
                         "artificial intelligence","computer science"]
    result = []
    for query in report_query_list:
        pass    
    write_report_part_2(file_name, result)


def get_user_query(query:str) -> list:
    user_input = query
    query_list = user_input.rstrip().split()
    return query_list


if __name__ == "__main__":
    new_list = get_list_of_document("WEBPAGES_RAW\\bookkeeping.json")
    #dict{"word":{"docID":{"tf-idf":float,"line_num":[int],"cite":int}}}
    index_dict = defaultdict(dict)
    indexing(index_dict,new_list)
    write_dict(index_dict, "WordList.txt")
    #d = load_dict("WordList.txt")
    #print(len(d.keys()))
    query_list = get_user_query()
    computation = Cosine_computation(query_list)
    rank_list = computation.ranking()
    '''
    #Use for test before the GUI done 
    input_query = str(input("Please type your query: "))
    query_list = get_user_query(input_query)

    #Create report.pdf part 2 only (not finished)
    generate_report_part_2("Report_Part_2.txt")
    '''
    

    
    
