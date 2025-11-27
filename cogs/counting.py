import discord
from discord import app_commands
from discord.ext import commands

class Counting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Counting is ready!")

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

    class Counter(discord.ui.View):
        @discord.ui.button(label="0", style=discord.ButtonStyle.grey, emoji="😺")
        async def count(self, interaction: discord.Interaction, button: discord.ui.Button):
            number = int(button.label) if button.label else 0
            button.label = str(number + 1)

            await interaction.response.edit_message(view=self)

        # Source - https://stackoverflow.com/a
        # Posted by Judev1, modified by community. See post 'Timeline' for change history
        # Retrieved 2025-11-23, License - CC BY-SA 4.0

        # Gets the counter
            try:
                open("counter.txt", "x").close()
                counter = 0
            except:
                with open("counter.txt", "r") as file:
                    counter = int(file.readlines()[0])

        # Updates the counter
            with open("counter.txt", "w") as file:
                file.write(str(counter))

        # ...or if you're going to be updating it a lot
            file = open("counter.txt", "w")
            file.write(str(counter))

            file.close() # Once you're completley done

    class CountView(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.add_item(Counter())


    @app_commands.command(name="meow", description="click to meow!")
    async def myCounter(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=CountView())

async def setup(bot):
    await bot.add_cog(Counting(bot))