import tqdm

def error_check(data_ints: list[int], data_directions: list[str]) -> None:
    """Check that the input data is valid.

    Parameters:
    -----------
        data_ints (list[int]): List of integers representing movement amounts.
        data_directions (list[str]): List of strings representing movement directions.

    Returns:
    --------
        None

    Raises:
    -------
        ValueError: If the input data is not valid.
    """
    if not isinstance(data_ints, list):
        raise ValueError(f"data_ints must be a list of integet, instead got {type(data_ints)}")
    if not isinstance(data_directions, list):
        raise ValueError(f"data_directions must be a list of strings, instead got {type(data_directions)}")
    if not all(isinstance(x,int) for x in data_ints):
        raise ValueError("data_ints must be a list of integers")
    if not all(isinstance(x,str) for x in data_directions):
        raise ValueError("data_directions must be a list of strings.")        


def part_1_logic(
    data_ints: list[int], data_directions: list[str], dial: int = 50
) -> int:
    """
    Main logic used for part 1 of day 1.

    Parameters:
    -----------
        data_ints (list[int]): List of integers representing movement amounts.
        data_directions (list[str]): List of strings representing movement directions.
        dial (int): Starting position on the dial. Default is 50.

    Returns:
    --------
            int: The count of times the dial hits zero.
        """
    zero_counter = 0
    error_check(data_ints, data_directions)
    for i, num in tqdm.tqdm(enumerate(data_ints), total=len(data_ints)):
        direction = data_directions[i]
        if direction == "L":
            dir_sign = -1
        elif direction == "R":
            dir_sign = 1
        else:
            raise ValueError(f"Unknown direction: {direction}")

        dial = (dial + dir_sign * num) % 100
        if dial == 0:
            zero_counter += 1
    return zero_counter


def part_2_logic(
    data_ints: list[int], data_directions: list[str], dial: int = 50
) -> int:
    """
    Main logic used for part 2 of day 1.

    Parameters:
    -----------
        data_ints (list[int]): List of integers representing movement amounts.
        data_directions (list[str]): List of strings representing movement directions.
        dial (int): Starting position on the dial. Default is 50.

    Returns:
    --------
            int: The count of times the dial hits zero.
        """
    zero_counter = 0
    error_check(data_ints, data_directions)
    for i, num in enumerate(data_ints):
        direction = data_directions[i]
        if direction == "L":
            dir_sign = -1
        elif direction == "R":
            dir_sign = 1
        else:
            raise ValueError(f"Unknown direction: {direction}")

        for i in range(0, num, 1):
            dial = dial + dir_sign
            if dial < 0:
                dial = 99
            elif dial > 99:
                dial = 0
            if dial == 0:
                zero_counter += 1

    return zero_counter


def day_1(data_ints: list[int], data_directions: list[str], part: int = 1) -> int:
    """Wrapper logic for day 1.
    
    Parameters:
    -----------
        data_ints (list[int]): List of integers representing movement amounts.
        data_directions (list[str]): List of strings representing movement directions.
        part (int): Part of the puzzle to solve (1 or 2). Default is 1.

    Returns:
    --------
        int: The solution to part 1.
    """

    if part == 1:
        zero_counter = part_1_logic(data_ints, data_directions)

    else:  # part 2
        zero_counter = part_2_logic(data_ints, data_directions)

    return zero_counter


if __name__ == "__main__":
    from utils.helper_funcs import open_data_text_file, split_data
    day = 1
    data = open_data_text_file(day, test=False)
    data_list = split_data(data, "\n")
    data_ints = [int(i[1:]) for i in data_list]
    data_directions = [i[0] for i in data_list]

    assert len(data_ints) == len(data_directions)
    result_part_1 = day_1(data_ints, data_directions, part=1)
    print(f"Part 1 Result: {result_part_1}")
    result_part_2 = day_1(data_ints, data_directions, part=2)
    print(f"Part 2 Result: {result_part_2}")
