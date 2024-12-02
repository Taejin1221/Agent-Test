import json


class BalanceRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _read_data(self) -> dict:
        with open(self.file_path, "r") as f:
            return json.load(f)

    def get_balance(self) -> int:
        data = self._read_data()
        balance = data["balances"]

        return balance
