import discord
import discord.utils
from discord.ext import commands
import os
import datetime

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
allowed_mentions = discord.AllowedMentions(everyone = True)

@bot.slash_command(name="ping")
async def ping(ctx):
  await ctx.respond(f"Pong! {round(bot.latency * 1000)}ms")

@bot.slash_command(name="session", description="Start a session")
async def session(ctx):
  role = discord.utils.get(ctx.guild.roles, name="Senior Leadership Team")

  if role not in ctx.author.roles:
    await ctx.respond("You do not have the required role to start a session!",ephemeral=True)
    return

  await ctx.respond(f' **Session Commencing**\n \nThe school gates have now opened for {datetime.datetime.today().strftime("%A %d %B %Y")} session. We invite pupils to begin making their way towards the campus, and we look forward to the school day ahead. Should you require assistance, \nPlease speak to an on-site member of staff of contact a member of our support team via ticket.\n\n**Host:** {ctx.author.mention}\n**Campus link:** https://www.roblox.com/games/17034428302/testhshhhss @everyone ', allowed_mentions = allowed_mentions)

@bot.slash_command(name="results", description="Declare application results")
async def results(ctx, passed: discord.Member, rank: discord.Role):
  role = discord.utils.get(ctx.guild.roles, name="Senior Leadership Team")

  if role not in ctx.author.roles:
    await ctx.respond("You do not have the required role to declare results!",ephemeral=True)
    return

  await passed.add_roles(rank)
  await passed.send(f'🎊 | Hello, Thank you for applying for **{rank.name}** Congratulations, SLT have accepted you into the  team. You have been roled and futher information will be given.')
  await ctx.respond("The applicant has been notified of the results.")



bot.run(os.environ['TOKEN'])
