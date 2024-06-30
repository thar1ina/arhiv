# class Computer:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def browse(self, url):
#         print(f"Используется {self.brand} {self.model} для просмотра {url}")
#
#
# class Phone:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def call(self, number):
#         print(f"Вызов {number} с помощью {self.brand} {self.model}")
#
#
# class SmartPhone(Computer, Phone):
#     def __init__(self, brand, model):
#         super().__init__(brand, model)
#
#     def use_gps(self, location):
#         print(f"Симуляция маршрута до {location} с помощью {self.brand} {self.model}")
#
#
#
# a = Computer("Dell", "Inspiron")
# print(a.browse())
# b = Phone("Apple", "iPhone 12")
# c = SmartPhone("Samsung", "Galaxy S21")
# d = SmartPhone("Google", "Pixel 6")