"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Palantir.

A typical American-style crossword puzzle grid is an N x N matrix with black and white squares, which obeys the following rules:

Every white square must be part of an "across" word and a "down" word.
No word can be fewer than three letters long.
Every white square must be reachable from every other white square.
The grid is rotationally symmetric (for example, the colors of the top left and bottom right squares must match).
Write a program to determine whether a given matrix qualifies as a crossword grid.

Upgrade to premium and get in-depth solutions to every problem.

If you liked this problem, feel free to forward it along so they can subscribe here! As always,
shoot us an email if there's anything we can help with!
"""


def check_connected(x, y, crossword, visited):
    if x >= len(crossword) or x < 0 or y >= len(crossword) or y < 0:
        return 0

    if (x, y) in visited:
        return 0
    if crossword[x][y] == 1:
        visited.append((x, y))

        return (check_connected(x + 1, y, crossword, visited) +
                check_connected(x - 1, y, crossword, visited) +
                check_connected(x, y + 1, crossword, visited) +
                check_connected(x, y - 1, crossword, visited)) + 1
    return 0


def get_flat(crossword):
    new_list = []
    for row in crossword:
        new_list.extend(row)
    return new_list


def all_connected(crossword):
    y = None
    for index in range(len(crossword[0])):
        if crossword[0][index] == 1:
            y = index
    return check_connected(0, y, crossword, []) == sum(get_flat(crossword))


def valid_row(row):
    count = 0
    for square in row:
        if square == 1:
            count += 1
        else:
            if count < 3 and count != 0:
                return False
            count = 0
    if count < 3 and count != 0:
        return False

    return True


def is_symmetric(crossword):
    new_list = []
    for row in crossword:
        new_list.extend(row)
    reversed_list = list(new_list)
    reversed_list.reverse()

    return new_list == reversed_list


def is_valid_crossword(crossword):
    columns = [*zip(*crossword)]
    is_valid = True

    for row in crossword:
        is_valid = is_valid and valid_row(row)
    for column in columns:
        is_valid = is_valid and valid_row(column)

    is_valid = is_valid and is_symmetric(crossword)

    is_valid = is_valid and all_connected(crossword)

    return is_valid


def main():
    is_valid_crossword([
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
    ])

    # is_valid_crossword([[1, 0], [0, 1]])


if __name__ == '__main__':
    main()
