import discord
import requests
import time
import API-Source

bot = discord.Client()
UI_DELAY = 0.5

@bot.event
async def on_ready():
    print("Activating Nerd Brain....")
    time.sleep(UI_DELAY)
    print("Processing Infinite Wisdom(Approximately).....")
    time.sleep(UI_DELAY)
    print("Brushing Up Nerd Glasses...")
    time.sleep(UI_DELAY)
    print(f"Nerd Ready - \tUsername - {bot.user}")

@bot.event
async def on_message(msg):
    if msg.contents.startswith('!wiki'):
        API-Source.wiki(msg.contents.split()[1])
    if msg.contents.startswith('!space'):
        API-Source.space(msg.contents.split()[1])


bot.run('API-TOKEN')



# xpath
# //*[@id="mw-content-text"]/div[1]/p[2]
# xpa

# https://api.le-systeme-solaire.net/rest/