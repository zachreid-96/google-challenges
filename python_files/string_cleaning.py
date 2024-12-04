"""
Description: see ../text_files/string_cleaning.txt for description
    forward_remove: stores string with 'word' removed from 'chunk' looping forwards
    backward_remove: stores string with 'word' removed from 'chunk' looping backwards
    finds first/last index of 'word' in 'chunk' and sets respective var to everything before found index
        and everything after found index + the length of the word
    does this until no more indices are found within the stored var
    then checks (letter by letter) to see which one has the lowest ordinance

    if after forward/backward_remove is done processing, and they are "" (a null string)
        returns the original chunk ASSUMING that the passed word is "" (a null string)
        so for the example of ("aabb", "ab") I choose to return "aabb" but could return "ab" just as well
        Assuming description hints at if after cleaning the string is null then the word was "" # Could be wrong
Args:
    chunk: the jumbled string that needs cleaned by removed 'word'
    word: the word (or letter mess) the pirate inserted into 'chunk'
Returns:
    returns lexicographically the earliest word
Test Cases Used:
    "lololololo", "lol" # Expected return of 'looo'
    "goodgooogoogfogoood", "goo" # Expected return of 'dogfood'
    "aabb", "ab" # Expected return of 'aabb'
"""


def solution(chunk, word):

    forward_remove = chunk
    backward_remove = chunk

    while True:
        forward_temp = forward_remove
        f_index = forward_temp.find(word)
        if f_index >= 0:
            f = f_index + len(word)
            forward_remove = forward_temp[:f_index] + forward_temp[f:]

        backwards_temp = backward_remove
        r_index = backwards_temp.rfind(word)
        if r_index >= 0:
            r = r_index + len(word)
            backward_remove = backwards_temp[:r_index] + backwards_temp[r:]

        if f_index < 0 and r_index < 0:
            break

    if forward_remove == "" and backward_remove == "":
        return chunk

    x = 0
    while True:

        if x == len(forward_remove) and x > len(backward_remove):
            return forward_remove
        elif x == len(backward_remove) and x > len(forward_remove):
            return backward_remove
        elif x == len(forward_remove) and x == len(backward_remove):
            return forward_remove

        if ord(forward_remove[x]) < ord(backward_remove[x]):
            return forward_remove
        elif ord(forward_remove[x]) > ord(backward_remove[x]):
            return backward_remove
        elif ord(forward_remove[x]) == ord(backward_remove[x]):
            x += 1
    return


if __name__ == "__main__":

    print(solution("lololololo", "lol"))
    print(solution("goodgooogoogfogoood", "goo"))
    print(solution("aabb", "ab"))
