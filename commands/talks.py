import discord
from discord.ext import commands

class Talks(commands.Cog):
    """ Talks with user """

    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name='oi')
    async def send_hello(self, ctx):
        name = ctx.author.name
        response = f'Olá, {name}!'
        await ctx.send(response)


    @commands.command(name='segredo')
    async def secret(self, ctx):
        try:
            await ctx.author.send('Siga no insta @be.lencastre')
            await ctx.author.send('Quero biscoito 🍪')

        except discord.errors.Forbidden:
            await ctx.send('Não posso te contar um segredo! Habilite receber mensagens de qualquer pessoa do servidor (Configurações -> Privacidade e Segurança)')


    @commands.command(name='calcular')
    async def calculate_expression(self, ctx, *expression):
        response = eval(expression)
        expression = ''.join(expression)
        await ctx.send(f'A reapoata é {str(response)}')


def setup(bot):
    bot.add_cog(Talks(bot))
