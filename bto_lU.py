import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


with open('bot_token.txt', 'r') as file:
    TOKEN = file.read().strip()
bot.run(TOKEN)

