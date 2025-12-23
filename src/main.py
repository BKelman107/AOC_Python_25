from aoc_code.utils import open_data_text_file, split_data
from aoc_code import day_1  # import other days as needed
import argparse


def main(day: int, test: bool = False) -> None:
    if test:
        print(f"Running in test mode with day={day}")
    else:
        print(f"Running in production mode with day={day}")

    # day = 1
    if day == 1:
        data = open_data_text_file(day, test)
        data_list = split_data(data, "\n")
        data_ints = [int(i[1:]) for i in data_list]
        data_directions = [i[0] for i in data_list]

        assert len(data_ints) == len(data_directions)
        result_part_1 = day_1(data_ints, data_directions, part=1)
        print(f"Part 1 Result: {result_part_1}")
        result_part_2 = day_1(data_ints, data_directions, part=2)
        print(f"Part 2 Result: {result_part_2}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("--day", type=int, required=True, help="Day number to run.")
    parser.add_argument("--test", action="store_true", help="Run with test input.")
    args = parser.parse_args()

    main(day=args.day, test=args.test)
