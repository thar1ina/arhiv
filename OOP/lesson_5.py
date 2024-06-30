# a = [1, 2, [4, 7], [9, 11, [8,1,22]]]
# print(a[3][2][2])

# class Chocolate:
#     def __init__(self ,a):
#         self.a = a
#
#
#     def ch(self):
#         p = 3.14
#         return p * self.a // 2
#
# a = Chocolate(23)
# print(a.ch())



# b = lambda x: x * 3.14 // 2
# print(b(23))


# import math
#
# def distance(x1, y1, x2, y2):
#     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#
# # Считываем количество вершин многоугольника
# N = int(input())
#
# # Считываем координаты вершин
# vertices = []
# for _ in range(N):
#     x, y = map(float, input().split())
#     vertices.append((x, y))
#
# # Находим центральную точку многоугольника (среднее арифметическое координат)
# center_x = sum(vertex[0] for vertex in vertices) / N
# center_y = sum(vertex[1] for vertex in vertices) / N
#
# # Находим наименьшую длину линии разлома
# min_distance = float('inf')
# for i in range(N):
#     x1, y1 = vertices[i]
#     x2, y2 = vertices[(i + 1) % N]
#     dist = distance(x1, y1, x2, y2)
#     dist1 = distance(center_x, center_y, x1, y1)
#     dist2 = distance(center_x, center_y, x2, y2)
#     area = abs((x1 - center_x) * (y2 - center_y) - (x2 - center_x) * (y1 - center_y)) / 2
#     if abs(area - 0.5 * dist1 * dist2) < 1e-6:
#         min_distance = min(min_distance, dist)
#
# print(round(min_distance, 4))





# s = int(input('cm:'))
# a = int(input('cm:'))
# b = int(input('cm:'))
#
# d = list(map(lambda s, a, b: if a == b == s while True: elif a != s != b ))
# print(d)





# while True:
#     if a == s == b:
#         print()



# from  datetime import datetime
# n = datetime.now()
# g = [i for i in range(1, 10) ]
# a = datetime.now()
# v = a - n
# print(v)
















