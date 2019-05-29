from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def add_element(token:str, line_num:int, d:dict):
	if token not in STOPWORDS:
	    if d.get(token) == None:
	        d[token] = [1, {line_num}]
	    else:
	        d[token][0] += 1
	        d[token][1].add(line_num)

                
def count_words(content:list) -> dict: #Dict{str:[int, set{int}]}
    d = {}
    line_num = 0
    for line in content:
        line_num += 1
        start_pointer = 0
        end_pointer = 0
        for l in line:
            if l.isalnum():
                end_pointer += 1
                if end_pointer == len(line):
                    add_element(line[start_pointer:].lower(), line_num, d)
            else:
                if end_pointer - start_pointer == 0:
                    end_pointer += 1
                    start_pointer = end_pointer
                else:
                    token = line[start_pointer:end_pointer].lower()
                    add_element(token, line_num, d)
                    end_pointer += 1
                    start_pointer = end_pointer
    return d

def common_line_num(l:list) -> int: #l is the list of sets of line numbers, returns the max count of common line numbers
    d = {}
    searched_set = set()
    result = 0

    for s in l:
        for line_num in s:
            if line_num not in searched_set:
                searched_set.add(line_num)
                max_lines = 0
                for line_num_set in l:
                    if line_num in line_num_set:
                        max_lines += 1
                if max_lines >= result:
                    result = max_lines
    return result
            


