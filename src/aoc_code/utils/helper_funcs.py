import os
import pathlib


def open_data_text_file(day: int, test: bool = False) -> str:
    """Open the data text file for the given day.

    Args:
        day (int): The day number.
        test (bool, optional): Whether to open the test input file. Defaults to False.

    Returns:
        str: The contents of the data text file.
    """
    current_dir = pathlib.Path(__file__).parents[3]
    data_dir = current_dir / f"data/day_{day}"
    if test:
        file_name = "test_input.txt"
    else:
        file_name = "input.txt"
    data_file_path = os.path.join(data_dir, file_name)
    with open(data_file_path, "r") as f:
        data = f.read().strip()
    return data

def split_data(data: str, split_command: str) -> list[str]:
    return data.split(split_command)