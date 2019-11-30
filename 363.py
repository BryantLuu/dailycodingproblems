"""
This problem was asked by Squarespace.

Write a function, add_subtract, which alternately adds and subtracts curried arguments. Here are some sample operations:

add_subtract(7) -> 7

add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0

add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11
"""


def add_subtract(value):
    total = value
    plus = True

    def _add_subtract(value):
        nonlocal plus
        nonlocal total
        if plus:
            total += value
        else:
            total -= value

        plus = False
        return _add_subtract

    return _add_subtract


def main():
    add_subtract(1)(2)(3)


if __name__ == '__main__':
    main()
