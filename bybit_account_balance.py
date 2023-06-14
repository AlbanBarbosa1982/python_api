# Import HTTP from the unified_trading module.
from pybit.unified_trading import HTTP

# Set up logging (optional)
import logging
logging.basicConfig(filename="pybit.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")


# You can create an authenticated or unauthenticated HTTP session.
# You can skip authentication by not passing any value for the key and secret.

session = HTTP(
    testnet=False,
    api_key="",
    api_secret="",
)

print(session.get_wallet_balance(accountType="CONTRACT"))
