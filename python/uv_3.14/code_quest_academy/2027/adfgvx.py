import sys
from collections import defaultdict
from itertools import batched

ADFGVX_POS_MAP = {
    "A": 0,
    "D": 1,
    "F": 2,
    "G": 3,
    "V": 4,
    "X": 5,
}


def decrypt(substitution_grid, code_word, encrypted_message):
    unsorted_encrypted_message = unsort_encrypted_message(code_word, encrypted_message)
    cleartext_message = convert_to_cleartext(substitution_grid, unsorted_encrypted_message)
    return cleartext_message


def unsort_encrypted_message(code_word, encrypted_message):
    code_word_map = build_code_word_map(code_word)
    unsorted_encrypted_message = ""
    code_word_len = len(code_word)
    current_col = 0
    current_row = list(" " * code_word_len)
    for idx, c in enumerate(encrypted_message):
        from_index = code_word_map[current_col]
        while idx + from_index > len(encrypted_message):
            current_col += 1
            from_index = code_word_map[current_col]

        current_row[from_index] = c
        current_col += 1
        if current_col % code_word_len == 0:
            unsorted_encrypted_message += "".join(current_row)
            current_col = 0
            current_row = list(" " * code_word_len)

    return (unsorted_encrypted_message + "".join(current_row)).strip()


def build_code_word_map(code_word):
    code_word_sorted = sorted(code_word)
    return {code_word_sorted.index(c): idx for idx, c in enumerate(code_word)}


def convert_to_cleartext(substitution_grid, unsorted_encrypted_message):
    message = ""
    for batch in batched(unsorted_encrypted_message, 2):
        if len(batch) != 2:
            raise "Unexpected string"
        row, col = batch
        row_idx = ADFGVX_POS_MAP[row]
        col_idx = ADFGVX_POS_MAP[col]
        message += substitution_grid[row_idx][col_idx]
    return message


def main():
    """
    Problem 220: ADFGVX [Hard]
    https://lmcodequestacademy.com/problem/adfgvx
    run (assumes correct python installed and active, e.g. via the uv framework of the parent folder) via:
        python adfgvx.py < inputs/adfgvx.in
    :return:
    """

    def stdin_readline_as_array() -> list[str]:
        return list(sys.stdin.readline())[:-1]

    num_cases = int(sys.stdin.readline())
    for _ in range(num_cases):
        substitution_grid = []
        for _ in range(6):
            substitution_grid.append(stdin_readline_as_array())
        code_word = stdin_readline_as_array()
        encrypted_message = stdin_readline_as_array()
        print(f"{decrypt(substitution_grid, code_word, encrypted_message)}")


if __name__ == "__main__":
    main()
