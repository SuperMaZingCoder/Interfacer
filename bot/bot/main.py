from os import environ

import asyncio

import asyncpg

from bot.bot import Interfacer
from bot.extensions import EXTENSIONS


async def run():
    user = environ.get("POSTGRES_USER")
    password = environ.get("POSTGRES_PASSWORD")
    database = environ.get("POSTGRES_DB")
    credentials = {"user": user, "password": password,
                   "database": database, "host": f"db", "port": "5432"}

    retries = 20
    while retries > 0:
        try:
            async with asyncpg.create_pool(**credentials) as database:
                await database.execute(
                    "CREATE TABLE IF NOT EXISTS user_preferences("
                    "user_id BIGINT,"
                    "guild_id BIGINT,"
                    "PRIMARY KEY (user_id, guild_id)"
                    ");"
                )

                bot = Interfacer(command_prefix="!", database=database)

                for extension in EXTENSIONS:
                    bot.load_extension(extension)

                await bot.start(environ.get("TOKEN"))
                print("success")
                retries = 0

        except Exception as e:
            print(e)
            print(f"Something went wrong. Retries left: {retries}")
            retries -= 1
            await asyncio.sleep(5)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
