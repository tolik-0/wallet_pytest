import pytest
from wallet import Wallet, InsufficientFunds


@pytest.fixture
def empty_wallet() -> Wallet:
    """Return a wallet with zero balance."""
    return Wallet()


@pytest.fixture
def wallet_with_100() -> Wallet:
    """Return a wallet preloaded with 100 units."""
    return Wallet(100)


def test_default_balance_is_zero(empty_wallet: Wallet) -> None:
    """Wallet created without arguments should have zero balance."""
    assert empty_wallet.balance == 0


def test_initial_balance(wallet_with_100: Wallet) -> None:
    """Wallet created with initial balance should store that value."""
    assert wallet_with_100.balance == 100


@pytest.mark.parametrize("amount,expected", [(10, 10), (25, 25), (50, 50)])
def test_deposit_increases_balance(empty_wallet: Wallet, amount: int, expected: int) -> None:
    """Deposit should increase wallet balance by the given amount."""
    empty_wallet.deposit(amount)
    assert empty_wallet.balance == expected


def test_deposit_negative_amount_raises(empty_wallet: Wallet) -> None:
    """Negative deposit should raise ValueError."""
    with pytest.raises(ValueError):
        empty_wallet.deposit(-5)


@pytest.mark.parametrize("amount", [1, 50, 100])
def test_withdraw_decreases_balance(wallet_with_100: Wallet, amount: int) -> None:
    """Withdraw should decrease wallet balance when funds are sufficient."""
    wallet_with_100.withdraw(amount)
    assert wallet_with_100.balance == 100 - amount


def test_withdraw_too_much_raises(wallet_with_100: Wallet) -> None:
    """Withdrawing more than available should raise InsufficientFunds."""
    with pytest.raises(InsufficientFunds):
        wallet_with_100.withdraw(200)


def test_withdraw_negative_amount_raises(wallet_with_100: Wallet) -> None:
    """Negative withdraw should raise ValueError."""
    with pytest.raises(ValueError):
        wallet_with_100.withdraw(-10)
