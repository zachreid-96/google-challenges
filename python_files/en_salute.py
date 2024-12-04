"""
Description: see ../text_files/en_salute.txt for description
    right_counter: tracks minions going to the right and adds (2) for each minion '>'
    total_salutes: tracks number of salutes that happen between '>' and '<'

    tracks minions going right as that is natural direction of loop
    each '>' adds (2) to right_counter then each instance of '<' adds right_counter to total_salutes
    does nothing if '-' empty space is encountered
Args:
    salute: passed string of minions in the hallway (need to analyze salute count)
Returns:
    returns int value of the number of salutes that happen during the passed arg 'salute'
Test Cases Used:
    "--->-><-><-->-" # Expected output of 10
    ">----<" # Expected output of 2
    "<<>><" # Expected output of 4
"""


def solution(salute):

    right_counter = 0
    total_salutes = 0

    for s in range(len(salute)):
        if salute[s] == ">":
            right_counter += 2
        elif salute[s] == "<":
            total_salutes += right_counter
        elif salute[s] == "-":
            continue

    return total_salutes
