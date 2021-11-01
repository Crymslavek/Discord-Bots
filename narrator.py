import discord
import random
from flask import flask
from discord.ext import commands
from random import randint


bot = commands.bot(command_prefix=".")
client = discord.client()


@bot.event
async def on_ready():
    print("Automaton online")


@bot.command()
async def test(ctx):
    await ctx.send('This is a test')


@bot.command()
async def invite(ctx):
    ctx.send("https://discod.com/api/ouath2/autorize?client_id=889285536123060245&permissions=8&scope=bot")


@bot.command()
async def quest(ctx):
    await ctx.message.delete()
    Narrarator_responses_1 = [
        'Find a weapon for the armory',
        'Explore the caves.',
    ]
    quest = random.choice(Narrarator_responses_1)
    await ctx.send(quest)


@bot.command()
async def encounter(ctx):
    Narrarator_responses_2 = [
        'You found a bear!',
        'You found a bow, but there are no arrows.',
        'You found nothing...',
        'You found a sheild.',
        'You found a treasure chest, it has 2,000 gold!',
        'You were injured before you could find anything, and had to go home.',
        'A new candadite awaits...',
        'You found 500 gold!',
        'You found 1,000 gold!',
        "You found 1,500 gold!",
        'You found the sword of the storm!',
        'You are now a werewolf...',
        'You found a dragon hoard, but you left   everything there.',
    ]
    encounter = random.choice(Narrarator_responses_2)
    await ctx.send(encounter)


@bot.command()
async def ping(ctx):  #a!ping
    await ctx.send('Pong! {}ms'.format(round(bot.latency * 1000)))


def keep_alive():
    t = Thread(target=run)
    t.start(token)

bot.run(token)
