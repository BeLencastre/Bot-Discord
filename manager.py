from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
from discord.ext import commands


class Manager(commands.Cog):
    """ Manage the bot """

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Ready and connected as {self.bot.user}.')
        


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return True
        
        if 'palavrão' in message.content:
            await message.channel.send(f'Por favor, {message.author.name}, sem ofensas no chat.')
            await message.delete()


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send('Favor enviar todos os parâmetros.')
        elif isinstance(error, CommandNotFound):
            await ctx.send('O comando não existe. Digite !help para ver os comandos existentes.')
        else:
            raise error


def setup(bot):
    bot.add_cog(Manager(bot))
