def add_element(token:str, d:dict):
    if d.get(token) == None:
        d[token] = 1
    else:
        d[token] += 1


def count_words(content:list[str]): -> dict
    d = {}
    for line in content:
        
        start_pointer = 0
        end_pointer = 0
        for l in my_str:
            if l.isalnum():
                end_pointer += 1
                if end_pointer == len(my_str):
                    add_element(my_str[start_pointer:].lower(), d)
            else:
                if end_pointer - start_pointer == 0:
                    end_pointer += 1
                    start_pointer = end_pointer
                else:
                    token = my_str[start_pointer:end_pointer].lower()
                    add_element(token, d)
                    end_pointer += 1
                    start_pointer = end_pointer
    return d