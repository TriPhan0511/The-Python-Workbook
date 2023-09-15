from bank_accounts import *

dave = BankAccount(1000, 'Dave')
sarah = BankAccount(2000, 'Sarah')

# dave.get_balance()
# dave.balance = 4000
# dave.get_balance()

# dave.get_balance()
# sarah.get_balance()

# sarah.deposit(500)

# dave.withdraw(100000)
# # Withdraw interrupted:
# # Sorry, account 'Dave' only has a balance of $1000.00'

# dave.withdraw(10)
# # Withdraw completed.
# # Account 'Dave' balance = $990.00

# dave.transfer(10000, sarah)
# sarah.get_balance()
# # Beginning transfer.. 🚀
# # Transfer interrupted. ❌
# # Sorry, account 'Dave' only has a balance of $1000.00'
# # Account 'Sarah' balance = $2000.00

# dave.transfer(10, sarah)
# sarah.get_balance()
# # Beginning transfer.. 🚀
# # Withdraw completed.
# # Account 'Dave' balance = $990.00
# # Deposit completed.
# # Account 'Sarah' balance = $2010.00
# # Transfer completed! ✅
# # **********
# # Account 'Sarah' balance = $2010.00


# jim = InterestRewardsAcct(1000, 'Jim')

# jim.deposit(100)

# jim.transfer(100, dave)
# jim.get_balance()

blaze = SavingsAcct(1000, 'Blaze')

# blaze.deposit(100)
# # Account 'Blaze' balance = $1105.00

# blaze.transfer(100000, sarah)
# # **********
# # Beginning transfer.. 🚀
# # Transfer interrupted. ❌
# # Sorry, account 'Blaze' only has a balance of $1000.00'

# blaze.transfer(10, sarah)
# # **********
# # Beginning transfer.. 🚀
# # Withdraw completed.
# # Account 'Blaze' balance = $985.00
# # Deposit completed.
# # Account 'Sarah' balance = $2010.00
# # Transfer completed! ✅
# # **********

blaze.transfer(1000, sarah)
blaze.get_balance()


# blaze.withdraw(1000)
# # Withdraw interrupted:
# # Sorry, account 'Blaze' only has a balance of $1000.00'
