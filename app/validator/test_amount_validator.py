import pytest
from app.validator.amount_validator import amount_validator, positive_amount_validator

def test_amount_validator_raises_on_too_large():
    with pytest.raises(ValueError, match="exceed 10000"):
        amount_validator(20000)

def test_amount_validator_ok():
    amount_validator(5000)

def test_positive_amount_validator_raises_on_zero():
    with pytest.raises(ValueError, match="greater than 0"):
        positive_amount_validator(0)

def test_positive_amount_validator_raises_on_negative():
    with pytest.raises(ValueError, match="greater than 0"):
        positive_amount_validator(-5)

def test_positive_amount_validator_ok():
    positive_amount_validator(10)
