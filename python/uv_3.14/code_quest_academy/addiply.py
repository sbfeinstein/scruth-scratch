import sys


def main():
    """
    https://lmcodequestacademy.com/problem/addiply
    run (assumes correct python installed and active, e.g. via the uv framework of the parent folder) via:
        python addiply.py < inputs/addiply_1.in
    :return:
    """
    num_cases = int(sys.stdin.readline())
    for _ in range(num_cases):
        first, second = sys.stdin.readline().split(' ')
        print(f"{int(first) + int(second)} {int(first) * int(second)}")


if __name__ == "__main__":
    main()
