from stats import get_num_words
from stats import get_num_chars
from stats import sort_char_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(path)
    #print(book)
    num_words = get_num_words(book)
    num_chars = get_num_chars(book)
    char_stats = sort_char_count(num_chars)
    print(f"============ BOOKBOT ============\n Analyzing book found at {path}...")
    print(f"----------- Word Count ----------\n Found {num_words} total words")
    print("--------- Character Count -------")
    for i in char_stats:
        print(f"{i['char']}: {i['num']}")
    sys.exit(0)

main()