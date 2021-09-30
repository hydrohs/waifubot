# Discord Waifubot v3.1.0
import os
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = os.getenv('TEST_DISCORD_TOKEN')

initial_extensions = [
    'cogs.deredere',
    'cogs.misc',
    'cogs.quote',
    'cogs.robot',
    #'cogs.waifu'
    ]

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        print(f'{guild.name}\n')

@bot.event
async def on_message(message):
    notice_me = [
        'when will senpai notice me',
        'why won\'t senpai notice me',
        'why wont senpai notice me'
    ]

    for i in notice_me:
        if i in str.lower(message.content):
            await message.reply('I notice you!', mention_author=False)
            return

    await bot.process_commands(message)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(TOKEN)