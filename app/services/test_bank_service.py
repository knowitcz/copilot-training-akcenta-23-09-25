import pytest
from app.services.bank_service import BranchBankService, AtmBankService
from app.validator.amount_validator import AmountValidator

class AccountServiceDouble:
    def __init__(self):
        self.deposits = []
        self.withdrawals = []
        self.transfers = []

    def deposit_money(self, account_id, amount):
        self.deposits.append((account_id, amount))

    def withdraw_money(self, account_id, amount):
        self.withdrawals.append((account_id, amount))

    def transfer_money(self, from_account_id, to_account_id, amount):
        self.transfers.append((from_account_id, to_account_id, amount))

# BranchBankService tests

def test_branchbankservice_deposit():
    test_double = AccountServiceDouble()
    service = BranchBankService(test_double)
    service.deposit_money(1, 100)
    assert test_double.deposits == [(1, 100)]

def test_branchbankservice_withdraw():
    test_double = AccountServiceDouble()
    service = BranchBankService(test_double)
    service.withdraw_money(1, 50)
    assert test_double.withdrawals == [(1, 50)]

def test_branchbankservice_transfer():
    test_double = AccountServiceDouble()
    service = BranchBankService(test_double)
    service.transfer_money(1, 2, 200)
    assert test_double.transfers == [(1, 2, 200)]

# AtmBankService tests
def test_atmbankservice_deposit_valid():
    test_double = AccountServiceDouble()
    validator = AmountValidator()
    service = AtmBankService(test_double, validator)
    service.deposit_money(1, 100)
    assert test_double.deposits == [(1, 100)]

def test_atmbankservice_deposit_too_large():
    test_double = AccountServiceDouble()
    validator = AmountValidator()
    service = AtmBankService(test_double, validator)
    with pytest.raises(ValueError):
        service.deposit_money(1, 20000)

def test_atmbankservice_withdraw_valid():
    test_double = AccountServiceDouble()
    validator = AmountValidator()
    service = AtmBankService(test_double, validator)
    service.withdraw_money(1, 100)
    assert test_double.withdrawals == [(1, 100)]

def test_atmbankservice_withdraw_too_large():
    test_double = AccountServiceDouble()
    validator = AmountValidator()
    service = AtmBankService(test_double, validator)
    with pytest.raises(ValueError):
        service.withdraw_money(1, 20000)
