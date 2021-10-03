import discord
import colorama
from colorama import init, Fore, Back, Style
init(convert=True)
from discord.ext import commands
from discord.utils import get
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
import ctypes
#########################################
client = commands.Bot(command_prefix='.')

ctypes.windll.kernel32.SetConsoleTitleW("Logging...")
token = "" #put token here

@client.event
async def on_connect():
  print(f'''{Fore.RED}
╦═╗╔═╗╦ ╦╦═╗
╠╦╝╠═╣║║║╠╦╝
╩╚═╩ ╩╚╩╝╩╚═
{Fore.RESET}---------------------------
{Fore.RED}Logged In As: {Fore.RESET}{client.user.name}
{Fore.RED}In: {Fore.RESET}{len(client.guilds)} Guilds
{Fore.RESET}--------------------------------
  ''')

@client.event
async def on_message(message):
  try:
    if message.channel.id == 891970875736358932: #replace this with the id  of the channel/gc you want to log
      async for mesg in message.channel.history(limit=1):
        sus = "abcd" # Enter your webhook here
        async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url(str(sus), adapter=AsyncWebhookAdapter(session))
          await webhook.send(mesg.clean_content, username = message.author.display_name, avatar_url=message.author.avatar_url)
          print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}] {message.channel.name} {Fore.RESET}-> {Fore.RED}{message.author}: {Fore.RESET}{mesg.clean_content}")
  except:
    print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}] {message.guild.name} {Fore.RESET}-> {Fore.RED}{message.author}:{Fore.MAGENTA} Member has sent an image/embed")

      
client.run(token, bot=False)
