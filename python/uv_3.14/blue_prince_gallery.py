from itertools import product

with open("/usr/share/dict/words", "r") as f:
    english_words = {line.strip().lower() for line in f}

APPLE_WAGON_LETTERS = [
    ['c', 'p', 't', 'l', 's', 'm', 'w', 'b'],
    ['a', 'e', 'i', 'o', 'u', 'h', 'r', 't'],
    ['v', 'l', 'r', 'n', 't', 's', 'o', 'i'],
    ['d', 't', 'h', 's', 'i', 'k', 'v', 'a'],
    ['a', 'e', 'o', 'n', 'l', 'r', 'c', 's'],
    ['n', 'd', 'g', 'r', 'w', 't', 'e', 'y'],
]


def print_valid_words(letters):
    candidates_generator = ("".join(chars) for chars in product(*APPLE_WAGON_LETTERS))
    for candidate in candidates_generator:
        if is_valid_word(candidate):
            print(candidate)


def is_valid_word(str):
    return str.strip().lower() in english_words


def main():
    print_valid_words(APPLE_WAGON_LETTERS)


if __name__ == "__main__":
    main()
