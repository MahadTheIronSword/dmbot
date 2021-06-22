import discord
from discord.ext import commands

botToken = open('token.txt', 'r').read()
botPrefix = open('prefix.txt', 'r').read()

botIntents = discord.Intents.default()
botIntents.members = True

bot = commands.Bot(command_prefix=botPrefix, intents=botIntents)


@bot.event
async def on_command_error(message, error):
    print(error)
    await message.send('An error occurred. Please try again!')


@commands.has_permissions(administrator=True)
@bot.command()
async def dm(message, user: discord.Member, *, content: str):
    if not user.dm_channel:
        await user.create_dm()

    await user.dm_channel.send(content)

    dmEmbed = discord.Embed(title='DM Result', color=discord.Color.from_rgb(99, 205, 218))
    dmEmbed.add_field(name=f'''Successfully DM'ed {user.name}''', value='''DM was successful''')

    await message.send(embed=dmEmbed)


bot.run(botToken)
