# test_mock_time.py
import pytest
import datetime
from freezegun import freeze_time
from mock_time import discount_calculator

class DiscountCalculatorTest:
    @freeze_time("2021-04-26")
    def test_discount(self):
        assert(
            discount_calculator(
                value=100,
                due_date=datetime.date(year=2020, month=4, day=28),
                days=3,
                discount=0.2
            )
            == 80.0
        )

    @freeze_time("2021-04-26")
    def test_no_discount(self):
        assert(
            discount_calculator(
                value=100,
                due_date=datetime.date(year=2020, month=4, day=28),
                days=3,
                discount=0.2
            )
            == 100.0
        )


if __name__ == '__main__':
    pytest.main()
