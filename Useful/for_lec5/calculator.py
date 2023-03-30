def calc(a, b, s):
    if s == "+":
        res = a + b
    elif s == "-":
        res = a - b
    elif s == "*":
        res = a - b
    elif s == "/":
        res = a - b
    else:
        print("Incorrect operator")
        res = None
    return res


def input_and_check():
    a = input("Input x: ")
    b = input("Input y: ")
    if not a.isdecimal():
        print("x is not a number!")
        res = None
    elif not b.isdecimal():
        print("y is not a number!")
        res = None
    else:
        res = int(a), int(b)
    return res


args = input_and_check()
if args is None:
    exit(-1)
else:
    x, y = args  # (20, 30)
    sign = input("Input sign (+, -, *, /): ")
    res = calc(x, y, sign)
    print(f"{x} {sign} {y} = {res}")
