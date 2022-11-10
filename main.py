from datetime import datetime
import requests

PRICE_URL = "https://api.coingecko.com/api/v3/simple/price"

coin_ids = ['ethereum', 'bitcoin', 'cardano', 'solana', 'chainlink', 'the-graph', 'audius', 'livepeer', 'rally-2']
coin_ids_query = ','.join(coin_ids)
full_url = f"{PRICE_URL}?ids={coin_ids_query}&vs_currencies=usd"

response = requests.get(full_url)

for key, value in response.json().items():
    coin_id = key
    coin_value_usd = value['usd']
    current_datetime = str(datetime.now())
    insert_query = f"INSERT INTO crypto_prices (coin, price, ts) VALUES ('{key}', {coin_value_usd}, '{current_datetime}')"
    insert_request = requests.get(f"http://localhost:9000/exec?query={insert_query}")
