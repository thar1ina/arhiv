# Ответы на вопросы
# 1
'''
ООП делиться на три:
1 Инкапсуляция
2 Полиморфизм
3 Наследование
'''

# 2
'''Во первых  создаём class и даём название и в магический метод __init__ мы пишем атрибуты ,
с помощью self мы связываем их с методом .'''

# 3
'''
Простыми словами можно сказать class мы пишем в начале а объект в конце
В первую очередь мы создаем class и даём название пишется большой буквой иначе ошибка
 а в конце в этот class мы даём аргументы

'''

# 4

'''
Инкапсуляция делиться на три:
1 публичный - public
2 приватный - privad
3 закрытый  - protected

В объекте публичном можно вызвать и методы и атрибуты.
В приватном атрибуте есть одно нижнее подчёркивание и можно вызвать только методы.
В закрытом есть два нижнее подчеркивание и тоже можно вызвать только нижнее подчеркивание.
Чтобы вызвать атрибуты мы можем использовать getter , а изменить setter.
'''

# 5
'''Наследование бывает родительский и дочерний , 
от родительского в дочериний мы можем наследовать и методы и атрибуты и можем изменить его 
есть метод super в котором наследуем атрибуты и сразу можно их менять'''

# 6
''' Простыми словами мы можем сказать это инкапсуляция и наследование вместе взятых '''






'''ЗАДАЧИ'''


'''
Задача о банковском счете: Создайте класс BankAccount, который имеет атрибуты balance
 (баланс) и методы для deposit (внесения средств) и withdraw (снятия средств).
 Ограничьте сумму снятия, чтобы она не могла превышать текущий баланс.
 '''


# Задача 1

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def deposit(self):
#         if self.balance <= 15000:
#             return f'Средство внесён'
#         elif self.balance > 15000:
#             return f'Максимум 15тыс.'
#         else:
#             return 'error'
#
#     def withdraw(self):
#         if self.balance <= 18000:
#             return f'Снято'
#         elif self.balance > 18000:
#             return f'Максимум 18тыс.'
#         else:
#             return f'error'
#
#
# a = BankAccount(13000)
# print(a.deposit())
# print(a.withdraw())





'''
Создайте класс Book с атрибутами название, автор и год издания. Создайте методы для вывода информации о книге.
Затем создайте список книг и реализуйте метод для поиска книг по автору или году издания.
'''


# Задача 2


# class Book:
#     def __init__(self, name, avtor, year):
#         self.name = name
#         self.avtor = avtor
#         self.year = year
#
#     def info(self):
#         return f'Название книги {self.name}\nАвтор книги {self.avtor}\nГод {self.year}'
#
# class Books(Book):
#     def info2(self):
#         return f'{self.name} название книги\n{self.avtor} писатель\n{self.year} год'
#
#
#
#
#
#
# a = Book('<<Детство>>', '<<Лев Толстой>>', '<<1852>>')
# print(a.info())
# b = Books('<<Биринчи мугалим>>', '<<Чынгыз Айтматов>>','<<1962>>')
# print(b.info2())


'''
Создайте классы для моделирования товаров в магазине и корзины для покупок.
Покупатель должен иметь возможность добавлять товары в корзину и рассчитывать общую стоимость.
'''


# задача 3

# class Shop:
#     def __init__(self, name, corzina):
#         self.name = name
#         self.price = corzina
#
# class ShoppingCart:
#     def __init__(self):
#         self.odegda = []








'''
Создайте классы Bank и Customer, чтобы моделировать банковский аккаунт.
 Каждый клиент банка может иметь несколько счетов, 
 и банк должен предоставлять методы для открытия новых счетов, внесения и снятия средств.
'''


# задача 4

# class BankAccount:
#     def __init__(self, num, balance=0):
#         self.num = num
#         self.balance = balance
#
#     def deposit(self, sum):
#         self.balance += sum
#         print(f"Счет {self.num} Внесено {sum} som.")
#
#     def withdraw(self, sum):
#         if self.balance >= sum:
#             self.balance -= sum
#             print(f"Счет {self.num} Снято {sum} som.")
#         else:
#             print(f"Счет {self.num} Недостаточно средств для снятия.")
#
# class Customer:
#     def __init__(self, name):
#         self.name = name
#         self.new = {}
#
#     def open(self, num):
#         if num not in self.new:
#             self.new[num] = BankAccount(num)
#             print(f"Счет {num} открыт для клиента {self.name}.")
#         else:
#             print(f"Счет {num} уже существует для клиента {self.name}.")
#
# v = BankAccount(2300)
# v.deposit(3000)
# v.withdraw(400)
#
# s = Customer("Zarina")
#
# s.open("4177490179125507")
# s.open("4143784658943789")


