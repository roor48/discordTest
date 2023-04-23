from discord_webhook import DiscordWebhook

webhookUrl = 'https://discord.com/api/webhooks/1099561516845510676/csJKKoGLDXlZV-6rhvn8DX_p0pECVcw-D6Ki_t7WPquFlO2GINV7kWbzlccGF05IU-xP'
webhook = DiscordWebhook(url=webhookUrl, content = '||꼽구이 멍청이||')
response = webhook.execute()