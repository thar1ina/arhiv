######публичный
# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def say(self):
#         return f"my name is {self.name},  my salary {self.salary}"
#
# d = Person('Deniz', 24, 200000)
# print(d.say())

#####privad######
# class Person:
#     def __init__(self, name, age, salary):
#         self._name = name
#         self._age = age
#         self._salary = salary
#
#     def say(self):
#         return f"my name is {self._name},  my salary {self._salary}"
#
# d = Person('Deniz', 24, 200000)
# print(d.say())

###### защищенный #######
# class Person:
#     def __init__(self, name, age, salary):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary
#
#     def getter(self):
#         return self.__name
#
#     def setter(self, name_2, age_2):
#         self.__name = name_2
#         self.__age = age_2
#         return self.__name
#
#
#     def say(self):
#         return f"my name is {self.__name},  my salary {self.__salary}"
#
# d = Person('Deniz', 24, 200000)
# print(d.getter())
# print(d.setter('Tilek', 18))









# 1

# class Computer:
#     def __init__(self, cpu, memory):
#         self._cpu = cpu
#         self._memory = memory
#
#
#     def make_computations(self):
#         return f'Процессор {self._cpu},| Память {self._memory}'
#
#
#     def getter(self):
#         return self._cpu, self._memory
#
#
#     def setter(self, cpu2, memory2):
#         self._cpu = cpu2
#         self._memory = memory2
#         return self._cpu, self._memory
#
#
#
#
# a = Computer('Intel® Pentium(R) Silver N5030 CPU @ 1.10GHz × 4', '256 gb')
# print(a.make_computations())
# print(a.getter())
# print(a.setter('J4005I', '128 gb'))


# class Phone:
#     def __init__(self):
#         self._sim_cards_list = ['Beeline', 'O', 'MegaCom']
#
#     def get(self):
#         return self._sim_cards_list
#
#     def set(self, sim_cards):
#         self._sim_cards_list = sim_cards
#
#     def call(self):
#         d = input('+996')
#         if d[:2] == '77' or d[:2] == '22':
#             _sim = self._sim_cards_list[0]
#             print(f"Идет звонок {d} с сим-карты- {_sim}")
#
#
#         elif d[:1] == '7' or d[:1] == '5':
#             _sim2 = self._sim_cards_list[1]
#             print(f"Идет звонок {d} с сим-карты- {_sim2}")
#
#
#         elif d[:2] == '55' or d[:2] == '99':
#             _sim2 = self._sim_cards_list[2]
#             print(f"Идет звонок {d} с сим-карты- {_sim2}")
#
#         else:
#             print("Недопустимый номер")
#
# n = Phone()
# print(n.get())
# n.call()




# 3

#
#
#
#
#
#
