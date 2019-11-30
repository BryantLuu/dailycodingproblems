"""
This problem was asked by Google.

You are given a series of arithmetic equations as a string, such as:

y = x + 1
5 = x + 3
10 = z + y + 2
The equations use addition only and are separated by newlines.
Return a mapping of all variables to their values.
If it's not possible, then return null. In this example, you should return:

{
  x: 2,
  y: 3,
  z: 5
}
"""


def getCount(equ):
    count = 0
    for e in equ.split(' '):
        if e not in ('=', '+') and not e.isnumeric():
            count += 1
    return count


def getVariables(equations):
    variables = {}
    solved_variable_count = 0
    fail_twice = False
    prev_solved_variable_count = 0
    while not fail_twice:
        for equ in equations:
            replaceEqu = equ.replace('', '')
            for key, var in variables.items():
                replaceEqu = equ.replace(key, str(var))
            count = getCount(replaceEqu)
            if count > 1 or count == 0:
                continue
            else:
                before_equal = True
                numbers = []
                flip = False
                var = None
                for char in replaceEqu.split(' '):
                    if char == '=':
                        before_equal = False
                        continue
                    if before_equal and char.isnumeric():
                        numbers.append(int(char) * -1)
                    if not before_equal and char.isnumeric():
                        numbers.append(int(char))
                    if before_equal and not char.isnumeric() and char not in (
                            '=', '+'):
                        var = char
                    if not before_equal and not char.isnumeric(
                    ) and char not in ('=', '+'):
                        var = char
                        flip = True
                if var in variables:
                    continue
                if flip == True:
                    variables[var] = sum(numbers) * -1
                else:
                    variables[var] = sum(numbers)
                solved_variable_count += 1
        if solved_variable_count == prev_solved_variable_count:
            fail_twice = True
        prev_solved_variable_count = solved_variable_count
    return variables


def main():
    foo = """y = x + 1
5 = x + 3
10 = z + y + 2"""
    equations = []
    for line in foo.splitlines():
        equations.append(line)
    print(getVariables(equations))
    return


if __name__ == "__main__":
    main()
