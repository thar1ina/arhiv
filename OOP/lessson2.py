import time


# class Shop:
#
#     def __init__(self):
#         self.balance = 0

        # self.pocupcaa = 0



#     def balanc(self):
#         print('Добро пожаловать!')
#         time.sleep(2)
#         print('-' *20)
#         time.sleep(1)
#         self.balance = input('Сумма на карте:')
#         time.sleep(1)
#         print('Хорошо')
#         print('-' * 20)
#         time.sleep(1)
#
#         self.pocupca()
#
#
#     def pocupca(self):
#         pocupcaa = input('Сколько вышло:')
#         time.sleep(1)
#         if pocupcaa > self.balance:
#             print('недостаточно средств')
#
#         elif pocupcaa >= 5000 and pocupcaa < 10000:
#             n = pocupcaa - (pocupcaa // 100 * 5)
#             print(f'Покупка вышло больше 5000 сомов вам скидка на 5 % ')
#             print(f'Итог {n} сом')
#             time.sleep(1)
#             print('Cпасибо за покупку :)')
#
#         elif pocupcaa >= 10000:
#             b = pocupcaa - (pocupcaa // 100 * 10)
#             print(f'Покупка вышло больше 10000 сомов вам скидка на 10 % ')
#             print(f'Итог {b} сом')
#             time.sleep(1)
#             print('Cпасибо за покупку :)')
#
#         elif pocupcaa < 5000 and pocupcaa > 0:
#             print(f'Без скидки итог {pocupcaa} сомов')
#             time.sleep(1)
#             print('Cпасибо за покупку :)')
#         else:
#             print('error')
#
#
#
# a = Shop()
# a.balanc()