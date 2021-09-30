from discord.ext import commands

class waifu(commands.Cog, name='Get a Waifu!'):
    @commands.command(help='Responds with a random waifu')
    async def waifu(self, ctx):
        await ctx.send('Luka')

def setup(bot):
    bot.add_cog(waifu(bot))