import sqlite3
import re


def get_number(number: str) -> bool:
    return re.fullmatch(r'\+375\((29|25|33|44)\)\d{7}', number) is not None


def get_name(name: str) -> bool:
    return re.fullmatch(r'[\w]+', name) is not None


class acaunt:
    def __init__(self):
        with sqlite3.connect("telefon.db") as connection:
            connection.execute('SELECT * FROM telefon')

    def into_number(self, name, number):
        user = (name, number)
        with sqlite3.connect("telefon.db") as connection:
            connection.execute("insert Into telefon (name,number) values(?,?)", user)

    def alfa_name(self):
        with sqlite3.connect("telefon.db") as connection:
            total = connection.execute('SELECT * FROM telefon order by name')
            for phone in total.fetchall():
                print(phone)

    def update_cont(self, name, number):
        user = (name, number)
        with sqlite3.connect('telefon.db') as connection:
            connection.execute('update telefon set number = ? where name = ?', user)


class Controller:
    def __init__(self):
        self.akk = acaunt()

    def start(self):
        print("welcom into telefon-book")
        while True:
            print("Введите 0 Выйти из программы")
            print("Введите 1. Добавить новый контакт")
            print("Введите 2. Вывести весь список контактов в алфавитном порядке")
            print("Введите 3. Обновить номер контакта")
            user = int(input("Ведите число:"))
            if user == 1:
                print("Введите имя")
                name = input()
                while True:
                    if get_name(name) is False:
                        print("Попробуйте ещё")
                        name = input()
                    else:
                        break
                print("Введите номер телефона")
                number = input()
                while True:
                    if get_number(number) is False:
                        print("Попробуйте ещё")
                        number = input()
                    else:
                        break
                self.akk.into_number(name, number)

            if user == 2:
                print("Список ваших контактов:")
                self.akk.alfa_name()

            if user == 3:
                print("обновление номера ")
                print("Введите имя")
                name = input()
                while True:
                    if get_name(name) is False:
                        print("Попробуйте ещё")
                        name = input()
                    else:
                        break
                print("Введите номер телефона")
                number = input()
                while True:
                    if get_number(number) is False:
                        print("Попробуйте ещё")
                        number = input()
                    else:
                        break
                self.akk.update_cont(name, number)
                print("Complite")
            if user == 0:
                print("Good bye")
                break


if __name__ == '__main__':
    sudo = Controller()
    sudo.start()
