# Import the required modules
from pybit.unified_trading import HTTP
import pandas as pd

# Set up logging (optional)
import logging
logging.basicConfig(filename="pybit.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")

# You can create an authenticated or unauthenticated HTTP session.
session = HTTP(
    testnet=False,
    api_key="",
    api_secret="",
)

# Get the closed P&L data
closed_pnl_data = session.get_closed_pnl(
    category="linear",
    limit=50,
)

# Extract the list of closed P&L data
closed_pnl_list = closed_pnl_data['result']['list']

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(closed_pnl_list)

# Save the DataFrame to an Excel file
df.to_excel('closed_pnl_data.xlsx', index=False)

