"""
Description: see ../text_files/escape_pods.txt for description
    dynamically moves the bunnies through various doors to the escape pods
    takes 'path' and breaks it into 'entries', 'pathways', 'exits_ways' for ease of understanding
    entries: the arrs of 'path' that are designated entrances
    pathways: the arrs of 'path' not designated entrances or exits
    exit_ways: the arrs of 'path' designated exits

    Operation:
    loops through 'entries' and checks values of bunnies and designated door in 'pathways'
        if bunnies <= door -> passes full bunny count
        if bunnies > door -> passes bunny count equal to door
    loops through 'pathways' and checks values of bunnies and designated doors (if any) further down the hallway
        if bunnies <= door -> passes full bunny count
        if bunnies > door -> passes bunny count equal to door
    when end of pathways is done, create new var 'bunnies_ready_to_escape'
    bunnies_ready_to_escape: the arrs of 'pathways' that still have bunny values
    loops through 'bunnies_ready_to_escape' and checks values of bunnies and exit doors (if applicable)
        if bunnies <= door -> adds full bunny value to bunnies_saved var
        if bunnies > door -> adds door value to bunnies_saved var

    so for path [[0, 4, 6], [4, 0, 4], []]
        a condensed_path would look like [[4, 6], [4, 4], []]
        so values are checked like this [[4*00, 6*01], [4*00, 6*01], []]
        where *00 represents the [][] source of bunnies
        so that would then be [[4, 4], [4, 4], []]
        I turn the source to 0's to avoid confusion -> [[0, 0], [4, 4], []]

    If exit == [] assumed all bunnies are able to pass (see description text for test case #2

    tried to test some edge cases, but assuming only valid path arrs are passed (not testing all edge cases)
Args:
    entrances: rooms currently containing bunnies
    exits: rooms between bunnies and escape pods
    path: 'matrix' of entire layout
Returns:
    returns int value of how many bunnies can make it safely to the escape pods
    **based on description, assumed once a doorway is used it 'closes' and cannot be used again**
Test Cases Used:
    Entrances: [0]
    Escape Pods: [3]
    Path: [[0, 7, 0, 0],
           [0, 0, 6, 0],
           [0, 0, 0, 8],
           [9, 0, 0, 0]]
    Expected output of 6

    Entrances: [0, 1]
    Escape Pods: [4, 5]
    Path: [[0, 0, 4, 6, 0, 0],
           [0, 0, 5, 2, 0, 0],
           [0, 0, 0, 0, 4, 4],
           [0, 0, 0, 0, 6, 6],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]
    Expected output of 16

    Entrances: [0, 1, 2]
    Escape Pods: [9, 10, 11]
    Path: [[0, 0, 12, 8, 6, 0],
           [0, 13, 8, 5, 0, 0],
           [0, 6, 8, 5, 0, 0],
           [0, 5, 0, 0, 5, 4],
           [0, 0, 5, 0, 6, 6],
           [5, 0, 6, 0, 0, 6],
           [5, 0, 6, 0, 6, 0],
           [5, 0, 6, 0, 0, 6],
           [5, 0, 6, 0, 6, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]
    Expected output of 46

    Entrances: [0]
    Escape Pods: [1]
    Path: [[0, 7, 0, 0],
           [9, 0, 0, 0]]
    Expected output of 6
"""


def solution(entrances, exits, path_matrix):

    condensed_path = [[] for _ in range(len(path_matrix))]

    for row in range(len(path_matrix)):
        for col in range(len(path_matrix[row])):
            if path_matrix[row][col] != 0:
                condensed_path[row].append(path_matrix[row][col])

    bunnies_saved = 0

    entries = condensed_path[:len(entrances)]
    pathways = condensed_path[len(entrances):len(path_matrix) - len(exits)]
    exit_ways = condensed_path[len(path_matrix) - len(exits):]

    print(entries)
    print(pathways, '\n')
    if pathways:
        for entry in range(len(entries)):
            for bunny in range(len(entries[entry])):
                if entries[entry][bunny] <= pathways[bunny][entry]:
                    pathways[bunny][entry] = entries[entry][bunny]
                    entries[entry][bunny] = 0
                elif entries[entry][bunny] > pathways[bunny][entry]:
                    entries[entry][bunny] = 0
    elif not pathways:
        pathways = entries

    print(entries)
    print(pathways, '\n')

    path_interval = len(entries)

    print(f"Path_interval: {path_interval}")

    if len(pathways) - len(entries) > 0:
        for path in range(path_interval):
            for bunny in range(len(pathways[path])):
                if pathways[path][bunny] <= pathways[bunny+path_interval][path]:
                    pathways[bunny+path_interval][path] = pathways[path][bunny]
                    pathways[path][bunny] = 0
                elif pathways[path][bunny] > pathways[bunny+path_interval][path]:
                    pathways[path][bunny] = 0

    print(entries)
    print(pathways, '\n')

    bunnies_ready_to_escape = pathways[-path_interval:]

    print(bunnies_ready_to_escape)
    for room in range(len(bunnies_ready_to_escape)):
        for bunny in range(len(bunnies_ready_to_escape[room])):
            print(f"room: {room} | bunny: {bunny}")
            if not exit_ways[bunny]:
                bunnies_saved += bunnies_ready_to_escape[room][bunny]
                bunnies_ready_to_escape[room][bunny] = 0
            elif bunnies_ready_to_escape[room][bunny] <= exit_ways[bunny][room]:
                bunnies_saved += bunnies_ready_to_escape[room][bunny]
                bunnies_ready_to_escape[room][bunny] = 0
            elif bunnies_ready_to_escape[room][bunny] > exit_ways[bunny][room]:
                bunnies_saved += exit_ways[bunny][room]
                bunnies_ready_to_escape[room][bunny] = 0

    #print(bunnies_ready_to_escape)

    return bunnies_saved
