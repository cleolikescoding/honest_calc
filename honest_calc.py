msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0.0


def is_one_digit(n):
    if (n > -10 and n < 10) and n.is_integer():
        return True
    else:
        return False


def check(a, op, b):
    msg = ""

    if is_one_digit(a) and is_one_digit(b):
        msg += msg_6
    if (a == 1 or b == 1) and (op == "*"):
        msg += msg_7
    if (a == 0 or b == 0) and (op != "/"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg

    print(msg)


# Do math


def calculations(x, oper, y):
    result = 0.0

    if oper == "+":
        result = (x + y)
    elif oper == "-":
        result = (x - y)
    elif oper == "*":
        result = (x * y)
    elif oper == "/":
        result = (x / y)
    print(result)

    return result

# Validate stuff


def validate(x, oper, y):
    result = False
    try:
        # Check if x and y are numbers
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
    else:
        # Check if operator is valid
        if oper not in "+-/*":
            print(msg_2)
        else:
            # Tests laziness
            check(x, oper, y)

            # Tests for division by zero
            if oper == "/" and y == 0:
                print(msg_3)
            else:
                result = True

    return result


running = True
while True:
    calc = input(msg_0)
    x, oper, y = calc.split()

    # Tests if operand use memory
    if x == "M":
        x = memory
    if y == "M":
        y = memory

    # Validates the equation
    if not validate(x, oper, y):
        continue

    # Does the calculation
    result = calculations(float(x), oper, float(y))

    print(msg_4)
    ans_1 = input()

    if ans_1 == "y":
        if is_one_digit(result):
            print(msg_10)
            ans_3 = input()
            if ans_3 == "y":
                print(msg_11)
                ans_4 = input()
                if ans_4 == "y":
                    print(msg_12)
                    if input() == "y":
                        memory = result
        else:
            memory = result

    print(msg_5)
    ans_2 = input()

    if ans_2 != "y":
        break
