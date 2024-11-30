"""
Description: see ../text_files/grandest_staircase_of_them_all.txt for descriptoin
    Uses Partition Theory to calculate valid partitions of the bricks
    So stairs = 5, partitioning would find
        1 + 5, 2 + 3, 3 + 2, and 5 + 1 as valid partitions (based on guidelines see above)

    arr[k - 1][x] is partitioning stairs = x using parts smaller than k
    arr[k - 1][x - k] is partitioning stairs = (x - k) using parts smaller than k
    add arr[k - 1][x - k] only if x >= k else add 0

Args:
    stairs: the number of stairs Commander Lambda gave us
Returns:
    returns number of partitions divided by 2 for mirrored partitions
Test Cases Used:
    3 # Expected output 1
    4 # Expected output 1
    5 # Expected output 2
    6 # Excepted output 3
    200 # Expected output 487067745
"""


def solution(stairs):

    arr = [[0 for _ in range(stairs + 1)] for _ in range(stairs + 1)]

    for _ in range(stairs + 1):
        arr[_][0] = 1

    for row in range(1, stairs + 1):
        for col in range(0, stairs + 1):
            arr[row][col] = arr[row - 1][col] + (arr[row - 1][col - row] if col >= row else 0)

    return int(arr[stairs - 1][stairs])
