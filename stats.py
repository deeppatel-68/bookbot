def get_num_words(file_contents):
    string_list = file_contents.split()
    return len(string_list) 

def num_characters(file_contents):
    lower_words = file_contents.lower()
    char_dict = {}


    for c in lower_words:
        if c in char_dict:
            char_dict[c] = char_dict[c] + 1 
        else:
            char_dict[c] = 1
    return char_dict



def list(char_dict):
    sorted_chars = []

    for c in char_dict:
        if c.isalpha():
            sorted_chars.append({"char" : c, "num" : char_dict[c]})
    return sorted_chars


def sort_on(sorted_chars):
    return sorted_chars["num"]
