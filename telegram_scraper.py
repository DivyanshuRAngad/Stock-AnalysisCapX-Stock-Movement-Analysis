
from telethon.sync import TelegramClient

# Telegram API credentials
api_id = "your_api_id"
api_hash = "your_api_hash"
channel_name = "target_channel_name"

# Connect to Telegram
client = TelegramClient("session_name", api_id, api_hash)
client.start()

# Scrape messages
messages = []
for message in client.iter_messages(channel_name, limit=100):
    messages.append({"Date": message.date, "Message": message.text})

import pandas as pd
df = pd.DataFrame(messages)
df.to_csv("data/telegram_data.csv", index=False)
print("Data saved to telegram_data.csv")
