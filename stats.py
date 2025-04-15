def get_num_words(text):
    wordsList = text.split()
    return len(wordsList)

def get_num_of_characters(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def sort_dictionary(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1],reverse=True))
    return sorted_dict
