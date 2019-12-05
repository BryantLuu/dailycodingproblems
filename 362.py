"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""


def find_strobogrammatic(n):
    strob_nums = {
        '1': '1',
        '8': '8',
        '6': '9',
        '9': '6',
    }
    half_index = int(n / 2)
    seed_list = ['1', '8', '6', '9']
    for _ in range(half_index - 1):
        new_list = []
        for i in seed_list:
            for strob in strob_nums:
                new_list.append(i + strob)
        seed_list = new_list
    solutions = ['' for n in range(len(seed_list))]
    index = 0
    for num in seed_list:
        for char in range(len(num) - 1, -1, -1):
            solutions[index] = solutions[index] + strob_nums[num[char]]
        index += 1

    return_list = []
    if n % 2:
        for i in range(len(solutions)):
            return_list.append(seed_list[i] + '1' + solutions[i])
            return_list.append(seed_list[i] + '8' + solutions[i])
    else:
        for i in range(len(solutions)):
            return_list.append(seed_list[i] + solutions[i])
    return return_list


def main():
    # find_strobogrammatic(2)
    # print(find_strobogrammatic(3))
    # print(find_strobogrammatic(4))
    print(find_strobogrammatic(5))
    return


if __name__ == '__main__':
    main()
