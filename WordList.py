from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def add_element(token:str, d:dict):
	if token not in STOPWORDS:
	    if d.get(token) == None:
	        d[token] = 1
	    else:
	        d[token] += 1


def count_words(content:list) -> dict:
    d = {}
    for line in content:
        
        start_pointer = 0
        end_pointer = 0
        for l in line:
            if l.isalnum():
                end_pointer += 1
                if end_pointer == len(line):
                    add_element(line[start_pointer:].lower(), d)
            else:
                if end_pointer - start_pointer == 0:
                    end_pointer += 1
                    start_pointer = end_pointer
                else:
                    token = line[start_pointer:end_pointer].lower()
                    add_element(token, d)
                    end_pointer += 1
                    start_pointer = end_pointer
    return d
