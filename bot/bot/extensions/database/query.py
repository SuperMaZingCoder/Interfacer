from discord.ext import commands


class Query(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="abc")
    async def query(self, ctx, query):
        async with self.bot.database.acquire() as conn:
            res = await conn.fetch(query)
            print(str(res))
            await ctx.send(res)


def setup(bot):
    bot.add_cog(Query(bot))
