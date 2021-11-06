import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event 
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi there!!!")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.command()
async def  ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
    responses = ['It is Certain.','It is decidedly so.','Without a doubt.',' Yes definitely.','You may accept it.','Most likely.','Yes.','Your family will hate you for this decision.','Better not tell you now.','A goldfish asks better questions then you.','Dont count on it.','No.','Your family will love you for this decision.','Im unsure.','perhaps.','ask again.']
    await ctx.send(f'question: {question}\nAnswer: {random.choice(responses)}')

client.run("Nzc3NDI2NjU2NzM0MjE2MTk2.X7DQ_g.2Yn5kOS0sZnZfV9kaJq2nHo-1oU")
