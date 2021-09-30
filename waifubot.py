# Discord Waifubot v3.1.0
import os, deredere, misc, quote, robot, waifu
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = os.getenv('TEST_DISCORD_TOKEN')

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

try:
    bot.add_cog(deredere.deredere(bot))
    bot.add_cog(misc.misc(bot))
    bot.add_cog(quote.ggundam(bot))
    bot.add_cog(quote.pokemon(bot))
    bot.add_cog(robot.robot(bot))
    bot.add_cog(waifu.waifu(bot))
    bot.run(TOKEN)
except KeyboardInterrupt:
    bot.close()