"""
Description: see ../text_files/minion_hierarchy.txt for description
    Uses a dict preset with {0: 1} to count the minions
        preset with {0: 1} to account for Professor Boolean
    loops through range of levels and find how many employees at each level
    then loops through dict values and adds them
Args:
    levels: how many levels of supervision there are
Returns:
    returns integer value of how many employees there are
Test Cases Used:
    1 # Expected output 1
    2 # Expected output 57
    3 # Expected output 400
"""


def answer(levels):
    # Has max of 7 reports for 1 manager

    my_dict = {0: 1}

    for i in range(1, levels + 1):
        my_dict[i] = my_dict[i - 1] * 7

    total_employees = 0
    for v in my_dict.values():
        total_employees += v

    return total_employees
