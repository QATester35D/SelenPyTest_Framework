import json
import requests
import time

class TestAPIGetCall:

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

        response = requests.post(
            webhook_url,
            data={'payload': json.dumps(payload)}
        )

        if response.status_code != 200:
            raise ValueError(f"Request to Slack returned error {response.status_code}, response: {response.text}")
        else:
            print(f"Notification sent to {channel}")

apiCalls=TestAPIGetCall()
webhook = "https://hooks.slack.com/services/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"
apiCalls.send_slack_notification(
    channel="#selenpytest",
    username="selenpytest",
    text="This is posted from python and VSCode to #selenpytest and comes from a bot named selenpytest.",
    icon_emoji=":ghost:",
    webhook_url=webhook
)
