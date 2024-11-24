import math
from itertools import permutations

"""
Description: Recursively continues the party from brute_force
    recursively checks if passed permutation will give the same output as the passed original order
    this is a 'smart brute force' method, smart because it checks until it fails
    checks layer by layer (doesn't check depth 7 if depth 3 fails)
    will get 'head' of each list and compare them
        if EQUAL - calls itself with the lists split into their right and left trees
        if NOT-EQUAL - returns False
            
    true_order = [2, 3, 1] && perm = [2, 1, 3]
    true_head = 2 && perm_head = 2 -- EQUAL SO
    true_head_left, perm_head_left = [1] && true_head_right, perm_head_right = [3]
    calls itself again
        
    true_order = [2, 1, 3] && perm = [3, 2, 1]
    true_head = 2 && perm_head = [3] -- NOT-EQUAL SO
    return False
        
Args:
    true_order: a list of numbers [4, 3, 1, 2]; the original list of numbers passed
    perm: a list of numbers [3, 2, 1, 4]; the permutation of the original list
Returns:
    True if the entire order is preserved and will result in same tree
    False if the order is not preserved and will not result in same tree
Test Cases Used:
    [5, 9, 8, 2, 1] # Expected output 6
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Expected output 1
    [5, 2, 1, 3, 6] # Expected output 8
"""


def brute_force_solve(true_order, perm):
    if true_order == []:
        return True

    if perm == []:
        return True

    true_head = true_order[0]
    true_remainder = true_order[1:]

    perm_head = perm[0]
    perm_remainder = perm[1:]

    if true_head == perm_head:

        true_head_left = [true_remainder[i] for i in range(len(true_remainder)) if true_remainder[i] < true_head]
        true_head_right = [true_remainder[i] for i in range(len(true_remainder)) if true_remainder[i] > true_head]

        perm_head_left = [perm_remainder[i] for i in range(len(perm_remainder)) if perm_remainder[i] < perm_head]
        perm_head_right = [perm_remainder[i] for i in range(len(perm_remainder)) if perm_remainder[i] > perm_head]

        if brute_force_solve(true_head_left, perm_head_left) and brute_force_solve(true_head_right, perm_head_right):
            return True

    return False


"""
Description: Wrapper for brute_force_solve (gets the party started)
    takes the original sequence, finds the tree head and the tree remainder
    finds the tree left && finds the tree right (based on tree_head)
    gets all permutations of the remainder and loops them
    in LOOP finds perm tree left and perm tree right
    checks if perm tree left and perm tree right will result in same as true tree left and true tree right
Args:
    seq: the passed sequence and will need to find all permutations of said sequence that result in same tree
Returns:
    returns the string of how many permutations result in the same tree formation
Test Cases Used:
    [5, 9, 8, 2, 1] # Expected output 6
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Expected output 1
    [5, 2, 1, 3, 6] # Expected output 8
Test Cases Used:
    [5, 9, 8, 2, 1] # Expected output 6
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Expected output 1
    [5, 2, 1, 3, 6] # Expected output 8
"""


def brute_force(seq):
    matches_found = 0

    start_head = seq[0]
    remainder = seq[1:]

    true_left = [remainder[i] for i in range(len(remainder)) if remainder[i] < start_head]
    true_right = [remainder[i] for i in range(len(remainder)) if remainder[i] > start_head]

    perms = list(permutations(remainder))

    for perm in perms:

        left_perm = [perm[i] for i in range(len(perm)) if perm[i] < start_head]
        right_perm = [perm[i] for i in range(len(perm)) if perm[i] > start_head]

        if brute_force_solve(true_left, left_perm) and brute_force_solve(true_right, right_perm):
            matches_found += 1

    return str(matches_found)


"""
Description: 
    Recursively finds the binomial coefficient for a given set of numbers and multiplies up the tree
Args:
    seq: the passed set of numbers
Returns:
    returns the number of permutations that result in the same tree
"""


def binomial_coefficient(seq):
    if len(seq) <= 2:
        return 1

    head = seq[0]
    left = [seq[i] for i in range(len(seq)) if seq[i] < head]
    right = [seq[i] for i in range(len(seq)) if seq[i] > head]

    current_coefficient = (math.factorial(len(left) + len(right)) /
                           (math.factorial(len(left)) * math.factorial(len(right))))
    left_coefficient = binomial_coefficient(left)
    right_coefficient = binomial_coefficient(right)

    return int(current_coefficient * left_coefficient * right_coefficient)


"""
Description: 
    wrapper for binomial_coefficient(seq)
    named solution as per the google challenge description in ../text_files/binary_bunnies.txt
Args:
    seq: the passed set of numbers
Returns:
    returns string value of permutations of seq that will create same tree
Test Cases Used:
    [5, 9, 8, 2, 1] # Expected output 6
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Expected output 1
    [5, 2, 1, 3, 6] # Expected output 8
"""


def solution(seq):
    return str(binomial_coefficient(seq))
