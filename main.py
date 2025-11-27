import discord
from discord.ext import commands, tasks
import os
import asyncio
from itertools import cycle
import logging
from dotenv import load_dotenv
import sqlite3

load_dotenv(".env")
TOKEN: str = os.getenv("TOKEN")

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

bot_statuses = cycle(["mreow!", "murrr~", "HISSS!", "it's a wip, hush!"])

@tasks.loop(seconds=30)
async def change_bot_status():
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))
    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {len(synced_commands)} commands.")
    except Exception as e:
        print("An error with syncing application commands has occured: ", e)

@bot.event
async def on_guild_join(guild):
    conn = sqlite3.connect("./cogs/main.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Guilds (guild_id) VALUES (?)", (guild_id,))
    conn.commit()
    conn.close()

@bot.event
async def on_guild_remove(guild):
    conn = sqlite3.connect("./cogs/main.db")
    cursor = conn.cursor()
    cursor.execute("DELETE * FROM Guilds WHERE guild_id = ?", (guild_id,))
    conn.commit()
    conn.close()

@bot.tree.command(name="kitty", description="kitty goes meow!")
async def meow(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} *mreow~*")

@bot.event
async def on_ready():
    print("Kitty is ready!")
    change_bot_status.start()

class MyModal(discord.ui.Modal, title="Report User"):
    user_id = discord.ui.TextInput(label="User ID:", style=discord.TextStyle.short, placeholder="enter user id (ex: 123456789012345678)")
    reason = discord.ui.TextInput(label="Reasons:", style=discord.TextStyle.paragraph, placeholder="enter the reason for the report")

    async def on_submit(self, interaction: discord.Interaction):
        if len(str(self.user_id)) > 18:
            await interaction.response.send_message("*HISS!* user id is invalid", ephemeral=True)
            return

        await interaction.response.send_message(f"*mreow~* thank u for reporting {self.user_id} for {self.reason}!", ephemeral=True)

@bot.tree.command(name="report", description="report a user for a specific reason")
async def report(interaction: discord.Interaction):
    modal = MyModal()
    await interaction.response.send_modal(modal)

@bot.command()
async def kitty(ctx):
    await ctx.send(f"*mreow~* {ctx.author.mention}")

async def Load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await Load()
        await bot.start(TOKEN)

asyncio.run(main())