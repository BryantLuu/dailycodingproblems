"""
This problem was asked by Facebook.

Given a list of integers L, find the maximum length of a sequence of consecutive numbers that can be formed using elements from L.

For example, given L = [5, 2, 99, 3, 4, 1, 100], return 5 as we can build a sequence [1, 2, 3, 4, 5] which has length 5.
"""


def get_max_sequence(nums):
    nums.sort()
    current_num = nums[0]
    max_length = 1
    length = 1
    for num in nums[1:]:
        if num == current_num + 1:
            length += 1
        else:
            length = 1

        if length > max_length:
            max_length = length

        current_num = num

    return max_length


def main():
    print(get_max_sequence([5, 2, 99, 3, 4, 1, 100]))


if __name__ == "__main__":
    main()
