import json
import os

import slack
from dotenv import load_dotenv

def load_env_variable():
    load_dotenv()

def get_slack_bot_token():
    token = os.environ.get("SLACK_BOT_TOKEN")
    if(token is None):
        print("Slack Bot Token doesn't exist")
        exit()
    return token

def get_slack_client():
    return slack.WebClient(token=get_slack_bot_token())

class HelloBot():
    def __init__(self):
        self.user_name = input("Enter Slack Username: ")
        self.slack_client = get_slack_client()
        self.message = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Hey <@{}> !! :tada:\n I am a new bot :hugging_face:\n Do you like me?".format(self.user_name)
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Yes"
                        },
                        "style": "primary",
                        "value": "yes"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "No"
                        },
                        "style": "danger",
                        "value": "no"
                    }
                ]
            }
        ]

    def get_user_id(self):
        api_call = self.slack_client.api_call("users.list")
        assert api_call is not None
        users = api_call.get("members")
        for user in users:
            if "name" in user and self.user_name in user.get("name") and not user.get("deleted"):
                return user.get("id")
        print("user {} doesn't exist".format(self.user_name))
        exit()

    def post_message(self):
        user_id = self.get_user_id()
        response = self.slack_client.chat_postMessage(channel=user_id, blocks=self.message)
        print(response)

if __name__ == '__main__':
    load_env_variable()
    hello_bot = HelloBot()
    hello_bot.post_message()
