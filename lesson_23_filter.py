# a = [1, 3, 5, 6, 8, 10, 22, 240]
# d = []
# for i in a:
#     if i % 2 == 0:
#         d.append(i)
# print(d)


# def func(x):
#     return x % 2 == 0
#
# def func_2(x):
#     return x % 2 != 0
#
#
# a = [1,2, 3, 5, 6, 8, 10, 22, 240]
# b = list(filter(func, a))
# d = list(filter(func_2, a))
# print(b)
# print(d)


# def s(x):
#     return x % 3 == 0 and x % 2 == 0
#
#
# a = [1, 2, 5, 6, 8, 9, 10, 22, 240]
# b = list(filter(s, a))
# print(b)

#
# a ='hello4234243'
# b = list(filter(str.upper, a))
# print(b)


# def f(x):
#     return x
#
# a = {'Bishkek': +996, 'Moskva': +8, 'Kazakstan': +7, 'Uzbekistan': +998}
# b = dict(filter(f, a.items()))
# print(b)


# a = {"bishkek": 996,
#      "moscwa": +7,
#      "ozbekistan": +998,
#      "kazaxstan": +77}
# s = a.items()
# s = set(filter(lambda x: dict, s))
# print(s)


# a = ['hello', 12, False, 'hi',True, 'how are you', {1, 2}, [3, 4]]
# b = list(filter(lambda x: isinstance(x, int), a))
# print(b)





# a = ["app",
#      'orange',
#      "banana",
#      'strawberry',
#      "cherry",
#      "paya",
#      "mango",
#      "waterlemon",
#      "lemn",
#      "limon"]
# s = list(filter(lambda z: len(z) >= 5, a))
# print(s)

# a = ["app",
#      'orange',
#      "banana",
#      'strawberry',
#      "cherry",
#      "paya",
#      "mango",
#      "waterlemon",
#      "lemn",
#      "limon"]
#
#
# def fruit(x):
#     if x == 'banana':
#         return x
#
#
# def fruit_2(x):
#     if x != 'banana':
#         return x
#
#
# b = list(filter(fruit, a))
# print(b)
#
# dd = list(filter(fruit_2, a))
# print(dd)


# a = ['enter your name ', [56, 67], {123}, '456', False, True, 'how do you do']
# b = {x for x in a if type(x) == bool}
# print(b)



# Задача_1: Выберите только положительные числа из списка.
#
# Задача_2: Отфильтруйте строки, которые содержат более 5 символов.
#
# Задача_3: Выберите только четные числа из списка.
#
# Задача_4: Отфильтруйте строки, которые содержат букву 'a'.
#
# Задача_5: Выберите только элементы списка, которые больше 10.
#
# Задача_6: Создайте функцию, которая фильтрует строки, начинающиеся с определенной буквы.
#
# Задача_7: Создайте новый словарь, включая только пары ключ-значение, где значение больше 5.