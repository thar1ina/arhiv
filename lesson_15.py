# def func(*args):
#     summ = 0
#     for i in args:
#         summ += i
#     print(summ)
#
# func(3, 5, 5, 10)
#

# def sum_1(x, y):
#     print(x + y)
# sum_1(5,6)


# def sum_1(x, y):
#     return x + y
# print(sum_1(5,6))


# a = [1, 2, 3, 4, 5]
# for i in a:
#     print(i, end='\t')


# for i in range(20):
#     print(i)


# def func(n):
#     for i in range(n+1):
#         if i % 2 != 0:
#             print(i)
#
# func(100)


# *arqs, **kwarqs

# def func(*args):
#     return args
#
#
# print(func(4, 5, 6, 'hi', [2, 5, 6]))


# def func(**kwargs):
#     for i,j in kwargs.items():
#         if i == 'age':
#             print(i,j)
#
#
# print(func(name='John', age=23, salary=40000))

# def func(**kwargs):
#     for i,j in kwargs.items():
#         if str(j) >= '35000':
#             print(j)
# func(name ='John', age = 23, salary= 40000)


# def func(*args):
#     for i in args:
#         print(i)
#
#
# print(func(2, 3, 4, 5, 6))

# def func(**kwargs):
#     # return type(kwargs)
#     for i, j in kwargs.items():
#         print(i, j)
#
#
# print(func(name='Deniz', age=23, salary=10000))

# def func(*args, **kwargs):
#     return args, kwargs
#
#
# print(func(2,3,4, a = 2, b = 3, c = 4))


# def func(y, a=5):
#     return a + y
#
#
# print(func(3, 4))

# a = (2,3,4,5,6)
#
# d = list(a)
# print(d)





#
# def func(name, salary = 5000):
#     return f'{name} - {salary}'
#
# print(func('Samat', 7000))



#
# def func (*args, **kwargs):
#     d = [args,kwargs]
#     return d
# print(func(1,2,3 , Sasha = 2300))



# 1
# def func(**kwargs):
#     return kwargs
#
#
# print(func(Asan=67, Alica=88, Samat=99))

# 2
# def func(students, rating):
#     return f'{students} - {rating}'
# print(func('Alice', 90))

# 3

# def func(students, rating,x, y ):
#     return f'{students} - {rating}, {x} - {y}'
# print(func('Alice', 90,'Eve', 92))

# 4
# def func(students , rating = 69):
#     return f'{students} - {rating}'
# print(func('Bob', 88))


# 5
# def func(**kwargs):
#     a ={'Charlie'}
#     return kwargs.fromkeys(a)
# print(func(Alice = 90, Samat= 55, Asel= 78))

# 6
def func(**kwargs):
    a = {'David'}
    return kwargs.pop(a)

print(func(Alice = 90, Samat= 55, Asel= 78, David=34))







# 7
# def func(**kwargs):
#     return kwargs.items()
# print(func(Alice = 90, Samat= 55, Asel= 78))








# def menu (**kwargs):
#     a = {'besh-barmak = 130'}
#     return kwargs.items(), kwargs.update(a)
#
#
#
#
# print(menu(lagman = 120, plov=120, borsh=100 ))
#
#

 # menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# a = {'besh_barmak': 130}
# s = menu.update(a)
# b = {'lagman': 135}
# d = menu.update(b)
# c = menu.pop('borsh')
# print(menu)



