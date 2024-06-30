#####000 # 1 - var
# class Person:
# name = 'Deniz'
# age = 24
# city = 'Bishkek'
# position = 'programmer'
# salary = 200000
#
# def say_hello(self):
# return f"hello {self.name}"
#
#
# d = Person()
# print(d.say_hello())
# print(d.city)

# 2-var
# class Person:
# def init(self, name, age, city, position, salary):
# self.name = name
# self.age = age
# self.city = city
# self.position = position
#  self.salary = salary
#
# def say_hello(self):
# return f"hello {self.name}"
#
#
# d = Person('Deniz', 24, 'Bishkek', 'programmer', 200000)
# print(d.say_hello())
# print(d.city)

# nasledovanie
#
# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def say_hello(self):
#         return f"hello {self.name}"
#
#     def walking(self):
#         return 'seyildoo'
#
#     def say(self):
#         return f"hello {self.name}"
#
#
# class Povar(Person):
#     def tamak(self):
#         return "tamak jasay alat"
#
#
# class Programmer(Povar):
#
#     def coding(self):
#         return 'kod jazat'
#
#
# p = Povar('Demir', 24, 200000)
# print(p.tamak())
# print(p.walking())
# print(p.say())
# d = Programmer('Diana', 24, 200000)
# print(d.coding())
# print(d.walking())
# print(d.tamak())
# print(d.say())
#
#

# class Animals:
#     def __init__(self, years):
#         self.years = years
#         name = 'dog'
#
#     def yearss(self):
#         return f'{self.years} лет'
#     def breathe(self):
#         return 'дышит'
#
# class Cats(Animals):
#     def mew(self):
#         return 'мяукает'
#
#
# class Dogs(Animals):
#     def bark(self):
#         return 'лаять'
#
# a = Cats(5)
# print(a.mew())
# print(a.breathe())
# print(a.years)
# b = Dogs(3)
# print(b.bark())
# print(b.breathe())
# print(b.years)


# 2

# class Persons:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def name1(self):
#         return f'I am {self.name}'
#     def age1(self):
#         return f'I am {self.age} years old'
#
# a = Persons('Zarina', 18)
# print(a.name1())
# print(a.age1())


# 3

# class AUTO:
#     def __init__(self, name, year, ss):
#         self.name = name
#         self.year = year
#         self.ss = ss
#
#     def yearr(self):
#         return f'Первый выпуск {self.year} году'
#
#     def namee(self):
#         return f'{self.name}'
#
#
# class SPORTAUTO(AUTO):
#     def s(self):
#         return f'Максимальная скорость {self.ss}'
#
#
# a = SPORTAUTO('Ferrari', 1946,'340 км/ч' )
# print(a.namee())
# print(a.yearr())
# print((a.s()))

# 4

# class PC:
#     def __init__(self,name, year, CPU, RAM, SSD):
#         self.name = name
#         self.year = year
#         self.CPU = CPU
#         self.RAM = RAM
#         self.SSD = SSD
#
#     def cpu(self):
#         return f'Процессор {self.CPU}'
#
#
#     def ram(self):
#         return f'Оперативная память  {self.RAM}'
#
#     def ssd(self):
#         return f'Ёмкость диска {self.SSD}'
#
# class Dictionary(PC):
#
#
#     def naame(self):
#
#         return f'Имя {self.name}'
#
#     def its(self):
#         return f'Год  {self.year}'
#
# class Dictionary1(PC):
#
#
#     def naame1(self):
#         return f'Имя {self.name}'
#
#     def its1(self):
#         return f'Год  {self.year}'
#
#
#
#
#
#
#
# a = Dictionary( 'Aser', 2020, 'Intel® Pentium(R) Silver N5030 CPU @ 1.10GHz × 4 ', 8,
#                 '240,1GB')
# print(a.naame())
# print(a.its())
# print(a.cpu())
# print(a.ram())
# print(a.ssd())
# a1 = Dictionary1('Asus', 2023,'J4005I', 8, '240 GB')
# print(a1.naame1())
# print(a1.its1())
# print(a1.cpu())
# print(a1.ram())
# print(a1.ssd())





