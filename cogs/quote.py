from discord.ext import commands

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

def setup(bot):
    bot.add_cog(ggundam(bot))
    bot.add_cog(pokemon(bot))