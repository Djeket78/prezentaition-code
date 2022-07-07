#Solving the situation when a client wants to pay for a service

service_price = 100
coefitient_crypto=1.5


client_cash_amount= int(input('Enter cash amount: '))


if client_cash_amount >= service_price:
    print('CASH payment success!!!')
else: 
    print('CASH Payment FALURE!!!')
    client_card_amount= int(input('Enter card amount: '))
    if client_card_amount >=service_price:
        print('CASH payment success!!!')
    else:
        print('CASH Payment FALURE!!!')
        client_cash_crypto= int(input('Enter crypto amount: '))
        convert_crypto=client_cash_crypto * coefitient_crypto
        if convert_crypto >=service_price:
             print('CASH payment success!!!')
        else:
             print('CASH Payment FALURE!!!')
    