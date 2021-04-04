import discord
from discord.ext import commands, tasks
from discord.utils import get

bot = commands.Bot(command_prefix=".")


@bot.event      #STARTUP 
async def on_ready():
    await bot.change_presence(
        status=discord.Status.do_not_disturb, 
        activity=discord.Activity(type=discord.ActivityType.listening, name="@Mafiot"))
    print("neatza bro")

@bot.event      #ERROR MESSAGE
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")

@bot.command()      #ALO MSG
async def alo(ctx):
    await ctx.send("alo?")

@bot.command()      #PURGE AMOUT MESSAGES
@commands.has_permissions(administrator=True)
async def clear(ctx, amout=2):
        await ctx.channel.purge(limit=amout+1)

@bot.command()      #CHANGE NICK
async def nick(ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention}.')

@bot.command()      #SKRILLEX REMIX LINK
async def skrillexremix(ctx):
    await ctx.send("https://www.youtube.com/watch?v=c5Myyr6vNxg")

@bot.command()      #AVATAR
async def avatar(ctx, *,  user: discord.Member =None):
    userAvatarUrl = user.avatar_url
    await ctx.send(userAvatarUrl)

@bot.command()      #SEND MSG
async def msg(ctx, member: discord.Member, *, content):
    await ctx.channel.purge(limit=1)
    dm = await member.create_dm()
    await dm.send(content)
    await ctx.send("Message sent!")

@bot.command()      #REACT TO A MESSAGE
async def react(ctx, message: discord.Message, emote):
    await message.add_reaction(emote)
    await ctx.send("Succesfully reacted.")

@bot.command()      # WIDTH x HEIGHT + SIZE OF ATTACHMENT
async def size(ctx):
    attachment = ctx.message.attachments[0] 
    await ctx.send(f"{attachment.width} x {attachment.height} ({attachment.size/1000000} MB)")

bot.run("ODAwNzcyNzMzOTUxNjcyMzcw.YAW_uQ.4aiYl7nthwHl3OzAsOiqgoHzN3U")
