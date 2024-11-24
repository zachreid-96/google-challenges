"""
Description:
    Used to test the algorithm given
Args:
    message: the passed message in test cases
Returns:
    returns digest the 'hash'
"""


def get_digest(message):
    digest = [0] * 16

    digest[0] = ((129 * 0) ^ 0) % 256

    for i in range(1, len(digest)):
        digest[i] = ((129 * message[i]) ^ message[i - 1]) % 256

    return digest


"""
Description: 
    used to find the mod inverse of (129, 256)
    checks numbers up to mult (129) for a match
Args:
    mult: 129
    mod: 256
Returns:
    returns i (where mult * i % mod == 1) so 129 * 129 = 16641 % 256 = 1
    returns -1 if no number is found
"""


def mod_inverse(mult, mod):
    for i in range(0, mod):
        if (mult * i) % mod == 1:
            return i

    return -1


"""
Description: see ../text_files/hash_it_out.txt for description
    creates an empty arr of 0's
    
    process to isolate message[i]
    
    digest[i] = ((129 * message[i]) ^ message[i - 1]) % 256
        XOR both sides by message[i - 1] since XOR is opposite of XOR
    (digest[i] ^ message[i - 1]) = ((129 * message[i])) % 256
        let T = (digest[i] ^ message[i - 1]) SO
    (digest[i] ^ message[i - 1]) = (129 * message[i]) % 256
        multiply both sides by mod inverse of 129
        need to pass mod into mod_inverse() so mod_inverse(129, 256)
    ((digest[i] ^ message[i - 1]) * mod_inverse(129, 256)) % 256 = message[i]
        reverse
    message[i] = ((digest[i] ^ message[i - 1]) * mod_inverse(129, 256)) % 256
    
Args:
    digest: this is the passed 'hash' that needs 'decrypted'
Returns:
    returns decrypted message
Test Cases Used:
    [0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129]
    Expects [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]
    Expects [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
"""


def solution(digest):
    message = [0] * 16

    for i in range(0, len(message)):
        message[i] = (mod_inverse(129, 256) * (digest[i] ^ message[i - 1])) % 256

    return message
