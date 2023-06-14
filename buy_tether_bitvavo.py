import ccxt

API_KEY = ""
API_SECRET = ""
BASE_CURRENCY = "EUR"
TARGET_CURRENCY = "USDT"
TARGET_AMOUNT = 100
MINIMUM_EUR_AMOUNT = 5

exchange = ccxt.bitvavo({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})

symbol = f"{TARGET_CURRENCY}/{BASE_CURRENCY}"
order_type = 'market'
side = 'buy'
amount = None
price = None

# Fetch balance
balance = exchange.fetch_balance()
eur_balance = balance['total'][BASE_CURRENCY]
print(f"Your current {BASE_CURRENCY} balance: {eur_balance}")

# Get the current ticker price
ticker = exchange.fetch_ticker(symbol)
current_price = ticker['ask']

# Calculate the required amount of EUR to buy the target amount of USDT
required_eur_amount = TARGET_AMOUNT * current_price

if eur_balance < required_eur_amount:
    print(f"Your available {BASE_CURRENCY} balance is not sufficient to buy {TARGET_AMOUNT} {TARGET_CURRENCY}.")
else:
    # Calculate the amount of USDT to buy
    amount = TARGET_AMOUNT

    try:
        order = exchange.create_order(symbol, order_type, side, amount, price)
        print('Order created:', order)
    except Exception as e:
        print('Error:', e)

exchange = ccxt.bitvavo({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})

symbol = f"{TARGET_CURRENCY}/{BASE_CURRENCY}"
order_type = 'market'
side = 'buy'
amount = None
price = None

# Fetch balance
balance = exchange.fetch_balance()
eur_balance = balance['total'][BASE_CURRENCY]
print(f"Your current {BASE_CURRENCY} balance: {eur_balance}")

# Ensure the available balance is greater than or equal to the minimum order amount
if eur_balance < MINIMUM_EUR_AMOUNT:
    print(f"Your available {BASE_CURRENCY} balance is below the minimum order amount of {MINIMUM_EUR_AMOUNT} {BASE_CURRENCY}.")
else:
    # Get the current ticker price
    ticker = exchange.fetch_ticker(symbol)
    current_price = ticker['ask']

    # Calculate the amount of USDT to buy
    amount = eur_balance / current_price

    try:
        order = exchange.create_order(symbol, order_type, side, amount, price)
        print('Order created:', order)
    except Exception as e:
        print('Error:', e)