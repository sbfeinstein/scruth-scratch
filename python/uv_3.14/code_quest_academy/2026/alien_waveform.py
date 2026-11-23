import re
import sys


def pattern_to_regex(pattern, components=None, is_alternatives=False) -> str:
    # Regex stuff, see:
    #   https://docs.python.org/3/howto/regex.html
    #   https://docs.python.org/3/library/re.html

    if components is None:
        components = []

    if not pattern:
        join_operator = "|" if is_alternatives else ""
        return join_operator.join(map(str, components))

    c = pattern[:1]
    remainder = pattern[1:]

    if c == '.':
        components.append('*')
    elif c == '-':
        components.append('+')
    elif c == '/':
        components.append('?')
    elif c == '(':
        closing_index = find_closing_index(remainder, '(', ')')
        alternatives_pattern = remainder[:closing_index]
        remainder = remainder[closing_index:]
        alternatives_component = pattern_to_regex(pattern=alternatives_pattern)
        components.append(f"(?:{alternatives_component})")
    elif c == '[':
        closing_index = find_closing_index(remainder, '[', ']')
        alternatives_pattern = remainder[:closing_index]
        remainder = remainder[closing_index:]
        alternatives_component = pattern_to_regex(pattern=alternatives_pattern, is_alternatives=True, )
        components.append(f"(?:{alternatives_component})")
    elif not c in [']', ')']:
        components.append(c)

    return pattern_to_regex(pattern=remainder, components=components, is_alternatives=is_alternatives)


def find_closing_index(s: str, open_char: str, close_char: str) -> int:
    remaining = 1
    for idx, c in enumerate(s):
        if c == open_char:
            remaining += 1
        elif c == close_char:
            remaining -= 1
        if remaining == 0:
            return idx
    raise ValueError("No matching closing character")


def process(patterns, data_stream):
    def find_best():
        result_span = None
        result_pattern = None
        for pattern in patterns:
            result = pattern[0].search(data_stream, pos=pos)
            if not result or not result.span(0):
                continue
            current_span = result.span(0)
            if not result_span \
                    or (current_span[0] < result_span[0]) \
                    or (current_span[0] == result_span[0] and current_span[1] > result_span[1]):
                result_span = current_span
                result_pattern = pattern
        return result_span, result_pattern

    # print(f"Processing patterns:\n{"".join(map(lambda t: f"'{t[0]}' to '{t[1]}'\n", patterns))}")
    # print(f"Processing data_stream:\n{data_stream}")

    pos = 0
    in_message = False
    found_any_messages = False
    while pos < len(data_stream):
        best_span, best_pattern = find_best()
        if not best_span:
            if in_message:
                print()
            break
        found_any_messages = True
        if in_message and best_span[0] > pos + 7:
            print()
            in_message = False
        if not in_message:
            print(f"MESSAGE AT {best_span[0]} ", end='')
        in_message = True
        print(best_pattern[1], end='')
        pos = best_span[1]
    if not found_any_messages:
        print("NO MESSAGES")


def main():
    """
    Problem 300: Alien Waveform
    Difficulty: Hard
    https://lmcodequestacademy.com/problem/alien-waveform
    run (assumes correct python installed and active, e.g. via the uv framework of the parent folder) via:
        python alien_waveform.py < inputs/alien_waveform_1.in
    :return:
    """
    # sys.stdin = io.StringIO(SAMPLE_INPUT)

    num_cases = int(sys.stdin.readline())
    for case_num in range(num_cases):
        patterns = []
        data_stream = ""
        d_count, s_count = sys.stdin.readline().split(" ")
        for _ in range(int(d_count)):
            pattern, linguistic_unit = sys.stdin.readline().split(" ", 1)
            patterns.append((re.compile(pattern_to_regex(pattern)), linguistic_unit.strip()[1:-1]))
        for _ in range(int(s_count)):
            data_stream += sys.stdin.readline().strip()
        process(patterns, data_stream)


if __name__ == "__main__":
    main()
