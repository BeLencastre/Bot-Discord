from discord.ext import commands

class Reactions(commands.Cog):
    """ Assigns roles according to user reactions """

    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == '🚹':
            role = user.guild.get_role(949775329428389888)
            await user.add_roles(role)
        elif reaction.emoji == '🚺':
            role = user.guild.get_role(949775484332437525)
            await user.add_roles(role)
        
def setup(bot):
    bot.add_cog(Reactions(bot))
