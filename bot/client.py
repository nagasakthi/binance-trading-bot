from binance.client import Client
from config import API_KEY, API_SECRET
import time

def get_client():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    # ✅ Correct universal fix
    server_time = client.get_server_time()['serverTime']
    system_time = int(time.time() * 1000)
    client.timestamp_offset = server_time - system_time

    return client