"""
Description: 
    Utilizes 'trial division' to determine if a number is prime
    only loops through numbers up to sqrt(num)
Args:
    num: passed number to test prime-ness
Returns:
    return True if prime
    return False if composite
"""


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


"""
Description: see ../text_files/re_id.txt for description
    dynamically creates a prime string long enough to contain the new_id for any given employee
    once a long enough (id start position + 6 extra) is obtained it breaks out
    creates substring of prime_number_st to give to employee as their new id
Args:
    id: passed id starting position
Returns:
    return string value of their new_id based on prime string
Test Cases Used:
    0 # Expected output 23571
    3 # Expected output 71113
"""


def solution(id):
    prime_number_str = ""

    for i in range(0, 10000):
        if len(prime_number_str) >= (id + 6):
            break
        if is_prime(i):
            prime_number_str += str(i)

    print(prime_number_str)
    new_id = prime_number_str[id:id + 5]

    return str(new_id)
