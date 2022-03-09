from discord.ext import commands, tasks
from datetime import datetime

class Dates(commands.Cog):
    """ Work with dates """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()
    

    @tasks.loop(hours=1)
    async def current_time(self):
        time = datetime.now()
        time = time.strftime('%d/%m/%Y às %H:%M:%S')

        channel = self.bot.get_channel(949685443312648236)
        await channel.send(f'Data atual ➢ {time}')


def setup(bot):
    bot.add_cog(Dates(bot))
