import discord

bot = discord.Client()

@bot.event
async def on_ready():
    print("Bot Activated")
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello")


bot.run("YOUR BOT TOKEN")