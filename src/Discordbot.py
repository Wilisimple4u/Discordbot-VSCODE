# bot.py
from utyl import *
import discord
import os
import dotenv
dotenv.load_dotenv()


# load_dotenv()
#TODO remeber to add a method to grab the token from a text file and insert it into TOKEN. DONE
TOKEN = os.getenv('Token')
GUILD = 'TEST server'


client = discord.Client(intents=discord.Intents.all())

# Kommentar fra Sondre:
# ======================
# PS: Her trenger du ikke gjenta ordene, men heller bruke en funksjon som konverterer alt til lowercase (word.lower()),
# da blir det mindre arbeid :)
# (Jeg endra koden for å vise)

# GAMMEL, uten lowercase:
#badWords = [
#    "fuck", "Fuck", "FUCK",
#    "shit", "Shit", "SHIT",
#    "hell", "Hell", "HELL",
#    "dick", "Dick", "DICK",
#    "bitch", "Bitch", "BITCH",
#    "asshole", "Asshole", "ASSHOLE",
#    "goddamn", "God damn",
#    "Jesus", "jesus",
#    "nigger", "Nigger", "NIGGER",
#]

# NY, med lowercase:
badWords = [
    "fuck",
    "shit",
    "hell",
    "dick",
    "bitch",
    "asshole",
    "goddamn", "god damn",
    "jesus",
    "nigger",
]


theList = [
    "!list",    "!hi",
        "!wow",    "!error",
        "!great success",
        "!thanks",  "!intro",
        "!greet",   "!clear x",
        "!test",    "!clear last",
]


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!list":
        await message.channel.send("Here is a list of commands:")
        await message.channel.send(theList)
        return

    # NY, med lowercase:
    if any(word.lower() in message.content for word in badWords):
        await message.channel.purge(limit=1)
        await message.channel.send("There will be no swearing in my christian minecraft discord server!")
        return

    if message.content == "!clear last":
        await message.channel.purge(limit=2)
        return

    if message.content.startswith('!clear'):
        clearValue = message.content.split(' ')
        if len(clearValue) == 2 and clearValue[1].isdigit():
            clearNumber = int(clearValue[1])
        else:
            return
        if clearNumber <= 30:
            await message.channel.purge(limit=clearNumber)
            await message.channel.send("deleted " + str(clearNumber) + " messages")
        else:
            await message.channel.send("clear number too high or other unexpected error")
        return


    if message.content == "!test":
        await message.channel.send(f"y or n")

        # This will make sure that the response will only be registered if the following
        # conditions are met:
        def check(msg):
            return msg.author == msg.author and msg.channel == msg.channel and \
                msg.content.lower() in ["y", "n"]

        msg = await client.wait_for("message", check=check)

        if msg.content.lower() == "y":
            await message.channel.send("You said yes!")
        elif msg.content.lower() == "n":
            await message.channel.send("You said no!")

    if message.content == "!hi":
        await message.channel.send("wow")
        return

    if message.content == "!thanks":
        await message.channel.send("You are welcome hope to be of service later")
        return

    if message.content == "!greet":
        await message.channel.send("Hi, I am Jordi, I can be helpful sometimes.")
        return

    if message.content == "!intro":
        await message.channel.send("Hi my name is Jordi, I will help with whatever is in my ability")
        return

    if message.content == "!wow":
        await message.channel.send("error")
        return

    if message.content == "!error":
        await message.channel.send("hi")
        return

    if message.content == "!great success":
        await message.channel.send("Put up the streamers, blow up the ballons, we have to celebrate this.")
        return



@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

client.run(TOKEN)
