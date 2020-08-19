import os
import random
import discord
import threading
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

TOKEN = os.environ['DISCORD_SECRET']

client = discord.Client()

publix_quotes = [
    "WHERE SHOPPING IS A PLEASURE",
    "REMEMBER: WE'RE ALL IN THIS TOGETHER",
    "WILL THAT BE BOAR'S HEAD OR PUBLIX?"
]

evil_publix_quotes = [
    "Ĥ̵̠̖̥͍̝̻̙̜̘̅̿̂E̶̢͔̩̺̥͍̫̲͍̤̩̠̙̎̓̓̃͒̆̃̿̏͆ͅ ̶̻̰͙̦͐͌̓̈́C̵̨̹̹̮͚̬̰̻͎̩̻͍̓̾̃̒̿̈͂͊̊̎̊̐͐͠͝Ȯ̷̡̧̞̱̻̻̺̥̙̏͆͂̂̃̌͋̈͗̓͆͂̍͝M̶̢̛̱̪͖͕͖̦̥͓͙̗͙̥͍̀̾̊̾́̕͝Ȩ̶͇͍͔̿̎̑̏̐́̾́̾͝Ṡ̶̡̞͍̥̹͖͎̞͕̍̓̓͆̒̇̊̔̌͜͝͝",
    "A̸̛̤̜̅S̶̞̟͋ ̵̜͑̓̕Í̴̢̱͉̝̃̉Ņ̴̑̑͌͝ ̵͓̙̓͒E̴̟͂̉̽A̵̟̲͒R̶͖̯̔Ṱ̵́͑͘H̴̨̗̄̒̊̕ ̶̲͇̣̔͆̎͜Ạ̸̰̉̽͠S̶̞͕̫̙̈́ ̶͉̫͓̃̇̔͛Í̷̛̬̌̊͜Ţ̸̡̫̰̉̄͝ ̸̞̟͍̾̒͂͂Í̴̢̻̼͔̎̒̽Ṡ̶̖ ̷͚̝̈́̈I̸̧̛̝N̷̨̛̝̣͙̆̕ ̴̙̻͕̑̈͘͠H̵̲̘͒͝ͅĚ̸̝̠͚̘L̸͈̗͇̣̎̓Ļ̵́̊͝",
    "N̵̢̞̠̲̈́E̷̹̟͐͒̆M̵̡̰͓̯̏͒͝͝A̶͕̎̉̾͝",
    "I̶A̷ ̵I̶A̴ ̶C̸T̴H̶U̴L̴H̵U̷ ̷F̴H̶A̴T̵G̴N̶"
]


class Client(discord.Client):
    async def background_task(self):
        pass


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        if "publix" in message.content.lower():
            await message.channel.send(random.choice(publix_quotes))
        if "xi|duq" in message.content.lower() or "xilduq" in message.content.lower():
            await message.channel.send(random.choice(evil_publix_quotes))
        else:
            if message.content.startswith("!tendies"):
                r = requests.get("http://arepublixchickentendersubsonsale.com")
                soup = BeautifulSoup(r.text, 'html.parser')
                try:
                    if "yes" in soup.title.string.lower():
                        await message.channel.send("Chicken tender subs on sale today! Only at Publix, where shopping is a pleasure.")
                    else:
                        await message.channel.send("Not this week, my dudes.")
                except:
                    await message.channel.send("Not this week, my dudes.")
client.run(TOKEN)
