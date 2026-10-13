import pytest

from bank import BankAccount, InsufficientFunds


@pytest.fixture
def account():
    return BankAccount("alice", balance=100)


def test_account_starts_with_fixture_data(account):
    assert account.owner == "alice"
    assert account.balance == 100


def test_deposit_increases_balance(account):
    account.deposit(50)

    assert account.balance == 150


@pytest.mark.parametrize("amount", [0, -1])
def test_deposit_rejects_non_positive_amounts(account, amount):
    with pytest.raises(ValueError, match="deposit must be positive"):
        account.deposit(amount)

    assert account.balance == 100


def test_withdraw_decreases_balance(account):
    account.withdraw(10)

    assert account.balance == 90


def test_withdraw_more_than_balance_is_refused(account):
    with pytest.raises(InsufficientFunds, match="balance is only 100"):
        account.withdraw(500)

    assert account.balance == 100


def test_each_test_gets_a_fresh_account(account):
    assert account.balance == 100


def test_deposit_of_zero_is_refused(account):
    with pytest.raises(ValueError):
        account.deposit(0)

    assert account.balance == 100


def test_withdrawing_whole_balance_leaves_zero(account):
    account.withdraw(100)

    assert account.balance == 0


def test_two_withdrawals_both_reduce_balance(account):
    account.withdraw(30)
    account.withdraw(20)

    assert account.balance == 50


def test_add_interest_increases_balance_by_rate(account):
    account.add_interest(0.05)

    assert account.balance == pytest.approx(105)


def test_interest(account):
    account.add_interest(0.10)

    assert account.balance == pytest.approx(110)
