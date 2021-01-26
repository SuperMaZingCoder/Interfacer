from discord.ext import commands


class DeleteUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def optout(self, ctx):
        async with self.bot.database.acquire() as conn:
            query = "DELETE FROM user_preferences WHERE user_id = $1 AND guild_id = $2"
            await conn.execute(query, ctx.author.id, ctx.guild.id)


def setup(bot):
    bot.add_cog(DeleteUser(bot))
