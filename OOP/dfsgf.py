import datetime as dtt
import time

class Bancomat:
    def __init__(self):
        # self.lan = ""
        # self.name = ""
        self.balance = 0

    def language(self):
        while True:
            self.lan = input('Выберите язык: ')
            time.sleep(1)
            if self.lan == 'Кыргызский':
                print('Кош келиниз!')
                self.kyrg()
                break
            elif self.lan == 'Русский':
                print('Добро пожаловать!')
                self.rus()
                break
            else:
                print('error')
                continue

    def kyrg(self):
        self.name = input('Ф.И.О.: ')
        self.balance = int(input('Картадагы каражат: '))
        time.sleep(1)
        if self.pinn1():
            self.summ1()

    def rus(self):
        self.name = input('Ф.И.О.: ')
        self.balance = int(input('Сумма на карте: '))
        time.sleep(1)
        if self.pinn():
            self.summ()

    def pinn(self):
        pin = input("Пин код: ")
        if pin.isdigit() and len(pin) == 4:
            print("Принят")
            time.sleep(1)
            return True
        else:
            print("Попробуйте снова.")
            time.sleep(1)
            return False

    def pinn1(self):
        pin = input("Пин код: ")
        if pin.isdigit() and len(pin) == 4:
            print("Принят")
            time.sleep(1)
            return True
        else:
            print("Попробуйте снова.")
            time.sleep(1)
            return False

    def summ(self):
        x = [200, 500, 1000, 5000]
        x.append(self.balance)
        print(x)
        number = int(input("Введите сумму мак.10тыс.: "))
        time.sleep(1)
        if number % 100 == 0 and number % 240 != 0 and number < 10000:
            print("Возьмите деньги")
            time.sleep(2)
            self.Chek(number)
        else:
            print("Не удалось совершить операцию")

    def Chek(self, number):
        g = input('Нужен ли вам чек?   1) Да    2) Нет:')
        if g == 'Да':
            print(f'{self.name} | Общая сумма на карте {self.balance} сом | Осталось {self.balance - number} сом {dtt.datetime.now()}')


    def summ1(self):
        x = [200, 500, 1000, 5000]
        x.append(self.balance)
        print(x)
        number = int(input("Суммадагы каражатты териниз мак. 10 мин: "))
        time.sleep(1)
        if number % 100 == 0 and number % 240 != 0 and number < 10000:
            print("Акчаны алыныз")
            time.sleep(2)
            self.Chek1(number)
        else:
            print("Кайра кайталап корунуз")

    def Chek1(self, number):
        g = input('Чек керекпи?   1) Ооба    2) Жок:')
        if g == 'Ооба':
            print(f'{self.name} | Баланстагы каражат {self.balance} сом | Калдыгы {self.balance - number} сом {dtt.datetime.now()}')


a = Bancomat()
a.language()