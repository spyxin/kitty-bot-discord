import discord
from discord.ext import commands
from discord import app_commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# idk what im doing... the bot ones give me errors sometimes >:C

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True
intents.members = True
# Source - https://stackoverflow.com/a
# Posted by thecalendar
# Retrieved 2025-11-24, License - CC BY-SA 4.0

bot = commands.Bot(command_prefix="!", intents=intents,
                   case_insensitive=False,)


# Source - https://stackoverflow.com/a
# Posted by Bushy8903, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-24, License - CC BY-SA 4.0

from typing import Literal, Optional

@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")


class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=1432880893936140450)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f'Error syncing commands: {e}')

    async def on_member_join(member):
        await member.send(f"mreow~ *welcome to the server* {member.name}*!*")

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

client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=aiyyayay)


@client.tree.command(name="kitty", description="kitty go meow!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("mreowp~")

@client.tree.command(name="attack", description="kitty attack!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("<a:cathug:1439065316813574295>")

@client.tree.command(name="print", description="kitty prints!", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

@client.tree.command(name="intro", description="kitty info!", guild=GUILD_ID)
async def printer(interaction: discord.Interaction):
    embed = discord.Embed(title="Mreow!", url="https://www.youtube.com/watch?v=AxE4TltnvjI", description="i'm a kitty >:3", color=discord.Colour.light_theme())
    embed.set_thumbnail(url='https://i.pinimg.com/736x/e8/ce/e3/e8cee33facd4a26c8907e31e13e712aa.jpg')
    embed.add_field(name="About me:", value="i'm a bot made by @aromaks! <a:catwave:1442245430124482590>", inline=False)
    embed.add_field(name="What do I do?", value="i go meow :3")
    embed.set_footer(text="mreowp~ *purr*")
    embed.set_author(name=interaction.user.name, url="https://www.youtube.com/@aromaksim", icon_url="https://i.pinimg.com/736x/4f/9b/05/4f9b05aa280d7ae970885b1b669d4431.jpg")
    await interaction.response.send_message(embed=embed)


class Counter(discord.ui.View):
    @discord.ui.button(label="0", style=discord.ButtonStyle.green, emoji="😺")
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


@client.tree.command(name="cat", description="click to meow!", guild=GUILD_ID)
async def myButton(interaction: discord.Interaction):
    await interaction.response.send_message("mreow~", view=Counter())

class View(discord.ui.View):
    @discord.ui.button(label="Vibe check!", style=discord.ButtonStyle.green, emoji="🥀")
    async def button_callback(self, button, interaction):
        await button.response.send_message("success! you're awesome >:3")

    @discord.ui.button(label="Click here!", style=discord.ButtonStyle.red, emoji="😼")
    async def two_button_callback(self, button, interaction):
        await button.response.send_message("you're very submissive...")

    @discord.ui.button(label="Mreowp~", style=discord.ButtonStyle.blurple, emoji="🐈")
    async def three_button_callback(self, button, interaction):
        await button.response.send_message("*purrr*")

@client.tree.command(name="vibes", description="click for a vibe check!", guild=GUILD_ID)
async def myButton(interaction: discord.Interaction):
    await interaction.response.send_message(view=View())



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


@client.tree.command(name="animals", description="which animal is the best?", guild=GUILD_ID)
async def myMenu(interaction: discord.Interaction):
    await interaction.response.send_message(view=MenuView())


client.run(token idk lol), log_handler=handler, log_level=logging.DEBUG)