import enum


class InvoiceTypeFrequency(enum.Enum):
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'
    YEARLY = 'YEARLY'
    ONCE = 'ONCE'
