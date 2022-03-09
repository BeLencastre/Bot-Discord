import requests
import discord
from discord.ext import commands

class Smart(commands.Cog):
    """ Smart commands """

    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name='cripto')
    async def crypto(ctx, coin, base='BUSD'):
        try:
            response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}')

            data = response.json()
            price = data.get('price')

            if price:
                await ctx.send(f'Valor de {coin.upper()}/{base.upper()} é {price}')
            else:
                await ctx.send(f'O par {coin.upper()}/{base.upper()} é inválido.')

        except Exception as error:
            await ctx.send('Ops, deu algum erro. Tente novvamente em alguns instantes.')
            print(error)


    @commands.command(name='imagem')
    async def get_random_image(self, ctx, width, height):
        url_image = f'https://picsum.photos/{width}/{height}'

        embed_image = discord.Embed(
            title = 'Resultado da busca de imagem',
            description = 'Essa busca é totalmente aleatória',
            color = 0x0000FF
        )

        embed_image.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed_image.set_footer(text=f'Feito por {self.bot.user.name}', icon_url=self.bot.user.avatar_url)

        embed_image.add_field(name='Fonte', value='Utilizamos a API do Picsum')
        embed_image.add_field(name='Parâmetros', value='{largura}/{altura}')
        embed_image.add_field(name='Atenção', value='A miniatura sempre será a mesma. Clique para acessar a imagem gerada.', inline=False)
        embed_image.add_field(name='Link de Exemplo', value='https://picsum.photos/1920/1080', inline=False)

        embed_image.set_image(url=url_image)
        await ctx.send(embed=embed_image)


def setup(bot):
    bot.add_cog(Smart(bot))
