import pytest

from shipping import shipping_fee


@pytest.mark.parametrize("weight_kg", [-1, 0])
def test_non_positive_weight_is_rejected(weight_kg):
    with pytest.raises(ValueError, match="weight must be more than 0 kg"):
        shipping_fee(weight_kg)


@pytest.mark.parametrize("weight_kg", [0.5, 1])
def test_up_to_one_kilogram_costs_40_baht(weight_kg):
    assert shipping_fee(weight_kg) == 40


@pytest.mark.parametrize("weight_kg", [1.1, 5])
def test_over_one_and_up_to_five_kilograms_costs_60_baht(weight_kg):
    assert shipping_fee(weight_kg) == 60


@pytest.mark.parametrize(
    ("weight_kg", "expected_fee"),
    [
        (5.01, 70),
        (5.2, 70),
        (6, 70),
        (6.01, 80),
    ],
)
def test_over_five_kilograms_charges_for_each_started_kilogram(
    weight_kg, expected_fee
):
    assert shipping_fee(weight_kg) == expected_fee
