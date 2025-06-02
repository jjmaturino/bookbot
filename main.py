from stats import get_word_count, get_char_count, get_char_list
from typing import  Union


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()

def print_report(book_path: str, word_count: int, char_list: list[dict[str, Union[str, int]]]) -> None:

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_list:
        char_val = char["char"]

        if not char_val.isalpha():
            continue

        char_instances = char["num"]

        print(f"{char_val}: {char_instances}")

    print("============= END ===============")

def main():
    book_path = "./books/frankenstein.txt"
    book_contents = get_book_text(book_path)

    num_of_words = get_word_count(book_contents)
    char_list = get_char_list(get_char_count(book_contents))



    print_report(book_path, num_of_words, char_list)





main()
