import discord, os, dotenv
from discord.ext import commands

import data
import requests
import json
import asyncio

dotenv.load_dotenv()
TOKEN = '!'
PREFIX = os.getenv('PREFIX')

bot = commands.Bot(command_prefix=TOKEN,
                   case_insensitive=True,
                   help_command=None)


def data():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def text():
    try:
        with open(f'lang/{data()["bot_lang"]}.json', 'r',
                  encoding='utf-8') as f:
            return json.load(f)
    except:
        print('Invalid lang in settings')
        exit()


response_lang = 'en' if data()['Response lang'] == '' else data(
)['Response lang']
request_lang = 'en' if data()['Search lang'] == '' else data()['Search lang']


@bot.command(hidden=True)
async def help(ctx, *, command=None):
    "Get some dancing help"
    emb = discord.Embed(title="8H Bot | Help",
                        colour=discord.Colour.blurple())
    emb.set_thumbnail(url="")
    if command:
        c = bot.get_command(command)
        if not c:
            emb = discord.Embed(description="Nah, that's not a command",
                                colour=discord.Colour.red())
            return await ctx.send(embed=emb)
        emb.description = f"**`{c.name} {c.signature}`**\n*{c.help}*"
        return await ctx.send(embed=emb)
    res = ""
    for a in bot.commands:
        if a.name != "jishaku":
            if not a.hidden:
                res += f"[**{a.name}**] {a.help}\n"
    emb.description = res
    await ctx.send(embed=emb)



@bot.command(name='clear', help='this command will clear messages')
# @commands.has_role('mod')
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)



# Events
@bot.event
async def on_ready():

    print(f"Started The Bot {bot.user.name} in {len(bot.guilds)} Servers!")
    activity = discord.Game(name="!movies | Free Movies And TV Shows | By daar#1000", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Connected To DaarServers")





# Commands. Should eventually start using cogs, but this is good for now
@bot.command(
    name='movies',
    aliases=['> Movies:'],
    brief='Make the bot say "> Movies:"',  # Movies
    description='Make the bot say "> Movies:"'  # Long description of command
)
async def Teest10(ctx):
    await ctx.send(f">https://flixtor.to/watch/movie/32915994/tom-jerry https://flixtor.to/watch/movie/29556290/raya-and-the-last-dragon  https://flixtor.to/watch/movie/27145410/coming-2-america https://flixtor.to/watch/tv/5324138/superman-lois https://flixtor.to/watch/movie/44873946/girl-in-the-basement https://flixtor.to/watch/movie/32508850/crisis  https://flixtor.to/watch/movie/36097626/the-mauritanian https://flixtor.to/watch/movie/44321034/dark-web-cicada-3301 https://flixtor.to/watch/tv/5407282/resident-alien {ctx.message.author.mention}!")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')




if __name__ == '__main__':
    bot.run("ODE3NTI0NTk1MzA4NDk0OTE5.YEKxHA.lWH7EgZCQjTVYV9YLK0JnAuikNA")
