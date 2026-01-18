// link of the question: https://leetcode.com/problems/simple-bank-system/description

// solution 1
class Bank {
private:
    vector<long long> user_money;
    int num_account;
    bool valid_account(int account) {
        if (account >= 1 && account <= user_money.size()) {
            return true;
        } else {
            return false;
        }
    }

public:
    Bank(vector<long long>& balance) {
        user_money = balance;
        num_account = balance.size();
    }

    bool transfer(int account1, int account2, long long money) {
        if (valid_account(account1) && valid_account(account2) && user_money[account1-1] >= money) {
            user_money[account1-1] -= money;
            user_money[account2-1] += money;
            return true;
        } else {
            return false;
        }
    }
    
    bool deposit(int account, long long money) {
        if (valid_account(account)) {
            user_money[account-1] += money;
            return true;
        } else {
            return false;
        }
    }
    
    bool withdraw(int account, long long money) {
        if (valid_account(account) && user_money[account-1] >= money) {
            user_money[account-1] -= money;
            return true;
        } else {
            return false;
        }
    }
};

// solution 2
class Bank {
private:
    vector<long long> balances;
    bool valid_account(int account) {
        return account >= 1 && account <= balances.size();
    }

public:
    Bank(vector<long long>& balance) {
        balances = std::move(balance);
    }

    bool transfer(int account1, int account2, long long money) {
        if (!valid_account(account1) || !valid_account(account2)) {
            return false;
        }
        if (balances[account-1] < money || money <= 0) {
            return false;
        }
        
        balances[account1-1] -= money;
        balances[account2-1] += money;
        return true;
    }
    
    bool deposit(int account, long long money) {
        if (money <= 0) {
            return false;
        }
        if (!valid_account(account)) {
            return false;
        }

        balances[account-1] += money;
        return true;
    }
    
    bool withdraw(int account, long long money) {
        if (money <= 0) {
            return false;
        }
        if (!valid_account(account) || balances[account-1] < money) {
            return false;
        }

        balances[account-1] -= money;
        return true;
    }
};

/*
1. no need length of balance, just use the length of _balances to ensure you can get the latest length of _balances
2. in valid_account, people often use return condition to simplified the condition branch
3. using guard clauses / early return 
    - people do not evaluate the successful condition
    - often deal with all unsuccessful conditions, which can return false early
4. some tips in OOP
    - balances is an inside variable, do not let the programmer access it directly
        optional<long long> get_balance(int account) {
            if (!valid_account(account)) {
                return std::nullopt;
            } else {
                return balances[account-1];
            }
        }

- detail of optional<T>
    - in traditional C++, some invalid value (like nullptr, -1, "", ...) may be confused with the valid value
    - the optional has been created to replace invalid value
    - it will return the T type value, which you have defined or return nothing (nullopt)
    - need to include <optional> and C++17 up version can use it

- detail of move
    - often used to create an object, because it only copies the pointer, it can be faster
    - can not use the value of the variable after move, it can only be reassigned or deleted
    - need to include <utility> and C++11 up version can use it 
*/