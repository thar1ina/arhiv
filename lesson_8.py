# c = input('a:')
# if len(c) <= 5:
#     print(c)
# elif len(c) > 5:
#     d = (c[0:1])
#     i = (c[-1])
#     s = str(len(c) - 2)
#     print(d + s + i)


while True:
    pas = input("Введите пароль: ")

    if len(pas) < 8:
        print("Короткий!")
        continue

    elif pas.isdigit():
        print("Ошибка")
        continue

    elif pas.isalpha():
        print("Ошибка")
        continue

    elif  pas.isalnum():
        print("Ошибка")
        continue

    elif "123" in pas or "abs" in pas:
        print("Нельзя повторять!")
        continue

    else:
        print("Надежный пароль")
    break