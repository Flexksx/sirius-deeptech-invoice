import enum


class DueInvoicePeriod(enum.Enum):
    DAY = 'DAY'
    WEEK = 'WEEK'
    MONTH = 'MONTH'
    YEAR = 'YEAR'
    ONCE = 'ONCE'

    def __str__(self):
        return self.value

    def __repr__(self) -> str:
        return super().__repr__() + f'({self.value})'

    def __dict__(self):
        return self.value
