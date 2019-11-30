"""
This problem was asked by Amazon.

Write a function that takes a natural number as input and returns the number of digits the input has.

Constraint: don't use any loops.
"""


def digits_count(num):
    return len(str(num))


def main():
    assert digits_count(55) == 2
    print('yay')


if __name__ == "__main__":
    main()
