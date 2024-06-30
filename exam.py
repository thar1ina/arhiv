import random
# # 1
# a = ('Hello world')
# s = a[::-1]
# print(s)




# # 2
# a = [10, 15, 20, 25, 50, 55, 100, 111, 122]
# b = list(filter( lambda x: x % 2 == 0, a))
# print(b)
#
#
#
#
#
# # 3
# a = random.randrange(1, 5)
# ss = 0
# while 1 == 1:
#     b = int(input('num:'))
#     ss += 1
#     if a > b:
#         s = a - b
#         print('Меньше',a ,'на ', s)
#         continue
#     elif a < b:
#         f = b - a
#         print('Больше',a ,'на', f)
#         continue
#
#     elif a == b:
#        n = input(f'Вы угадали за {ss} попыток. Хотите ли вы продолжить?')
#        if n == 'Да':
#            continue
#        else:
#            print('Спасибо за игру')
#            break


# 4



# def d (*args):
#     s =  sum(args)
#     print(s)
#
#
# a = [10, 15, 20, 25, 50, 55, 100, 111, 122]
# d(*a)




# 5

# def func(*args):
#     d = []
#     for i, j in args:
#         s = i ** j
#         d.append(s)
#     print(d)
#
# a = [[2, 3] ,[4, 5], [3, 4]]
# func(*a)




# # 6
# t = [1, 2, 3, 4, 5, 6, 7, 8]
# reversed = False
#
# if not reversed:
#     t.reverse()
#     print(t)
# else:
#     print(t)





# 7
# d = int(input('num:'))
# for i in range(100):
#
#     if d >= 0 and d <= 21 or d >= 57 and d <= 100:
#         print("Число разрешено")
#         break
#     else:
#         print("Число запрещено")
#         break

# 8

# i = 0
# while i < 100:
#     n = 1
#     i += n
#     print(i)



# 9
#
# for i in range(1, 10 + 1):
#     if i >= 1 and i < 7 or i >= 8 and i <= 10:
#         print(i)