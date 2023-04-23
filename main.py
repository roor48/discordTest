import requests
discord = "https://discord.com/api/webhooks/1099561516845510676/csJKKoGLDXlZV-6rhvn8DX_p0pECVcw-D6Ki_t7WPquFlO2GINV7kWbzlccGF05IU-xP"
headers = {
    'Content-Type':'application/json',
}
data = '{"content":"asd!"}'
response = requests.post(discord, headers=headers, data=data)