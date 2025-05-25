import pytest
from unittest.mock import Mock
from app.services.bank_service import BranchBankService, AtmBankService, OnlineBankService

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


def amount_validator(amount):
    if amount <= 0 or amount > 10000:
        raise ValueError("Amount must be positive and less than or equal to 10000")

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
    service = AtmBankService(test_double, amount_validator)
    service.deposit_money(1, 100)
    assert test_double.deposits == [(1, 100)]

def test_atmbankservice_deposit_too_large():
    test_double = AccountServiceDouble()
    service = AtmBankService(test_double, amount_validator)
    with pytest.raises(ValueError):
        service.deposit_money(1, 20000)

def test_atmbankservice_withdraw_valid():
    test_double = AccountServiceDouble()
    service = AtmBankService(test_double, amount_validator)
    service.withdraw_money(1, 100)
    assert test_double.withdrawals == [(1, 100)]

def test_atmbankservice_withdraw_too_large():
    test_double = AccountServiceDouble()
    service = AtmBankService(test_double, amount_validator)
    with pytest.raises(ValueError):
        service.withdraw_money(1, 20000)

# OnlineBankService tests
def test_onlinebankservice_transfer_valid():
    test_double = AccountServiceDouble()
    service = OnlineBankService(test_double, amount_validator)
    service.transfer_money(1, 2, 300)
    assert test_double.transfers == [(1, 2, 300)]

def test_onlinebankservice_transfer_too_large():
    test_double = AccountServiceDouble()
    service = OnlineBankService(test_double, amount_validator)
    with pytest.raises(ValueError):
        service.transfer_money(1, 2, 20000)
