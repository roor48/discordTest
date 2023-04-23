from discord_webhook import DiscordWebhook

webhookUrl = open(r"./apiKey.txt", 'r').readline()
webhook = DiscordWebhook(url=webhookUrl, content = ':toolbox:')
response = webhook.execute()