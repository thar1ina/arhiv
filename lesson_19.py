# a = lambda a , b: a ** b
# print(a(3, 2))

a = lambda a , b: 'a больше ' if a > b else  'b больше'
a = int(input('num:'))
b = int(input('num:'))
print(a(a, b))
