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

operators = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y}
memory = 0


def main():
    while True:
        print(msg_0)
        x, operator, y = input().split()
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory

        try:
            x, y = float(x), float(y)
            lazy = check_lazy(x, y, operator)
            if operator == '/':
                v = x / y
        except ValueError:
            print(msg_1)
        except ZeroDivisionError:
            print(lazy)
            print(msg_3)
        else:
            if operator not in operators:
                print(msg_2)
            else:
                result = operators[operator](x, y)
                if lazy:
                    print(lazy)
                print(result)
                main_2(result)
                break


def main_2(result):
    while True:
        store = input(msg_4 + '\n')
        if store == 'y':
            sure = is_one_digit(result)
            if sure:
                global memory
                memory = result
                break
            else:
                break
        elif store == 'n':
            break

    while True:
        continue_ = input(msg_5 + '\n')
        if continue_ == 'y':
            main()
            break
        if continue_ == 'n':
            break


def check_lazy(x, y, operator):
    message = ''
    if ((-10 < x < 10) and (-10 < y < 10)) and (x.is_integer() and y.is_integer()) :
        message += msg_6
    if ((x == 1) or (y == 1)) and operator == '*':
        message += msg_7
    if ((x == 0) or (y == 0)) and operator in ['*', '+', '-']:
        message += msg_8
    if message != '':
        message = msg_9 + message
    return message


def is_one_digit(result):
    if (10 > result > -10) and result.is_integer():
        msg_ = {10: msg_10, 11: msg_11, 12: msg_12 }
        msg_index = 10
        while msg_index <= 12:
            answer = input(msg_[msg_index] + '\n')
            if answer == 'y':
                msg_index += 1
            if answer == 'n':
                return False
        return True
    return True


main()
