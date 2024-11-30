"""
Description:
    Allows more practice with a recurrence solution to partition theory
    creates 2d array and initializes 0th elem to 1 since there is only 1 way to partition 0
    row is largest number allowed for given row section
    col is the targe number being partitioned
Args:
    num: passed number to find all given partitions
Returns:
    returns integer value of given partitions
Test Cases Used:
    num = 4 # Expected output 5
    num = 6 # Expected output 11
    num = 30 # Expected output 5604
"""


def count_all_partitions(num):
    arr = [[0 for _ in range(num + 1)] for _ in range(num + 1)]

    arr[0][0] = 1

    for row in range(1, num + 1):
        for col in range(0, num + 1):
            arr[row][col] = arr[row - 1][col] + (arr[row][col - row] if col >= row else 0)

    return int(arr[num][num])


"""
Description:
    Allows more practice with a recurrence solution to partition theory
    creates 2d array and initializes 0th elem to 1 since there is only 1 way to partition 0
    row is largest number allowed for given row section
    col is the targe number being partitioned
    takes 'num' and finds all partitions of said 'num' into constrained parts defined by 'partitions'
Args:
    num: passed number to find all given partitions
    partition: limit on how many elements can be in a partition
Returns:
    returns integer value of given ways to partition number into specified limit
Test Cases Used:
    num = 6, partitions = 3 # Expected output 3
    num = 7, partitions = 3 # Expected output 4
    num = 9, partitions = 4 # Expected output 6
"""


def count_partitions_with_exact_parts(num, partitions):
    arr = [[[0 for _ in range(partitions + 1)] for _ in range(num + 1)] for _ in range(num + 1)]

    arr[0][0][0] = 1

    for row in range(1, num + 1):
        for col in range(num + 1):
            for parts in range(partitions + 1):
                arr[row][col][parts] += arr[row - 1][col][parts]

                if col >= row and parts > 0:
                    arr[row][col][parts] += arr[row][col - row][parts - 1]

    return int(arr[num][num][partitions])


"""
Description:
    Allows more practice with a recurrence solution to partition theory
    creates 2d array and initializes 0th elem to 1 since there is only 1 way to partition 0
    row is largest number allowed for given row section
    col is the targe number being partitioned
    finds all partitions made up of exclusively odd numbers
Args:
    num: passed number to find all given partitions
Returns:
    returns integer value of given partitions made of exclusively odd numbers
Test Cases Used:
    num = 6 # Expected output 3
    num = 8 # Expected output 6
    num = 10 # Expected output 10
"""


def count_partitions_with_odd_members(num):
    arr = [[0 for _ in range(num + 1)] for _ in range(num + 1)]

    for row in range(1, num + 1):
        arr[row][0] = 1

    for row in range(1, num + 1):
        for col in range(1, num + 1):
            arr[row][col] = arr[row - 1][col] + (arr[row][col - row] if (col >= row and row % 2 == 1) else 0)

    return int(arr[num][num])


"""
Description:
    Allows more practice with a recurrence solution to partition theory
    creates 2d array and initializes 0th elem to 1 since there is only 1 way to partition 0
    row is largest number allowed for given row section
    col is the targe number being partitioned
    finds partitions made of distinct numbers (no repeats)
Args:
    num: passed number to find all given partitions
Returns:
    returns integer value of given partitions made of exclusively distinct numbers
Test Cases Used:
    num = 6 # Expected output 4
    num = 8 # Expected output 6
    num = 10 # Expected output 10
"""


def count_partitions_with_distinct_members(num):
    arr = [[0 for _ in range(num + 1)] for _ in range(num + 1)]

    arr[0][0] = 1

    for row in range(1, num + 1):
        for col in range(0, num + 1):
            arr[row][col] = arr[row - 1][col] + (arr[row - 1][col - row] if col >= row else 0)

    return int(arr[num][num])


"""
Description:
    Allows more practice with a recurrence solution to partition theory
    creates 2d array and initializes 0th elem to 1 since there is only 1 way to partition 0
    row is largest number allowed for given row section
    col is the targe number being partitioned
    finds partitions and stores partitions (and the steps it took to create it)
Args:
    num: passed number to find all given partitions
    mult: passed number to check if all bits in the partition % mult == 0
Returns:
    returns integer value of given partitions made of all bits being modulo mult
Test Cases Used:
    num = 6, mult = 3 # Expected output 2
    num = 6, mult = 2 # Expected output 3
    num = 8, mult = 3 # Expected output 0
"""


def count_partitions_with_sum_to_multiple(num, mult):
    arr = [[[[] for _ in range(num + 1)] for _ in range(num + 1)] for _ in range(num + 1)]

    arr[0][0] = [[]]

    for row in range(1, num + 1):
        for col in range(0, num + 1):
            # Carry over partitions without using the current row
            arr[row][col] = arr[row - 1][col]

            # Add partitions that include the current row
            if col >= row:
                arr[row][col] += (part + [row] for part in arr[row][col - row])

    mult_count = 0
    for part in arr[num][num]:
        if sum(part) == num:
            if all(p % mult == 0 for p in part):
                print(part)
                mult_count += 1

    return mult_count


"""
Description:
    Allows more practice with a recurrence solution to partition theory
    creates 2d array and initializes 0th elem to 1 since there is only 1 way to partition 0
    row is largest number allowed for given row section
    col is the targe number being partitioned
    finds partitions and stores partitions (and the steps it took to create it)
Args:
    num: passed number to find all given partitions
    limit: passed number to check if all bits in the partition are less than or equal to limit
Returns:
    returns integer value of given partitions made of all bits <= limit
Test Cases Used:
    num = 6, mult = 3 # Expected output 7
    num = 5, mult = 2 # Expected output 3
    num = 7, mult = 4 # Expected output 11
"""


def count_partitions_with_max_partition_limit(num, limit):
    arr = [[[[] for _ in range(num + 1)] for _ in range(num + 1)] for _ in range(num + 1)]

    arr[0][0] = [[]]

    for row in range(1, num + 1):
        for col in range(0, num + 1):
            # Carry over partitions without using the current row
            arr[row][col] = arr[row - 1][col]

            # Add partitions that include the current row
            if col >= row:
                arr[row][col] += (part + [row] for part in arr[row][col - row])

    mult_count = 0
    for part in arr[num][num]:
        if sum(part) == num:
            if all(p <= limit for p in part):
                print(part)
                mult_count += 1

    return mult_count


"""
Description:
    Allows more practice with a recurrence solution to partition theory
    creates 2d array and initializes 0th elem to 1 since there is only 1 way to partition 0
    row is largest number allowed for given row section
    col is the targe number being partitioned
    finds partitions and stores partitions (and the steps it took to create it)
Args:
    num: passed number to find all given partitions
    gap: passed number to check if any bit has a gap equal to or greater than this gap
Returns:
    returns integer value of given partitions that have atleast one 'gap' that satisfies gap arg
Test Cases Used:
    num = 6, gap = 1 # Expected output 7
    num = 6, gap = 2 # Expected output 4
    num = 8, gap = 3 # Expected output 6
    num = 10, gap = 2 # Expected output 27
"""


def count_partitions_with_gap_constraint_any(num, gap):
    arr = [[[[] for _ in range(num + 1)] for _ in range(num + 1)] for _ in range(num + 1)]

    arr[0][0] = [[]]

    for row in range(1, num + 1):
        for col in range(0, num + 1):
            # Carry over partitions without using the current row
            arr[row][col] = arr[row - 1][col]

            # Add partitions that include the current row
            if col >= row:
                arr[row][col] += (part + [row] for part in arr[row][col - row])

    gap_count = 0
    for part in arr[num][num]:
        if sum(part) == num:
            max_gap = 0
            for p in range(1, len(part)):
                if part[p] - part[p-1] > max_gap:
                    max_gap = part[p] - part[p-1]
                    if max_gap >= gap:
                        gap_count += 1
                        break

    return gap_count


"""
Description:
    Allows more practice with a recurrence solution to partition theory
    creates 2d array and initializes 0th elem to 1 since there is only 1 way to partition 0
    row is largest number allowed for given row section
    col is the targe number being partitioned
    finds partitions and stores partitions (and the steps it took to create it)
Args:
    num: passed number to find all given partitions
    gap: passed number to check if any bit has a gap equal to or greater than this gap
Returns:
    returns integer value of given partitions that all parts satisfy the passed gap arg
Test Cases Used:
    num = 6, gap = 1 # Expected output 3
    num = 6, gap = 2 # Expected output 2
    num = 8, gap = 3 # Expected output 2
    num = 10, gap = 2 # Expected output 5
"""


def count_partitions_with_gap_constraint_all(num, gap):
    arr = [[[[] for _ in range(num + 1)] for _ in range(num + 1)] for _ in range(num + 1)]

    arr[0][0] = [[]]

    for row in range(1, num + 1):
        for col in range(0, num + 1):
            # Carry over partitions without using the current row
            arr[row][col] = arr[row - 1][col]

            # Add partitions that include the current row
            if col >= row:
                arr[row][col] += (part + [row] for part in arr[row][col - row])

    gap_count = -1
    for part in arr[num][num]:
        if sum(part) == num:
            gap_count += 1
            for p in range(1, len(part)):
                if part[p] - part[p-1] < gap:
                    gap_count -= 1
                    break

    return gap_count


"""
Description:
    Allows more practice with a recurrence solution to partition theory
    creates 2d array and initializes 0th elem to 1 since there is only 1 way to partition 0
    row is largest number allowed for given row section
    col is the targe number being partitioned
    finds partitions and stores partitions (and the steps it took to create it)
    utilizes same is_prime() function from re-ip.py
Args:
    num: passed number to find all given partitions
Returns:
    returns integer value of given partitions that all parts are prime
Test Cases Used:
    num = 5 # Expected output 2
    num = 7 # Expected output 3
    num = 10 # Expected output 5
    num = 11 # Expected output 6
"""


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def count_partitions_with_prime_constraint(num):
    arr = [[[[] for _ in range(num + 1)] for _ in range(num + 1)] for _ in range(num + 1)]

    arr[0][0] = [[]]

    for row in range(1, num + 1):
        for col in range(0, num + 1):
            # Carry over partitions without using the current row
            arr[row][col] = arr[row - 1][col]

            # Add partitions that include the current row
            if col >= row:
                arr[row][col] += (part + [row] for part in arr[row][col - row])

    prime_count = 0
    for part in arr[num][num]:
        if sum(part) == num:
            print(part)
            prime_count += 1
            for p in part:
                if not is_prime(p):
                    prime_count -= 1
                    break

    return prime_count
