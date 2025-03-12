import discord
from discord.ext import commands
import os
import subprocess
import shutil
import asyncio
import git

TOKEN = "MTAxNTU5NDg5ODk4NjEyMzM2NA.GrWsiD.u1ceoKXZGeDmLG76io5kMOidrv55SEka43Miy0"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

bot.run(TOKEN)
