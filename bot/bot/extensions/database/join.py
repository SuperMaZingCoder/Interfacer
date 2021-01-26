from discord.ext import commands


class CreateUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def optin(self, ctx):
        async with self.bot.database.acquire() as conn:
            query = "INSERT INTO user_preferences(user_id, guild_id) VALUES ($1, $2)"
            await conn.execute(query, ctx.author.id, ctx.guild.id)


def setup(bot):
    bot.add_cog(CreateUser(bot))
