import pytest
from app.calculations import add, BankAccount

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(100)

@pytest.mark.parametrize("num1, num2, result", [
    (3,2,5),
    (7,1,8),
    (4,4,8)
])
def test_add(num1, num2, result):
    print("testing add function")
    assert add(num1, num2) == result

def test_bank_balance_initial(bank_account):
    
    assert bank_account.balance == 100

def default_test_bank_balance_initial(zero_bank_account):
    
    assert zero_bank_account.balance == 100

def test_deposit(bank_account):
    
    bank_account.deposit(80)
    assert bank_account.balance == 180

def test_withdraw(bank_account):
   
    bank_account.withdraw(40)
    assert bank_account.balance == 60

def test_collect_interest(bank_account):
    
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 110 
@pytest.mark.parametrize("deposit, withdraw, result", [
    (100, 80, 20),
    (200, 90, 110),
    (400, 310, 90)
])
def test_transaction(zero_bank_account,deposit, withdraw, result):
    zero_bank_account.deposit(deposit)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == result