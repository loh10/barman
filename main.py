import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = "", description = "Barman de yopiland")

@bot.command()
async def salut(ctx):
    await ctx.send("Bonjour")

@bot.command()
async def Salut(ctx):
    await ctx.send("Bonjour")

@bot.command()
async def bonjour(ctx):
    await ctx.send("Bonjour")

@bot.command()
async def Bonjour(ctx):
    await ctx.send("Bonjour")

@bot.command()
async def slt(ctx):
    await ctx.send("Bonjour")

@bot.command()
async def cc(ctx):
    await ctx.send("Bonjour")

@bot.command()
async def re(ctx):
    await ctx.send("Rebonjour")

@bot.command()
async def Bonsoir(ctx):
    await ctx.send("Bonsoir")

@bot.command()
async def bonsoir(ctx):
    await ctx.send("Bonsoir")

@bot.command()
async def yo(ctx):
    await ctx.send("Bonjour")

@bot.event
async def on_ready():
    print("Ready !")    

bot.run("OTA1NzcxNDkxMjQ3OTE5MTM0.YYO7bw.XlKS8KxB-KPeZf_Eh3RiLTR1u4w")