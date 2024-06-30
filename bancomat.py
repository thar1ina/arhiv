# try-except
import time

# try:
#     x = 5
#     y = 1
#     print(x / y)
# except Exception as j:
#     print('domoy', j)
# else:
#     print('else ishtedy')
# finally:
#     print('finally ishtedy')

    # x = 5
    # y = 4
    # print(x + y)



# try:

#     a = int(input('Введите номер:'))
#     b = int(input('Введите сумму:'))
#     print('Успешно пополнена')
#
# except Exception:
#     print('Попробуйте ещё раз')
# # else:
# #     print('Минимум 5 сом')
# finally:
#     print('Спасибо за обращение')


# 1-variant
# try:
#     while True:
#         import datetime as dtt
#         q = input('Выберите язык:')
#         time.sleep(1)
#         if q == ('Кыргызский'):
#             print('Кош келиниз')
#             rr = input('Ф.И.О.:')
#             time.sleep(1)
#             tt = int(input('Картаныздагы каражат:'))
#             time.sleep(1)
#             ss = int(input('Пин кодту териниз:'))
#             time.sleep(1)
#             if ss > 9999 or ss < 9999:
#                 print('Пин код туура эмес')
#                 continue
#             elif ss == 9999:
#                 xx = [200, 500, 1000, 5000, tt]
#             print(xx)
#             bb = int(input('Сумманы жазыныз:'))
#             time.sleep(2)
#             if tt < bb:
#                 print('Каражатыныз жетишсиз')
#                 continue
#             elif tt >= bb:
#                 print('Акчанызды алыныз')
#                 time.sleep(2)
#         elif q == ('Русский'):
#             print('Добро пожаловать!')
#         else:
#             print('error')
#             continue
#         r = input('Ф.И.О.:')
#         time.sleep(1)
#         t = int(input('Cумма на карте:'))
#         time.sleep(1)
#         s = int(input('Введите пин код:'))
#         time.sleep(1)
#         if s > 9999 or s < 9999:
#             print('Неправильный пин код')
#             continue
#         elif s == 9999:
#          x = [200, 500, 1000, 5000, t]
#         print(x)
#         b = int(input('Выберите действие:'))
#         time.sleep(2)
#         if  t < b:
#             print('Недостаточно средств')
#             continue
#         elif t >= b:
#             print('Возьмите деньги')
#             time.sleep(2)
#         def func(g):
#                 if g == 'Да':
#                     print(r,
#                                '| Общая сумма на карте', t , 'сом',
#                                 ' | Осталось', t-b, 'сом',dtt.datetime.now())
#
#         v = input(f'Нужен ли вам чек?   1) Да    2) Нет:')
#         func(v)
#         break
#
# except Exception:
#     print('Попробуйте ещё раз')
#
#
#
# finally:
#     print('Спасибо за обращение')


try:
    while True:
        import datetime as dtt
        q = input('Выберите язык:')
        time.sleep(1)
        if q == ('Кыргызский'):
            print('Кош келиниз!')
            rr = input('Ф.И.О.:')
            time.sleep(1)
            tt = int(input('Картаныздагы каражат:'))
            time.sleep(1)
            def p(pas):
                return pas.isdigit() and len(pas) == 4
            a = input("Пин кодту териниз: ")
            if p(a):
                print("Туура")
            else:
                print("Туура эмес.")
            time.sleep(1)
            x = [200, 500, 1000, 5000]
            x.append(tt)
            print(x)
            def numb(num):
                return num % 100 == 0 and num % 240 != 0 and num < 10000
            number2 = int(input("Сумманы жазыныз мак.10мин.: "))
            time.sleep(1)
            if numb(number2):
                print("Акчаны алыныз")
                time.sleep(2)
            else:
                print("Кайра кайталап корунуз")
                break
            def func(gg):
                if gg == 'Ооба':
                    print(rr,
                          '| Суммадагы каражат', tt, 'сом',
                          ' | Калдыгы', tt - number2, 'сом', dtt.datetime.now())


            v = input(f'Чек керекпи?   1) Ооба    2) Жок:')
            func(v)
            break
        elif q == ('Русский'):
            print('Добро пожаловать!')
        else:
            print('error')
            continue
        r = input('Ф.И.О.:')
        time.sleep(1)
        t = int(input('Cумма на карте:'))
        time.sleep(1)
        def p(pas):
            return pas.isdigit() and len(pas) == 4

        a = input("Пин код: ")
        if p(a):
                print("Принят")
        else:
                print("Попробуйте снова.")
        time.sleep(1)
        x = [200, 500, 1000, 5000]
        x.append(t)
        print(x)
        def numb(num):
            return num % 100 == 0 and num % 240 != 0 and num < 10000

        number = int(input("Введите сумму мак.10тыс.: "))
        time.sleep(1)
        if numb(number):
            print("Возьмите деньги")
            time.sleep(2)
        else:
            print("Не удалось совершит операцию")
            continue
        def func(g):
            if g == 'Да':
                print(r,
                             '| Общая сумма на карте', t , 'сом',
                                ' | Осталось', t - number, 'сом',dtt.datetime.now())

        v = input(f'Нужен ли вам чек?   1) Да    2) Нет:')
        func(v)
        break

except Exception:
    print('Попробуйте ещё раз')



finally:
    print('Спасибо за обращение!')
