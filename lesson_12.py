# x = [2, 33, 22, 2, 5, 22, 22, 22, 7]
# d = set(x)
# print(type(d))
# print(d)


# a = {'qwerty', True, False, (1, 2, 5, 9), 3.4}
# print(a)

# a = {1, 3,1, 5, 1, 3, 2, 2}
# print(a)

# a = 'hello'
# s = set(a)
# print(s)

# a = {1, 3, 1, 5, 1, 3, 2, 2}
# a.add(10)
# a.add('qwerty')
# a.add((1,2,3))
# print(a)

# a = {1, 3, 1, 5, 1, 3, 2, 2}
# print(a)
# a.pop()
# a.pop()
# a.pop()
# a.pop()
# a.pop()
# print(a)


# a = {1, 3, 1, 5, 1, 3, 2, 2}
# a.clear()
# print(a)


# a = {1, 3, 1, 5, 1, 3, 2, 2}
# b = {2, 3, 4, 10, 11}
# s = a.difference(b)
# print(s)



# a = {1, 3, 1, 5, 1, 3, 2, 2}
# a.update([11,22,33])
# a.add(11)
# a.add(22)
# a.add(33)
# print(a)


# a = {1, 2, 3, 4, 5}
# a.discard(1)
# print(a)

# a = {1, 2, 3, 4, 5}
# a.remove(11)
# print(a)

# a = {1, 2, 3, 4, 5}
# print(len(a))


# a = {1, 2, 3, 4, 5}
# for i in range(len(a)):
#     print(i)

# a = {'hello', 'hi', 'how are you', 'hello'}
# print(a)

#
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# l = set1.isdisjoint(set2)
# print(l)


# set{}
# [], '', (), {}

# d = {1, 2, 3, 1, 4, 5, 6}
# print(d)


# x = [2, 33, 22, 2, 5, 22, 22, 7]
# d = set(x)
# print(type(d))
# print(d)

# d = {2, 3, 1, 4, 5, 6}
# f = d.pop()
# print(d)

# r = {'apple', 'banana', 'qiwi', 'apelsin'}
# print(r)


# r = {'apple', 'banana', 'limon', 'qiwi', 'apelsin'}
# d = r.pop()
# print(r)

# r = {'apple', 'banana', 'qiwi', 'apelsin'}
# d = r.clear()
# print(r)

# r = {'apple', 'banana', 'qiwi', 'apelsin'}
# d = r.clear()
# print(r)

# r = {'apple', 'banana', 'qiwi', 'apelsin'}
# d = r.copy()
# print(d)

# r = {'apple', 'banana', 'qiwi', 'apelsin'}
# d = r.add('limon')
# print(r)

# r = {'apple', 'banana', 'qiwi', 'apelsin'}
# d = r.remove('apple')
# print(r)

# r = {'apple', 'banana', 'qiwi', 'apelsin'}
# for i in r:
#     print(i, end=' ')

# r = {'apple', 'banana', 'qiwi', 'apelsin'}
# for i in r:
#     print(i, end=' ')

# r = {'apple', 'banana', 'qiwi', 'apelsin'}
# for i in r:
#     if i == 'banana':
#         break
#     print(i)








# 1
#
# x = {5, 4, 6, 7, 5, 4, 2}
# y = {5, 4, 3, 4, 5, 3, 2}
# print(x, y)


#
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# a = farm_1.isdisjoint(farm_2)
# print(a)
# #



# set2 = {3, 4, 5, 6, 7}
# set3 = {5, 6, 7, 8, 9}
# s = set2.intersection(set3)
# print(s)
# #

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# set3 = {5, 6, 7, 8, 9}
# a = set1.intersection(set2, set3)
# print(a)

# numbers = [1, 2, 3, 2, 4, 5, 3]
# print(len(numbers))
#
#
# numbers = [1, 2, 3, 2, 4, 5, 3]
# a = set(numbers)
# print(a)

# #
# a = {1, 2, 3}
# b = {2, 3, 4}
# s = a.update(b)
# print(s)
# #
# #
# a = {1, 2, 3}
# b = {2, 3, 4}
# x = a.difference(b)
# y = b.difference(a)
# print(x, y)
# #

# a = {1, 2, 3}
# b = {2, 3, 4}
# x = a.difference(b)
# y = b.difference(a)
# print(x, y)



#
# a = int(input('num:'))
# # for i in a:
# if (a == a[::-1]):
#     print(f'a[1]')
#
# # a = 1, 2, 3, 4
# print(a[-1])