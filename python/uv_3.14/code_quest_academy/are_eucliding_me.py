import sys


def is_coprime(first, second):
    if first == 1 and second == 1:
        return "COPRIME"
    elif first == second:
        return "NOT COPRIME"
    else:
        minuend, subtrahend = (first, second) if first > second else (second, first)
        diff = minuend - subtrahend
        print(f"{minuend}-{subtrahend}={diff}")
        return is_coprime(subtrahend, diff)

def main():
    """
    https://lmcodequestacademy.com/api/static/problems/are-eucliding-me
    run (assumes correct python installed and active, e.g. via the uv framework of the parent folder) via:
        python are_eucliding_me.py < inputs/are_eucliding_me_1.in
    :return:
    """
    num_cases = int(sys.stdin.readline())
    for _ in range(num_cases):
        first, second = sys.stdin.readline().split(',')
        print(f"{is_coprime(int(first), int(second))}")


if __name__ == "__main__":
    main()
