from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url=open(r"./apiKey.txt", 'r').readline(), content = 'Hello')
response = webhook.execute()