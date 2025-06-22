import json
import requests
import time
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

# Get the Slack Bot token and set the webclient
load_dotenv()
slack_token=os.environ['SLACK_BOT_TOKEN']
client = WebClient(token=slack_token)

class TestSlackWebhookCall:
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
    
    def webhook_notify_general_channel(self,msg):
        return self._send_payload("#selenpytest",msg)

    def webhook_notify_ci_channel(self,msg):
        return self._send_payload("#ci-results",msg)

class TestSlackAPICall:
    def __init__(self):
        pass

    def send_slack_channel_message(self, channel_id, text):
        try:
            # Use the chat.postMessage method to send a message
            response = client.chat_postMessage(
                channel=channel_id,
                text=text
            )
            print(f"Message sent: {response['message']['text']}")
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")

#Slack API post
slackAPI=TestSlackAPICall()
channel_id = "C092KESV1K2"
message_text = "Making sure this still works #4"
slackAPI.send_slack_channel_message(channel_id, message_text)

#Slack Webhook post - need to update webhook url to post to the selenpytest channel also
webhook = os.environ['WEBHOOK_URL']
slackWebhookCalls=TestSlackWebhookCall(webhook)
result1=slackWebhookCalls.webhook_notify_general_channel("Making sure this still works #5")
result2=slackWebhookCalls.webhook_notify_ci_channel("Making sure this still works #6")
