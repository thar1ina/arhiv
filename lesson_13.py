# dict{}-dictionary - cловарь
#         / \
#     KEY  |  ValueError


# a = {'name': 'Samat', 'age': 22, 'salary': 40000}
# d = a.clear()
# print(a)


# a = {1, 2, 3, 4, 56}
# print(type(a))

# a = {'name': 20}
# print(type(a))

# a = {}
# print(type(a))

# a = {'name': 'Samat', 'age': 22, 'salary': 40000}
# d = a.copy()
# print(d)

# a = {'name': 'Samat', 'age': 22, 'salary': 40000}
# d = a.pop('salary')
# print(a)

# a = {'name': 'Samat', 'age': 22, 'salary': 40000}
# f = {'rost': 160}
# d = a.update(f)
# print(a)

# a = {'name': 'Samat', 'age': 22, 'salary': 40000}
# d = a.get('salary')
# print(d)

# a = {'name': 'Samat', 'age': 22, 'salary': 40000}
# d = a.values()
# print(d)

# a = {'name': 'Samat', 'age': 22, 'salary': 40000}
# d = a.keys()
# print(d)

# a = {'name': 'Samat', 'age': 22, 'salary': 40000}
# d = a.items()
# print(d)


# a = {'name': 'Samat', 'salary': 40000,'age': 22}
# d = a.popitem()
# print(a)


# a = {'name': 'Samat', 'salary': 40000,'age': 22}
# d = a.fromkeys('salary')
# print(d)

# a = {'name': 'Samat', 'salary': 40000,'age': 22}
# d = a.setdefault('salary')
# print(d)


# a = {'name': 'Samat', 'salary': 40000,'age': 22}
# for i in a.keys():
#     print(i)

# a = {'name': 'Samat', 'salary': 40000,'age': 22}
# for i in a.values():
#     print(i)

# a = {'name': 'Samat', 'salary': 40000,'age': 22}
# for i in a.items():
#     print(i)

# a = {'name': 'Samat', 'salary': 40000,'age': 22}
# for i,j in a.items():
#     print(i, j)

# a = {'name': 'Samat', 'salary': 40000,'age': 22}
# for i, j in a.items():
#     if j == 40000:
#         print(i,j)
#     else:
#         print('asdnjadsnf')




               # 1
# students = {'Alice': 90, 'Samat': 55, 'Asel': 78, 'Bob': 69, 'David': 34}
# a = students.get('Alice')
# print(a)

# students = {'Alice': 90, 'Samat': 55, 'Asel': 78, 'Bob': 69, 'David': 34}
# a = {'Eve': 92}
# b = students.update(a)
# print(students)

# students = {'Alice': 90, 'Samat': 55, 'Asel': 78, 'Bob': 69, 'David': 34}
# a = {'Bob': 88}
# b = students.update(a)
# print(students)

#
students = {'Alice': 90, 'Samat': 55, 'Asel': 78, 'Bob': 69, 'David': 34}
a = {'Charlie'}
b = students.fromkeys(a)
print(b)

# students = {'Alice': 90, 'Samat': 55, 'Asel': 78, 'Bob': 69, 'David': 34}
# a = students.pop('David')
# print(students)


# students = {'Alice': 90, 'Samat': 55, 'Asel': 78, 'Bob': 69, 'David': 34}
# a = students.items()
# print(a)


# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# a = {'besh_barmak': 130}
# s = menu.update(a)
# b = {'lagman': 135}
# d = menu.update(b)
# c = menu.pop('borsh')
# print(menu)


# a = {'apple': 35, 'banana': 160, 'cherry': 250, 'qiwi': 150}
# summ = 0
# for i in a.values():
#     summ += i
#     print(summ)



# a = {'apple': 35, 'banana': 160, 'cherry': 250, 'qiwi': 150}
# keys = list(a)
# index = 0
# while index<len(keys):
#     print(keys[index])
#     index += 1

#
# a = {'apple': 35, 'banana': 160, 'cherry': 250, 'qiwi': 150}
#     while True:
#         print(a.values())
#         break


#  a = {'apple': 35, 'banana': 160, 'cherry': 250, 'qiwi': 150}
# #     while True:
# #         print(a)
# #         break


# a = {'apple': 35, 'banana': 160, 'cherry': 250, 'qiwi': 150}
# while True:
#     if a.values() == 150:
#         print()
#         break
#     else:
#         print(' ')
#         break



# students = {'Bob': 34, 'Alice': 90, 'Samat': 95, 'Asel': 78, 'Bob': 69, 'David': 100, 'Saadat': 94, 'Xasan': 98,}
# d =[]
# for i,j in students.items():
#     if j >= 90:
#         d.append(i)
# print(d)

# a = {'1': 18, '2': 12, '3': 10, '4': 19, '5': 17 }
# summ = 0
# x = 18
# for i,j in a.items():
#     if j < 18:
#         print(i, f'  Набор на {x-j} учеников')
#     elif j > 18:
#         print(i,f'Исключаем {j-x} учеников')
#     elif j == 18:
#         print(i,'Заполнено')

