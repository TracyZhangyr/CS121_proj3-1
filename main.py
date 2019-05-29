from Document import Document

def get_list_of_document(document_path):
    list_of_Document = []
    with open(document_path) as json_file:
        for line in json_file:
            if not (line[0] == "{" or line[0] == "}"):
                new_list = line.replace('"', " ").replace(':', " ").rstrip().split()
                docID = new_list[0]
                url = new_list[1]
                list_of_Document.append(Document(docID, url))
    return list_of_Document



new_list = get_list_of_document("WEBPAGES_RAW\\bookkeeping.json")