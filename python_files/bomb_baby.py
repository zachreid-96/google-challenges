"""
Description: See ../text_files/bomb_baby.txt for description
    Since the bombs brought on board are M: 1 and F: 1
    we need to find the generations to get the passed Mach and Facula numbers
    checks to see if mach > facula and subtracts
    checks to see if facula > mach and subtracts
    if one dips below 0 return 'impossible'
    if both EQUAL 1 returns generations
    if both EQUAL each other and NOT 1 returns 'impossible'
Args:
    mach: target number of mach bombs
    facula: target number of facula bombs
Returns:
    returns str(generations) if both target numbers are possible
    returns 'impossible' if both target numbers are not possible
Test Cases Used:
    ('4', '7') # Expected output 4
    ('2', '1') # Expected output 1
    ('2', '4') # Expected output "impossible"
    ('57', '115') # Expected output 58
"""


def solution(mach, facula):
    generations = 0

    mach = int(mach)
    facula = int(facula)

    while True:

        if mach < 1 or facula < 1:
            return 'impossible'

        if mach == 1 and facula == 1:
            break

        if facula > mach:
            facula -= mach
            generations += 1
        elif mach > facula:
            mach -= facula
            generations += 1
        elif mach == facula:
            return 'impossible'

    return str(generations)
