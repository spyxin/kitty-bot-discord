import discord
from discord.ext import commands

class Embeded(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @commands.command()
    async def sendembed(self, ctx):
        embeded_msg = discord.Embed(title="About me", description="i'm a kitty bot, made by @aromaks <3", color=discord.Color.pink())
        embeded_msg.set_thumbnail(url="https://i.pinimg.com/736x/bd/1c/fc/bd1cfcbbd82fc71c53a24b7d090fc5d5.jpg")
        embeded_msg.add_field(name="Commands:", value=".kitty to meow, .sendembed to send an embed hehe", inline=False)
        embeded_msg.add_field(name="What do I do?", value="i'm here to meow and be fun >:3", inline=False)
        embeded_msg.add_field(name="Anything else?", value="trying to add more silly commands in the future :,] be patient, i'm dumb..", inline=False)
        embeded_msg.set_image(url="https://i.pinimg.com/736x/0b/92/27/0b92274bc38ad03d95ddf43627c7f7ca.jpg")
        embeded_msg.set_footer(text="*mreow~", icon_url=ctx.author.avatar)
        await ctx.send(embed=embeded_msg)

async def setup(bot):
    await bot.add_cog(Embeded(bot))