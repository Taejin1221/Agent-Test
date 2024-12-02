from repository.balance_repository import BalanceRepository


class BalanceService:
    def __init__(self, balance_repository: BalanceRepository):
        self.balance_repository = balance_repository

    def get_balance(self) -> int:
        return self.balance_repository.get_balance()
