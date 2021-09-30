import random
from discord.ext import commands

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

def setup(bot):
    bot.add_cog(misc(bot))