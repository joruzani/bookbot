def get_num_words(text):
    words = text.split()
    #for i in range(0,10,1):
    #    print(words[i])
    return len(words)

def get_num_chars(text):
    lower = text.lower()
    char_dic = {
        'a' : 0,
        'b' : 0,
        'c' : 0,
        'd' : 0,
        'e' : 0,
        'f' : 0,
        'g' : 0,
        'h' : 0,
        'i' : 0,
        'j' : 0,
        'k' : 0,
        'l' : 0,
        'm' : 0,
        'n' : 0,
        'o' : 0,
        'p' : 0,
        'q' : 0,
        'r' : 0,
        's' : 0,
        't' : 0,
        'u' : 0,
        'v' : 0,
        'w' : 0,
        'x' : 0,
        'y' : 0,
        'z' : 0,
    }
    for c in lower:
        if c in char_dic:
            char_dic[c] += 1
    return char_dic

def sort_on(dic):
    return dic["num"]


def sort_char_count(dic):
    dict_list = []
    for c, n in dic.items():
        dict_list.append({"char": c, "num": n})
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

