## api_key : "HI :P"

balance_sheet = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?period=quarterly&limit={years}&apikey={api_key}')


while True:
    comman = input('Company Name')

    if comman == 'IS':
        printi('Retrieve Company')

    elif comman == 'quit':
        break

    else:
        print('Statement not valid')