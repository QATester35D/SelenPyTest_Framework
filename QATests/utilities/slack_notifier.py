import json
import requests
import time

class TestAPIGetCall:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def _send_payload(self, channel, msg):
        payload = {
            "channel": channel,
            "username": "selenpytest",
            "text": msg,
            "icon_emoji": ":ghost:"
        }

        response = requests.post(self.webhook_url, data={'payload': json.dumps(payload)})
        return response.status_code

    def send_slack_notification(self, channel, username, text, icon_emoji, webhook_url):
        """
            Sends a message to a Slack channel using an incoming webhook.
            Args:
                channel (str): Slack channel (e.g., "#selenpytest")
                username (str): Display name of the bot
                text (str): Message text
                icon_emoji (str): Emoji to use as icon (e.g., ":ghost:")
                webhook_url (str): Slack webhook URL
        """
        payload = {
            "channel": channel,
            "username": username,
            "text": text,
            "icon_emoji": icon_emoji
        }

        #This worked
        # response = requests.post(self.webhook_url, data={'payload': json.dumps(payload)})

        if response.status_code != 200:
            raise ValueError(f"Request to Slack returned error {response.status_code}, response: {response.text}")
        else:
            print(f"Notification sent to {channel}")
