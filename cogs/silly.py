import discord
from discord import app_commands
from discord.ext import commands

class Silly(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Silly is ready!")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('kitty'):
            await message.channel.send(f'mreow~')

        if message.content.startswith('kitty!'):
            await message.channel.send(f'mreow~')

        if message.content.startswith('ZIPPY!'):
            await message.channel.send(f'mreowp?')

        if message.content.startswith('woof'):
            await message.channel.send(f'*HISSS!*')

        if message.content.startswith('woof!'):
            await message.channel.send(f'*HISSS!*')

        if message.content.startswith('WOOF'):
            await message.channel.send(f'*HISSS!*')

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('mreow!')
    
        await client.process_commands(message)

    @app_commands.command(name="attack", description="kitty attack!")
    async def level(self, interaction: discord.Interaction, member: discord.Member=None):

        if member is None:
            member = interaction.user

        member_id = member.id
        guild_id = interaction.guild.id

        await interaction.response.send_message(f"<a:cathug:1439065316813574295> get attacked {member.mention}! *mreow~*")

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

    class VibeCheck(discord.ui.View):
        def __init__(self):
            super().__init__()

        @discord.ui.button(label="Vibe check!", style=discord.ButtonStyle.green, emoji="🥀")
        async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
            await button.response.send_message("success! you're awesome >:3")

        @discord.ui.button(label="Click here!", style=discord.ButtonStyle.red, emoji="😼")
        async def two_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
            await button.response.send_message("you're very submissive...")

        @discord.ui.button(label="Mreowp~", style=discord.ButtonStyle.blurple, emoji="🐈")
        async def three_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
            await button.response.send_message("*purrr*")

    @bot.tree.command(name="vibes", description="kitty gives u a vibe check")
    async def vibes(self, interaction: discord.Interaction):
        view = VibeCheck()
        await interaction.response.send_message(view=view)

    class Menu(discord.ui.Select):
        def __init__(self):
            options = [
                discord.SelectOption(
                    label="cats", 
                    description="obviously the best animal",
                    emoji="🐈"
                    ),

                discord.SelectOption(
                    label="dogs", 
                    description="they're cool too, sure",
                    emoji="🐕"
                    ),
                discord.SelectOption(
                    label="birds", 
                    description="omfg yessss >:3",
                    emoji="🐦"
                    ),
            ]

            super().__init__(placeholder="Choose the best animal", min_values=1, max_values=1, options=options)

        async def callback(self, interaction: discord.Interaction):
            if self.values[0] == "cats":
                await interaction.response.send_message("cats are the rulers of the world >:3")

            elif self.values[0] == "dogs":
                await interaction.response.send_message("dogs can rule on the side of cats :]")

            elif self.values[0] == "birds":
                await interaction.response.send_message("birds: our sky warriors UuU")


    class MenuView(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.add_item(Menu())


    @app_commands.command(name="animals", description="which animal is the best?")
    async def myMenu(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=MenuView())

async def setup(bot):
    await bot.add_cog(Silly(bot))