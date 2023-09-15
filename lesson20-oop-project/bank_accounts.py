class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.name = account_name
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}.")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit completed.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}'")

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print('\nWithdraw completed.')
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning transfer.. 🚀')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer completed! ✅\n\n**********')
        except BalanceException as error:
            print(f"Transfer interrupted. ❌ {error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print("\nDeposit completed.")
        self.get_balance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5

    def withdraw(self, amount):
        super().withdraw(amount + self.fee)

    def transfer(self, amount, account):
        return super().transfer(amount + self.fee, account)
