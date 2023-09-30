from tgtg import TgtgClient 
import time
from dotenv import load_dotenv
import os
import sys

load_dotenv()

client = TgtgClient(os.getenv('access_token'),
                    os.getenv('refresh_token'), 
                    os.getenv('user_id'),
                    os.getenv('cookie'))


old_data = client.get_items(
        favorites_only=False,
        latitude=43,
        longitude=0,
        radius=5,
        with_stock_only=True
    )

sys.stdout.reconfigure(encoding='utf-8')


while True:
    data = client.get_items(
        favorites_only=False,
        latitude=43,
        longitude=0,
        radius=5,
        with_stock_only=True
    )

    for i in range(len(data)):
        item_id = data[i]['item']['item_id']
        item_name = data[i]['item']['name']
        item_description = data[i]['item']['description']

        print(item_id, item_description, item_name)

    time.sleep(1800)
