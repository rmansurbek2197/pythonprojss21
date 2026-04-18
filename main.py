class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Depozit amalga oshirildi. Hozirgi balans: {self.balance}")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Balans yetarli emas")
        else:
            self.balance -= amount
            print(f"Pul yechildi. Hozirgi balans: {self.balance}")

    def check_balance(self):
        print(f"Hozirgi balans: {self.balance}")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_name, balance=0):
        self.accounts[account_number] = BankAccount(account_number, account_name, balance)
        print(f"Hisa yaratildi. Hisa raqam: {account_number}")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def list_accounts(self):
        for account in self.accounts.values():
            print(f"Hisa raqam: {account.account_number}, Hisa nomi: {account.account_name}, Balans: {account.balance}")


def main():
    bank_system = BankSystem()
    while True:
        print("1. Hisa yaratish")
        print("2. Hisaga depozit qilish")
        print("3. Hisadan pul yechish")
        print("4. Hisa balansini tekshirish")
        print("5. Barcha hisalarni ko'rish")
        print("6. Chiqish")
        choice = input("Tanlang: ")
        if choice == "1":
            account_number = input("Hisa raqam: ")
            account_name = input("Hisa nomi: ")
            balance = float(input("Balans: "))
            bank_system.create_account(account_number, account_name, balance)
        elif choice == "2":
            account_number = input("Hisa raqam: ")
            account = bank_system.get_account(account_number)
            if account:
                amount = float(input("Depozit summa: "))
                account.deposit(amount)
            else:
                print("Hisa topilmadi")
        elif choice == "3":
            account_number = input("Hisa raqam: ")
            account = bank_system.get_account(account_number)
            if account:
                amount = float(input("Yechish summa: "))
                account.withdrawal(amount)
            else:
                print("Hisa topilmadi")
        elif choice == "4":
            account_number = input("Hisa raqam: ")
            account = bank_system.get_account(account_number)
            if account:
                account.check_balance()
            else:
                print("Hisa topilmadi")
        elif choice == "5":
            bank_system.list_accounts()
        elif choice == "6":
            break
        else:
            print("Noto'g'ri tanlov")

if __name__ == "__main__":
    main()