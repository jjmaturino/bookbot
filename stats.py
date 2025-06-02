from collections import defaultdict
from typing import Union

def get_words(content: str) -> list[str]:
    return content.split()

def get_word_count(content: str) -> int:
    return len(get_words(content))

def get_whitespace_count(content_length: int, number_of_words: int) -> int:
    return content_length - number_of_words

def get_char_count(content: str) -> dict[str, int]:
    res = defaultdict(int)

    words = get_words(content)

    for word in words:
        for char in word:
            lower_char = char.lower()

            res[lower_char] += 1
        
    
    whitespace_count = get_whitespace_count(len(content), get_word_count(content))

    res[" "] = whitespace_count


    return res

def get_char_list(char_dict: dict[str, int]) -> list[dict[str, Union[str, int]]]:
    res = []

    def new_dict(char_val: str, instances: int):
        return {"char": char_val, "num": instances}

    for char, val in char_dict.items():
        res.append(new_dict(char, val))

    def sort_on(dict):
        return dict["num"]

    res.sort(reverse=True, key=lambda x: x["num"])

    return res

