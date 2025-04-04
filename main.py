from stats import *
import string

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(text)
    #create a dictionary of all the characters
    character_count = get_num_of_characters(text)  
    #sort the dictionary
    sorted_character_dict = sort_dictionary(character_count)
    
    #start printing stuff
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_character_dict:
        if c.isalpha:
            print(c)
    print("============= END ===============")


main()

