# link of the question: https://leetcode.com/problems/simple-bank-system/description

# solution 1
class Bank:

    def __init__(self, balance: List[int]):
        self.user_money = balance
        self.num_account = len(balance)
        
    def valid_account(self, account:int) -> bool:
        if 1 <= account <= self.num_account:
            return True
        else:
            return False

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (self.valid_account(account1) and self.valid_account(account2) and self.user_money[account1-1] >= money):
            self.user_money[account1-1] -= money
            self.user_money[account2-1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if (self.valid_account(account)):
            self.user_money[account-1] += money
            return True
        else:
            return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if (self.valid_account(account) and self.user_money[account-1] >= money):
            self.user_money[account-1] -= money
            return True
        else:
            return False


# solution 2
class Bank:

    def __init__(self, balance: List[int]):
        self._balances = balance
        
    def valid_account(self, account:int) -> bool:
        return 1 <= account <= len(self._balances)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.valid_account(account1) or not self.valid_account(account2):
            return False
        if self._balances[account1-1] < money:
            return False
        
        self._balances[account1-1] -= money
        self._balances[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if money < 0:
            return False
        if self.valid_account(account):
            self._balances[account-1] += money
            return True
        else:
            return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if not self.valid_account(account):
            return False
        if self._balances[account-1] < money:
            return False
        if money < 0:
            return False
        
        self._balances[account-1] -= money
        return True

"""
1. no need length of balance, just use the length of _balances to ensure you can get the latest length of _balances
2. in valid_account, people who writing python often use return condition to simplified the condition branch
3. using guard clauses / early return 
    - people do not evaluate the successful condition
    - often deal with all unsuccessful conditions, which can return false early
4. some tips of python in OOP
    - balances is an inside variable, do not let the programmer access it directly
        def get_balance(self, account: int) -> int | None:
            if self.valid_account(account):
                return self._balances[account-1]
            else:
                return None
"""