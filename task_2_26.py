def input_data():
    calc = []
    try:
        x = float(input('Введите значение первого аргумента: '))
        calc.append(x)
    except ValueError:
        print('Аргумент должен быть числом!')
        #exit()
        calculation(input_data())
    y = input('Введите действие "+", "-", "/", "*": ')
    if y == "+" or y == "-" or y == "/" or y == "*":
        calc.append(y)
    else:
        print('Действие введено не верно!')
        #exit()
        calculation(input_data())
    try:
        z = float(input('Введите значение второго аргумента: '))
        calc.append(z)
    except ValueError:
        print('Аргумент должен быть числом!')
        #exit()
        calculation(input_data())

    return calc


def calculation(calc):
    if calc[1] == "+":
        print(f'{calc[0]} + {calc[2]} = {calc[0] + calc[2]}')
        exit()
    elif calc[1] == "-":
        print(f'{calc[0]} - {calc[2]} = {calc[0] - calc[2]}')
        exit()
    elif calc[1] == "*":
        print(f'{calc[0]} * {calc[2]} = {calc[0] * calc[2]}')
        exit()
    elif calc[1] == "/":
        if calc[2] != 0:
            print(f'{calc[0]} / {calc[2]} = {calc[0] / calc[2]}')
            exit()
        else:
            print('На ноль делить нельзя!')
    #exit()
    calculation(input_data())

calculation(input_data())

# Задание достаточно интересное, вроде бы простое, но начинаешь думать как лучше сделать и уже получается две функции.
# Не могу сказать что быстро сделал, пришлось немного посидеть)
#
