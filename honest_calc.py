msg_0 = "Enter an equation"
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
memory = 0


def is_one_digit(v):
    if (-10 < v < 10) and v.is_integer():
        return True
    else:
        return False


def ask_to_continue():
    while True:
        print(msg_5)
        answer = input()
        if answer != 'n' and answer != 'y':
            continue
        elif answer == 'y':
            return True
        else:
            return False


def ask_to_store():
    global memory
    global result
    answer_continue = False
    while True:
        print(msg_4)
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(eval(f"msg_{msg_index}"))
                    answer_sure = input()
                    if answer_sure == 'n':
                        break
                    elif answer_sure == 'y':
                        if msg_index < 12:
                            msg_index += 1
                        else:
                            memory = result
                            break
                    else:
                        continue
            else:
                memory = result
            answer_continue = ask_to_continue()
            break
        elif answer == 'n':
            answer_continue = ask_to_continue()
            break
        else:
            continue
    if answer_continue:
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg:
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    if oper in ['+', '-', '*', '/']:
        check(x, y, oper)
        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif y != 0:
            result = x / y
        else:
            print(msg_3)
            continue
        print(result)
        if ask_to_store():
            continue
        else:
            break
    else:
        print(msg_2)
        continue
