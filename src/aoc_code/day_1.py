from aoc_code.utils.helper_funcs import open_data_text_file, split_data

def part_1_logic(data_ints: list[int], data_directions: list[str], dial: int = 50) -> int:
    zero_counter = 0
    for i, num in enumerate(data_ints):
        direction = data_directions[i]
        if direction == 'L':
            dir_sign = -1
        elif direction == 'R':
            dir_sign = 1
        else:
            raise ValueError(f"Unknown direction: {direction}")
        
        dial = (dial + dir_sign * num) % 100
        if dial == 0:
            zero_counter += 1
    return zero_counter

def part_2_logic(data_ints: list[int], data_directions: list[str], dial: int = 50) -> int:
    zero_counter = 0
    for i, num in enumerate(data_ints):
        direction = data_directions[i]
        if direction == 'L':
            dir_sign = -1
        elif direction == 'R':
            dir_sign = 1
        else:
            raise ValueError(f"Unknown direction: {direction}")

        for i in range(0,num,1):
            dial = dial + dir_sign
            if dial < 0:
                dial = 99
            elif dial > 99:
                dial = 0
            if dial == 0:
                zero_counter += 1

    return zero_counter



def day_1(data_ints: list[int], data_directions: list[str], part: int = 1) -> int:
    """Solve part 1 of day 1.

    Args:
        data (str): The input data as a string.

    Returns:
        int: The solution to part 1.
    """

    if part == 1:
        zero_counter = part_1_logic(data_ints, data_directions)
    
    else: # part 2
        zero_counter = part_2_logic(data_ints, data_directions)


    return zero_counter

if __name__ == "__main__":
    day = 1
    data = open_data_text_file(day, test=True)
    data_list = split_data(data, "\n")
    data_ints = [int(i[1:]) for i in data_list]
    data_directions = [i[0] for i in data_list]

    assert len(data_ints) == len(data_directions)
    result_part_1 = day_1(data_list, part=1)
    print(f"Part 1 Result: {result_part_1}")
    result_part_2 = day_1(data_list, part=2)
    print(f"Part 2 Result: {result_part_2}")


