import discord # TODO: import the discord module
from discord.ext import commands 
import os
from dotenv import load_dotenv
from messages import announcement, permission # TODO: import the variables defined from messages.py

# This is to load .env file
load_dotenv("discord.env")
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# For setting up bot with command prefix
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# This is executed when you run the program
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Failed to sync commands: {e}")
    
    await show_embed() # TODO: call the show_embed() function

async def show_embed():
    print("The bot is now ready for use!")
    print("-----------------------------")

    channel_id = CHANNEL_ID #TODO: place here your channel ID in variable
    channel = bot.get_channel(channel_id)

    if channel:
        embed = discord.Embed(
            title="Bot ni Pinoy Big Sister",
            description=(
                "Welcome sa **Pinoy Big Sister**, mga online housemates!\n\n" \
                "Sa mga susunod na edisyon sa **Pinoy Big Sister**,\n" \
                "ito ang gagamiting channel ni Big Sister para sa mga: \n" \
                "(1) **anunsiyo** (/announcements)\n" \
                "(2) **nominasyon** (/nominate)\n" \
                "(3) paghingi sa kanya ng **permission** (/permission)" # TODO: fill in the description here
            ),
            color=0x5e17eb
        )
        await channel.send(embed=embed)
    else:
        print(f"Channel with ID {channel_id} not found.")


# This is for creating slash commands
@bot.tree.command(name="announcements", description="Tingnan ang anunsiyo ni Big Sister")
async def breakfastquote(interaction: discord.Interaction):
    await interaction.response.send_message(announcement)
    
#TODO: make the commands for /permission and /nominate
@bot.tree.command(name="permission", description="Humingi ng permiso kay Big Sister")
async def breakfastquote(interaction: discord.Interaction):
    await interaction.response.send_message(permission)    

@bot.tree.command(name="nominate", description="Magnominate ng isang housemate")
async def nominate(interaction: discord.Interaction, points: int, housemate: str):
    await interaction.response.send_message(f"Binibigyan mo ng **{points}** point/s si **{housemate}**")

#TODO: run the token by calling the TOKEN variable
bot.run(TOKEN)
