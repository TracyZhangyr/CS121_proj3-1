from bs4 import BeautifulSoup
import nltk

class Document:
    def __init__(self, docID: int, url: str):
        self.docID = docID
        self.url = url
        self.num_of_cites = 0
        self.content = self.get_content_from_path(docID)
        
    
    def get_content_from_path(self, docID) -> ["string"]:
        list_of_string = []
        directory_path = self.change_to_directory_path(docID)
        try:
            with open(directory_path, 'rb') as file:
                soup = BeautifulSoup(file, 'html.parser')  #compute broken HTML by using BeautifulSoup
                self.find_number_of_citation(soup)   #find number of citation in HTML
                raw_string = soup.get_text()
                print (self.docID)
                list_of_string = raw_string.splitlines()
        except Exception as ex:
            print(ex.message)
        finally:
            if file is not None:
                file.close()
        return list_of_string
  
                
    def change_to_directory_path(self, docID: int) -> str:
        directory_path = "WEBPAGES_RAW\\" + docID.replace('/', '\\')
        return directory_path
    
    
    def find_number_of_citation(self, soup):
        cite_list = soup.find_all("cite")
        if (cite_list):
            self.num_of_cites = len(soup.find_all("cite"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    