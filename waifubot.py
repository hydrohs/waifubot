# Discord Waifubot v3.0
import os, random
from discord import client
from discord.ext import commands
from discord.ext.commands.core import command

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    for guild in bot.guilds:
        print(f'{guild.name}\n')
        members = '\n - ' .join([member.name for member in guild.members])
        print(f'{members}')

class deredere(commands.Cog, name='Tsundere/Yandere'):
    @commands.command(help='Responds with a random tsundere quote')
    async def tsundere(self,ctx):
        quotes = [
            'I-it\'s not like I\'m responding because I like you, b-b-baka!',
            'I-it\'s not like I like you or anything!',
            'B-baka!',
            'I\'m not doing this because of you!',
            'D-don\'t get the wrong idea! I just wanted to say something!',
            'The only reason I\'m bringing you lunch is because you\'re too useless to make it yourself! I-It\'s not like it means anything, baka!',
            'Geez, can\'t you even fold your clothes right? What are you, a child!? Give them here, I\'ll do it myself! Hmpf, what would you do without me around.',
            'You should be honored that I\'m even bothering to pay attention to you, baka!',
            'F-fine, you can have some of my lunch. It\'s not like it\'s a gift or anything, I just can\'t eat this much by myself! H-hmpf!'
        ]

        response = random.choice(quotes)
        await ctx.send(response)

    @commands.command(help='Responds with a random yandere quote')
    async def yandere(self, ctx):
        quotes = [
            'I\'ll cut off your hand so I can hold it forever!',
            'Nobody\'s gonna take you away from me. Not even me, see? I\'ll kill me before that happens.',
            'Anyone who gets between me and you can just die!',
            'Do you think if you ignore me I would stop following you?',
            'Roses are red, handcuffs are naughty, if you ever left me, they\'d never find your body.',
            'If I can\'t have you, no one can.'
        ]
        response = random.choice(quotes)
        await ctx.send(response)

class misc(commands.Cog, name='Misc'):
    @commands.command(name='8ball', help='Simulates a magic 8 ball')
    async def eightball(self, ctx):
        answers = [
            "It is certain.",
            'It is decidedly so.',
            'Without a doubt.',
            'Yes, definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook is good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predit now.',
            'Concentrate and ask again.',
            'Don\'t count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook is not so good.',
            'Very doubtful.'
        ]

        response = random.choice(answers)
        await ctx.send(response)

class ggundam(commands.Cog, name='G Gundam Quotes'):
    @commands.command()
    async def shiningfinga(self, ctx):
        await ctx.send('俺のこの手が光って唸る！お前を倒せと輝き叫ぶ！必殺、**シャイニングフィンガー！**')

    @commands.command()
    async def shiningfinger(self, ctx):
        await ctx.send('This hand of mine glows with an awesome power. It’s burning grip tells me to defeat you! Now here I go, **Shining Finger!**')

    @commands.command()
    async def godfinger(self, ctx):
        await ctx.send('俺のこの手が真っ赤に燃える！！勝利を掴めて轟叫ぶ！！**爆熱ゴッドフィンガー！！！**')

    @commands.command()
    async def burningfinger(self, ctx):
        await ctx.send('This hand of mine is burning red! Its loud roar tells me to grasp victory! **Erupting Burning Finger!!!**')

class pokemon(commands.Cog, name='Pokemon Quotes'):
    @commands.command()
    async def burn(self, ctx):
        await ctx.send('Hah! You better have a Burn Heal!')

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
    bot.add_cog(deredere(bot))
    bot.add_cog(misc(bot))
    bot.add_cog(ggundam(bot))
    bot.add_cog(pokemon(bot))
    bot.run(TOKEN)
except KeyboardInterrupt:
    bot.close()