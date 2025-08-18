from playlists.py_openexchangerates import OpenExchangeRates

oe = OpenExchangeRates()
x = oe.convert_to_currency('USD', 'GBP', 50)
y = oe.convert_to_currency('GBP', 'INR', 100)

print(f'Conversion for 50 USD to GBP :: {x}')
print(f'Conversion for 100 GBP to INR :: {y}')