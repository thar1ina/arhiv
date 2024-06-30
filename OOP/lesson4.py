# Полимарфизм

# class Mix:
#     def __init__(self, name):
#         self.__name = name
#
#     def dyshat(self):
#         return f'Я могу дышать'
#
#
# class Animal(Mix):
#     def __init__(self):
#         super().__init__('Bear')
#
#     def dyshat(self):
#         return f'Я медведь я могу дышать'
#
#
# a = Mix('Asan')
# print(a.dyshat())
# b = Animal()
# print(b.dyshat())


# def my_func(x: int, y: float) -> float:
#     """
#     :param x: djkfhwepiurtylenfvpiguewrhsfjapuwiefjkads
#     :param y: kdjgpaoe;riufghjoaue
#     :return: dfhjp9eahvaiosjdfv
#     """
#
# print(my_func(12, 12.5))
#############################################################
# class Person:
#     def __init__(self, name: str, lastname: str):
#         self.name = name
#         self.lastname = lastname
#
#     def info(self):
#         return f'Your info: {self.name}\n{self.lastname}'
#
#
# class Animal(Person):
#     pass
#
#
# per = Person('Asan', 'Asanov')
# print(per.info())





# 1

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
#
#
#     def withdraw(self):
#         return f'Ваш баланс пополнен на {self.__balance} сомов'
#
#
#     def deposit(self, balance2):
#         self.__balance = balance2
#         return f'Ваш баланс пополнен на {self.__balance} сомов'
#
#
#
#
#
# a = BankAccount(300)
# print(a.withdraw())
# print(a.deposit(400))



# class Shape:
#     def __init__(self,  a, b):
#         # self.S = S
#         self.a = a
#         self.b = b
#
#
# class Circle(Shape):
#
#     def S2(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self):
#         super().__init__(235, 40)
#
#     def S(self):
#         return self.a * self.b
#
#
#
#
# a = Rectangle()
# print(a.S())



# 3

class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius, area):
        super().__init__()
        self.__radius = radius
        self.__area = area

    def calculate(self):
        return 3.14 * self.__radius * self.__area     # П == 3.14

    def info(self):
        r = self.calculate()
        return f"Круг радиус: {self.__radius}, площадь: {r}."


class RightTriangle(Figure):
    def __init__(self, a, b):
        super().__init__()
        self.__a = a
        self.__b = b

    def calculate(self):
        return   self.__a * self.__b //2

    def info(self):
        r = self.calculate()
        return f"Прямоугольный треугольник сторона а: {self.__a}, сторона b: {self.__b}, площадь: {r}."


l = Circle(2 , 12)
t = RightTriangle(5, 8)
print(l.info())
print(t.info())


        