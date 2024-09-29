import enum


class InvoiceTypeFrequency(enum.Enum):
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'
    YEARLY = 'YEARLY'
    ONCE = 'ONCE'

    def __str__(self):
        return self.value

    def __repr__(self) -> str:
        return super().__repr__() + f'({self.value})'

    def __dict__(self):
        return self.value
