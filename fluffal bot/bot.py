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

@client.command()
async def trans(ctx):
    await ctx.send("hot bishes on the pink pills")


@client.command()
async def nini(ctx):
    await ctx.send("night everyone")


@client.command()
async def sex(ctx):
    await ctx.send("bonk")

@client.command()
async def supporter(ctx):
    await ctx.send("If you wish to support bot development go help my mistress on kofi! https://ko-fi.com/doggo_vt")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.command()
async def  ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
    responses = ['ID10T error','nowi said no','It is Certain.','It is decidedly so.','Without a doubt.',' Yes definitely.','You may accept it.','Most likely.','Yes.','Your family will hate you for this decision.','Better not tell you now.','A goldfish asks better questions then you.','Dont count on it.','No.','Your family will love you for this decision.','Im unsure.','perhaps.','ask again.']
    await ctx.send(f'question: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases=['1d4'])
async def d4(ctx,*,roll):
    responses = ['1','2','3','4']
    await ctx.send(f'roll: {roll}\nrolled: {random.choice(responses)}')

@client.command(aliases=['1d6'])
async def d6(ctx,*,roll):
    responses = ['1','2','3','4','5','6']
    await ctx.send(f'roll: {roll}\nrolled: {random.choice(responses)}')

@client.command(aliases=['1d8'])
async def d8(ctx,*,roll):
    responses = ['1','2','3','4','5','6','7','8']
    await ctx.send(f'roll: {roll}\nrolled: {random.choice(responses)}')

@client.command(aliases=['1d10'])
async def d10(ctx,*,roll):
    responses = ['1','2','3','4','5','6','7','8','9','10']
    await ctx.send(f'roll: {roll}\nrolled: {random.choice(responses)}')

@client.command(aliases=['1d20'])
async def d20(ctx,*,roll):
    responses = ['1(critical miss take 1d4 damage)','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20 (perfection roll 1d4 bonus damage)']
    await ctx.send(f'roll: {roll}\nrolled: {random.choice(responses)}')

@client.command(aliases=['1d10d10'])
async def d1010(ctx,*,roll):
    responses = ['10','20','30','40','50','60','70','80','90','100']
    await ctx.send(f'roll: {roll}\nrolled: {random.choice(responses)}')

@client.command()
async def mom(ctx):
    await ctx.send("Username.Username is baking cookies.")

bot = commands.Bot(command_prefix='>')

@client.command()
async def gm(ctx):
    await ctx.send("good morning!")

@client.command()
async def birthday(ctx):
    await ctx.send("Happy birthday!")


@client.command()
async def Bolshevism(ctx):
    await ctx.send("Bolshevism (from Bolshevik) is a revolutionary socialist current of Soviet Marxist-Leninist political thought and political regime associated with the formation of a rigidly centralized, cohesive and disciplined party of social revolution, focused on overthrowing the existing capitalist state system, seizing power and establishing the dictatorship of the proletariat")

@client.command()
async def proletariat(ctx):
    await ctx.send("workers or working-class people, regarded collectively (often used with reference to Marxism).")



client.run(private key afd cog)

