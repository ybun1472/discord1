import discord, asyncio
import datetime
import os

token = "Njg1MzIyMzQ2MTE4MjUwNTA4.XmHCLA.6Zl3pyc5NP9n7aOZaS0tlrusaCs"
client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("바늘님 노예로 일하는중! :D"))
  print("시작!")
  print(client.user.name)
  print(client.user.id)
  print("------------------")

@client.event
async def on_message(message):
  if message.author.bot:
    return None

  if message.content.startswith("!내정보"):
   date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
   embed = discord.Embed(color=0x00ff00)
   embed.add_field(name="이름", value=message.author.name, inline=True)
   embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
   embed.add_field(name="디코가입일", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일 ", inline=True)
   embed.add_field(name="아이디", value=message.author.id, inline=True)
   embed.set_thumbnail(url=message.author.avatar_url)
   await message.channel.send(embed=embed)

  if message.content == "!노예":
    await message.channel.send("48468567799(자발적 노예) 프리뮬러_(스샷노예)뭉_치(노예(바늘님이잡아옴)")

  if message.content == "!트위치":
    await message.channel.send("https://www.twitch.tv/needle_kim/")

  if message.content == "바보":
    await message.channel.send("너가 더 바보지롱 (-﹏-。)")

  if message.content == "!바늘":
    await message.channel.send("너의 마음을 바늘이가 콕 콕 우리 앞으로 오래봐요")

  if message.content == "우욱":
    await message.channel.send("왜구려냥 (¬､¬)")

  if message.content == "?":
    await message.channel.send("갈고리 수집즁....(o´ω`o)")

  if message.content == "야발":
    await message.channel.send("야발?? 너 기강방으로와 (‘•̀ ▽ •́ )φ")

  if message.content == "ㅇㅅㅇ":
    await message.channel.send("또잉... ( ‘︿’ )")

  if message.content == "!4846":
    await message.channel.send("죄수번호 4846 조용히해라! ̿̿ ̿̿ ̿’̿’̵͇̿̿з=༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽ ")

  if message.content == "ㅇㅅㅇr`":
    await message.channel.send(" 코딱지 던지지 말라냥....( Ｔ▽Ｔ ) ")

  if message.content == "ㅇㅅㅇr'":
    await message.channel.send(" 코딱지 던지지 말라냥....( Ｔ▽Ｔ ) ")

  if message.content == "ㅇㅅaㅇ":
    await message.channel.send("긁적거리지말라냥... ~(˘▾˘)~")

  if message.content.startswith("!뮤트"):
    author = message.guild.get_member(int(message.content[4:22]))
    role = discord.utils.get(message.guild.roles, name="뮤트")
    await author.add_roles(role)

  if message.content.startswith("!언뮤트"):
    author = message.guild.get_member(int(message.content[5:23]))
    role = discord.utils.get(message.guild.roles, name="뮤트")
    await author.remove_roles(role)


access_token = os.environ["BOT_TOKEN"  
client.run(access_token)
