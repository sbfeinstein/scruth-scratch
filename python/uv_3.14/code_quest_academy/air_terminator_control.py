import datetime
import sys


def threat_level(is_friendly, data_points):

    # Transponder criteria can fast-return
    if is_friendly == "TRUE":
        return "NONE"

    # Longest continuous series and num times entering airspace criteria
    prev_entry_time = None
    num_entries = 0
    num_continuous = 1
    max_continuous = 1
    for data_point in data_points:
        entry_hour, entry_minute = data_point.split(":")
        entry_time = datetime.datetime(
            2026, 2, 28, int(entry_hour), int(entry_minute), 0, 0
        )
        diff = entry_time - prev_entry_time if prev_entry_time else None
        prev_entry_time = entry_time

        if diff == datetime.timedelta(0, 0, 0, 0, 15, 0, 0):
            num_continuous += 1
        else:
            num_entries += 1
            if num_continuous > max_continuous:
                max_continuous = num_continuous
            num_continuous = 1
        # print(f"  entry_time = {entry_time} and diff is {diff}")
    if num_continuous > max_continuous:
        max_continuous = num_continuous
    # print(f"  num_entries = {num_entries}, max_continuous = {max_continuous}")

    # Combine criteria for answer
    if len(data_points) >= 36 or max_continuous >= 12 or num_entries >= 8:
        return "HIGH"
    elif len(data_points) >= 24 or max_continuous >= 8 or num_entries >= 4:
        return "MEDIUM"
    elif len(data_points) >= 12 or max_continuous >= 4:
        return "LOW"
    else:
        return "NONE"


def main():
    """
    https://lmcodequestacademy.com/api/static/problems/air-terminator-control
    run (assumes correct python installed and active, e.g. via the uv framework of the parent folder) via:
        python air_terminator_control.py < inputs/air_terminator_control_1.in
    :return:
    """
    num_cases = int(sys.stdin.readline())
    for _ in range(num_cases):
        is_friendly, num_data_points = sys.stdin.readline().split(" ")
        data_points = [sys.stdin.readline() for _ in range(int(num_data_points))]
        print(f"{threat_level(is_friendly, data_points)}")


if __name__ == "__main__":
    main()
