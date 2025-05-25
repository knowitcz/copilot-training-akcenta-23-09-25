class AmountValidator:
    def validate(self, amount: int) -> None:
        if amount > 10000:
            raise ValueError("Amount cannot exceed 10000.")
