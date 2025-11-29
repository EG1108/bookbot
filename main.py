from stats import get_num_words
from stats import get_characters
from stats import sort_dict
from stats import format_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    def get_book_text(filepath):
        with open(filepath) as file:
            return file.read()
        
    book_text = get_book_text(sys.argv[1])

    num_of_words = get_num_words(book_text)
    print(f"Found {num_of_words} total words")
    characters = get_characters(book_text.lower())
    format_dict(sort_dict(characters))
main()