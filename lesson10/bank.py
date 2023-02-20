import random


def get_random_digits(count):
    get_list = ''
    for i in range(count):
        i = str(random.randint(1, 9))
        get_list += i
    return get_list


class BankAccount:
    def __init__(self, card_holder):
        self.card_holder = card_holder.upper()
        self.money = 0
        self.account_number = get_random_digits(20)
        self.card_number = get_random_digits(16)


class Bank:
    def __init__(self):
        self.bank_accounts: dict[str, BankAccount] = {}

    def open_account(self, card_holder):
        account = BankAccount(card_holder)
        self.bank_accounts[account.account_number] = account
        return account

    def add_money(self, account_number, money):
        a = self.bank_accounts[account_number]
        a.money += money

    def transfer_money(self, from_account_number, to_account_number, money):
        bank_chek = self.bank_accounts[from_account_number]
        bank_chek_2 = self.bank_accounts[to_account_number]
        bank_chek.money = bank_chek.money - money
        bank_chek_2.money = money

    def external_transfer(self, from_account_number, to_extrnal_number, money):
        user_chek = self.bank_accounts[from_account_number]
        user_chek.money = user_chek.money - money
        return 'Банк перевел', money, '$', 'с вашего счёта', user_chek, 'на внешний счёт', to_extrnal_number


class Controller:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        while True:
            print("Здравствуйте, наш банк открылся!")
            print("Выберите действие:")
            print("0. Завершить программу")
            print("1. Открыть новый счёт")
            print("2. Просмотреть открытые счета")
            print("3. Положить деньги на счёт")
            print("4. Перевести деньги между счетами")
            print("5. Совершить платёж")
            user = int(input())
            if user == 0:
                print("До свидания")
                break
            if user == 1:
                print("Введите имя и фамилию")
                card_holder = input()
                user_1=self.bank.open_account(card_holder)
                print("Счёт", user_1.card_number, "создан")
            if user ==2:
                print('Ваши открытые счета:')
                for account_number, account in self.bank.bank_accounts.items():
                    print(f'Cчёт: {account_number}')
                    print(f'   Остаток на счету: {account.money}$')
                    print(f'   Номер карты: {account.card_number}')
                    print(f'   Держатель карты: {account.card_holder}')
            elif user == 3:
                account_number = input('Введите номер cчёта: ')
                money = float(input(f'Количество денег: '))
                self.bank.add_money(account_number, money)
            elif user == 4:
                from_account_number = input('Введите номер cчёта-отправителя: ')
                to_account_number = input('Введите номер cчёта-получателя: ')
                money = float(input(f'Количество денег: '))
                self.bank.transfer_money(from_account_number, to_account_number, money)
            elif user == 5:
                from_account_number = input('Введите номер cчёта-отправителя: ')
                to_external_number = input('Введите номер счёта внешнего получателя: ')
                money = float(input(f'Количество денег: '))
                self.bank.external_transfer(from_account_number, to_external_number, money)
            else:
                print('Не поддерживаемая операция.')
            print()



if __name__ == '__main__':
    controller = Controller()
    controller.run()
