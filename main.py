import json
from discord_webhook import DiscordWebhook


with open("./apiKey.json", 'r') as file:
    webhookUrl = json.load(file)
webhook = DiscordWebhook(url=webhookUrl, content = ':toolbox:')
response = webhook.execute()