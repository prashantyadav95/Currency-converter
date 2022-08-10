# Currency converter
# Using forex_python library

from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input("Enter the amount: "))

from_currency = input("From Currency(Currency code): ").upper()
to_currency = input("To Currency(Currency code): ").upper()

result = int(c.convert(from_currency,to_currency,amount))

print(from_currency, " To ", to_currency, amount," : ",result)
