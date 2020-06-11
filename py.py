import discord

@client.event
async def on_ready():
  print(''Bot is ready.)

@client.event
async def on_message(message):
  if message.content.startswith('#help'):
    await client.send_message(message.channel, '명령어 목록:\n```#help - 명령어 목록을 확인합니다.```')

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
