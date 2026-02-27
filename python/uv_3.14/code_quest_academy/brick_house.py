import sys


def is_possible(num_small, num_large, target_length):
    remaining_large = num_large
    remaining_small = num_small
    remaining_target = target_length

    while remaining_target > 0 and remaining_large > 0:
        remaining_target -= 5
        remaining_large -= 1

    while remaining_target > 0 and remaining_small > 0:
        remaining_target -= 1
        remaining_small -= 1

    return remaining_target == 0

def main():
    """
    https://lmcodequestacademy.com/api/static/problems/brick-house
    run (assumes correct python installed and active, e.g. via the uv framework of the parent folder) via:
        python brick_house.py < inputs/brick_house_1.in
    :return:
    """
    num_cases = int(sys.stdin.readline())
    for lines_read in range(num_cases):
        num_small, num_large, target_length = sys.stdin.readline().split(' ')
        print(f"{is_possible(int(num_small), int(num_large), int(target_length))}")


if __name__ == "__main__":
    main()
