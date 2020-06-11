import discord
import os
import datetime


client = discord.Client()


@client.event
async def on_ready():
  print("login")
  print(client.user.name)
  print(client.user.id)
  print("------------------")
  await client.change_presence(game=discord.Game(name='appealbot.xyz', type=1))

@client.event
async def on_member_join(member):
  channel = discord.utils.get(member.guild.channels, name="welcome")
  await channel.send(f"[member.mention]님 환영합니다!")

@client.event
async def on_message(message):
  if message.content == "!":
    if message.channel.is_private and message.author.id != "718421206059057234":
      await client.send_message(message.channel, "```올바르지 않는 명령어 형식입니다.```")
  else:
    if message.content[1:5] == "help":
      if message.channel.is_private and message.author.id != "718421206059057234":
        await client.send_message(message.channel, "Commands:\n```!help - Appeal Bot에 대한 명령어들을 확인합니다.\n!appeal (playerName) - 당신의 벤 또는 뮤트 항소를 합니다.```")
    if message.content[1:7] == "appeal":
      if message.channel.is_private and message.author.id != "718421206059057234":
        if message.content[8:]:
          await client.send_message(discord.utils.get(client.get_all_channels(), id="718434205448536066"), "@everyone\n[ " + message.author.mention + "님의 항소 정보 ]\n디스코드 이름: " + message.author.mention + "\n디스코드 아이디: " + message.author.id + "\n마인크래프트 닉네임: " + message.content[8:])
          await client.send_message(message.channel, "```성공적으로 항소하셨습니다!```")
        else:
          await client.send_message(message.channel, "```마인크래프트 닉네임을 작성하여 주세요.```")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
