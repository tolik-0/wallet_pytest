class InsufficientFunds(Exception):
    """Custom exception raised when wallet does not have enough balance."""
    pass


class Wallet:
    """Simple wallet that stores an integer balance."""

    def __init__(self, initial_balance: int = 0) -> None:
        """Initialize wallet with optional initial balance."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._balance = initial_balance

    @property
    def balance(self) -> int:
        """Return current wallet balance."""
        return self._balance

    def deposit(self, amount: int) -> None:
        """Add funds to the wallet.

        :param amount: Positive amount to add.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: int) -> None:
        """Withdraw funds from the wallet.

        :param amount: Positive amount to withdraw.
        :raises InsufficientFunds: If balance is not enough.
        """
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self._balance:
            raise InsufficientFunds("Not enough balance in wallet.")
        self._balance -= amount

    def __repr__(self) -> str:
        """Return string representation for debugging."""
        return f"Wallet(balance={self._balance})"


def main() -> None:
    """Simple CLI for interacting with the wallet."""
    wallet = Wallet()
    print("Wallet CLI. Commands: deposit <amount>, withdraw <amount>, balance, quit")
    while True:
        command = input("> ").strip().lower()
        if command in {"quit", "exit"}:
            print("Goodbye!")
            break
        try:
            if command.startswith("deposit"):
                _, amount_str = command.split()
                wallet.deposit(int(amount_str))
                print(f"Deposited {amount_str}. New balance: {wallet.balance}")
            elif command.startswith("withdraw"):
                _, amount_str = command.split()
                wallet.withdraw(int(amount_str))
                print(f"Withdrew {amount_str}. New balance: {wallet.balance}")
            elif command == "balance":
                print(f"Current balance: {wallet.balance}")
            else:
                print("Unknown command.")
        except (ValueError, InsufficientFunds) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()