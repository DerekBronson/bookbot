from stats import *
import string
import sys

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])    
    
    num_words = get_num_words(text)
    #create a dictionary of all the characters
    character_count = get_num_of_characters(text)  
    #sort the dictionary
    sorted_character_dict = sort_dictionary(character_count)
    
    #start printing stuff
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_character_dict:
        if c.isalpha:
            print(f"{c}: {sorted_character_dict[c]}")
    print("============= END ===============")


main()

