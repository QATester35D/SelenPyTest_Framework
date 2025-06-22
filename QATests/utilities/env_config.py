import os
from dotenv import load_dotenv

# Load the .env file once when this module is imported
load_dotenv()

# Access and expose env variables
python_path = os.getenv("PYTHONPATH")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Optionally expose WebClient directly if always used
from slack_sdk import WebClient
slack_client = WebClient(token=SLACK_BOT_TOKEN)