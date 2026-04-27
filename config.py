import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN  = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set")
if not WEBAPP_URL:
    raise RuntimeError("WEBAPP_URL not set")
``
