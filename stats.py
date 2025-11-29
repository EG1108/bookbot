def get_num_words(text):
    counter_arr = text.split()
    return len(counter_arr)

def get_characters(text):
    word_dict = {}
    for character in text:
        if character not in word_dict:
            word_dict[character] = 1
        else:
            word_dict[character] += 1
    return word_dict

def sort_nums(num):
    return num["num"]

def sort_dict(dict):
    sorted_list = []
    for character in dict:
        if character.isalpha():
            sorted_list.append({"char" : character, "num" : dict.get(character)})
    sorted_list.sort(reverse=True, key=sort_nums)
    return sorted_list

def format_dict(dict):
    for character in dict:
        print(f"{character.get("char")}: {character.get("num")}")
        
