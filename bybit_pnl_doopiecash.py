from openpyxl import load_workbook
from pybit.unified_trading import HTTP
import pandas as pd

# Je sessie en het ophalen van de gegevens blijven hetzelfde
session = HTTP(
    testnet=False,
    api_key="",
    api_secret="",
)

closed_pnl_data = session.get_closed_pnl(
    category="linear",
    limit=50,
)

closed_pnl_list = closed_pnl_data['result']['list']

# Transformeer de gegevens om alleen de gewenste kolommen te bevatten
# Dit is een voorbeeld, je moet de correcte velden van je gegevens gebruiken
df = pd.DataFrame(closed_pnl_list)[['tradeId', 'tradeTime', 'symbol', 'asset', 'orderType', 'side', 'risk', 'entryPrice', 'stopPrice', 'stopPercentage', 'orderQty', 'contracts', 'RR', 'Tp1', 'Tp2', 'Tp3', 'Tp4', 'exitPrice', 'pnlBTC', 'pnlUSD', 'notes']]

# Laad het bestaande Excel-bestand
book = load_workbook('existing_file.xlsx')

# Creëer een pandas ExcelWriter object met de geladen workbook
writer = pd.ExcelWriter('DoopieCash-OrderDagboek-v1.1.xlsx', engine='openpyxl') 
writer.book = book

# Schrijf de DataFrame naar het derde werkblad, je kunt de naam aanpassen naar wat je wilt
df.to_excel(writer, sheet_name='Orderdagboek', index=False)

# Sla de wijzigingen op
writer.save()
