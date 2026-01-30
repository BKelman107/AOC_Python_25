import tqdm
import re

PATTERN = "\b(\d+)\1+\b"

def part_1_logic(num):
    """
    Logic for part 1 of day 2.
    
    Parameters:
    -----------
        num (int): The number to check against the pattern.
        
    Returns:
    --------
        str: The regex pattern if the number meets the criteria, else an empty string.
    """
    # For part 1, we are looking for repeating patterns - no odd length numbers allowed
    if len(str(num)) % 2 == 1:
        return ""
    else: 
        return PATTERN

def part_2_logic(num):
    return PATTERN

def day_2_logic(part, data_list):
    """Wrapper logic for day 2.
    
    Parameters:
    -----------
        part (int): Part of the puzzle to solve (1 or 2).
        data_list (list[str]): List of string ranges to process.

    Returns:
    --------
        int: Sum of disallowed IDs based on the specified part's logic.
    """
    disallowed_ids = []
    for item in tqdm.tqdm(data_list):
        lower, upper = item.split('-')
        for num in range(int(lower), int(upper) + 1):
            if part == 1:
                pattern = part_1_logic(num)
            elif part == 2:
                pattern = part_2_logic(num)
            if pattern != "":
                re.search(pattern, str(num))
                disallowed_ids.append(num)

    return sum(disallowed_ids)


if __name__ == "__main__":
    from utils.helper_funcs import open_data_text_file, split_data

    data = open_data_text_file(2, test=False)
    data_list = split_data(data, ",")
    print(f'Part 1 disallowed IDs: {day_2_logic(1,data_list)}')
    print(f'Part 2 disallowed IDs: {day_2_logic(2,data_list)}')
