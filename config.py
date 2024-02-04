import os

# Pyrogram API credentials
API_ID = int(os.environ.get("API_ID", 18923971))
API_HASH = os.environ.get("API_HASH", "78f80e014130f4ec3964550d4e87af61")

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6801681333:AAHmfygxg6Obl84JvDu915Nwxnu2v_2zRUk")

# Pyrogram session name
SESSION_NAME = os.environ.get("SESSION_NAME", "ForwadBot")

# MongoDB URI (if you're using MongoDB)
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority")
