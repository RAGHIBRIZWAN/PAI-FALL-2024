def currencyConvertor(currency1,amount,rate,currency2):
    ans = amount * rate
    print(f"{currency1} having amount {amount} is converted into {currency2} and the converted amount is {ans}")

currency1 = str(input('Enter the currency that needs to be converted: '))
currency2 = str(input('Enter the currency in which it is converted: '))
rate = float(input('Enter the exchange rate: '))
amount = int(input('Enter the amount to be converted: '))

currencyConvertor(currency1,amount,rate,currency2)
