import sys

ADFGVX_POS_MAP = {
    "A": 0,
    "D": 1,
    "F": 2,
    "G": 3,
    "V": 4,
    "X": 5,
}


def decrypt(substitution_grid, code_word, encrypted_message):
    code_word_len = len(code_word)
    code_word_sorted = sorted(code_word)
    code_word_orig_to_sorted_index = dict()
    code_word_sorted_to_orig_index = dict()
    for idx, c in enumerate(code_word):
        sorted_index = code_word_sorted.index(c)
        code_word_orig_to_sorted_index[idx] = sorted_index
        code_word_sorted_to_orig_index[sorted_index] = idx

    code_word_grid = []
    current_col = 0
    current_row = []
    for c in encrypted_message:
        if current_col % code_word_len == 0:
            if current_row:
                code_word_grid.append(current_row)
            current_col = 0
            current_row = []
        current_row.append(c)
        current_col += 1

    if current_row:
        if len(current_row) == code_word_len:
            code_word_grid.append(current_row)
        else:
            last_row = [None] * code_word_len
            last_row_idx = 0
            for c in current_row:
                orig_idx = code_word_sorted_to_orig_index[last_row_idx]
                while orig_idx > len(current_row):
                    last_row_idx += 1
                    orig_idx = code_word_sorted_to_orig_index[last_row_idx]
                last_row[last_row_idx] = c
                last_row_idx += 1
            code_word_grid.append(last_row)

    code_word_grid_reordered = []
    for r in code_word_grid:
        reordered_row = [None] * code_word_len
        for idx, c in enumerate(r):
            reordered_row[code_word_sorted_to_orig_index[idx]] = c
        code_word_grid_reordered.append(reordered_row)

    decrypted_message, row, col = "", None, None
    for grid_row in code_word_grid_reordered:
        for c in grid_row:
            if c is None:
                continue

            if row is None:
                row = ADFGVX_POS_MAP[c]
            elif col is None:
                col = ADFGVX_POS_MAP[c]

            if row is not None and col is not None:
                decrypted_message += substitution_grid[row][col]
                row, col = None, None

    return decrypted_message


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
