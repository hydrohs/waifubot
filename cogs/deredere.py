import random
from discord.ext import commands

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

def setup(bot):
    bot.add_cog(deredere(bot))