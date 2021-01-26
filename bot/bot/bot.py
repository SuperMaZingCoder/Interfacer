from discord import Embed
from discord.ext import commands


class Interfacer(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.database = kwargs["database"]

    @staticmethod
    async def on_command_completion(ctx):
        command = str(ctx.command)
        if command == "optin":
            embed = Embed(
                title="**User Successfully Opted In**",
                color=0x4BB543,
                description=(
                    f"`{ctx.author.name}` has opted in for API usage in the server `{ctx.guild.name}`. "
                    "To opt out from API usage in this server, run `!optout`."
                )
            )
            await ctx.send(embed=embed)
        elif command == "optout":
            embed = Embed(
                title="**User Successfully Opted Out**",
                color=0x4BB543,
                description=(
                    f"User `{ctx.author.name}` has opted out from API usage in the server `{ctx.guild.name}`. "
                    "To opt in for API usage in this server again, run `!optin`."
                )
            )
            await ctx.send(embed=embed)
