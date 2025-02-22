import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import get_spamming_text

load_dotenv()

# 봇 설정
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

spamming = False
TOKEN = os.getenv("DISCORD_TOKEN")
spamming_text = get_spamming_text.spam_text

@bot.command()
async def start_spam(ctx):
    global spamming
    spamming = True
    while spamming == True:
        await ctx.send(spamming_text)

@bot.command()
async def stop_spam(ctx):
    global spamming
    spamming = False
    await ctx.send("# Spamming has been stopped.")

# 봇 토큰으로 로그인
bot.run(TOKEN)
