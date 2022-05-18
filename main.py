# TO KEEP DISCORD BOT RUNNING IN REPL.IT
from keep_alive import keep_alive
import discord
from discord.ext import tasks

# WEB SCRAPING IMPORTS
import requests
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
  # Output to console when started
  print('Ready!')
  check.start()

# Check whether website has updated every 15 minutes
@tasks.loop(minutes=15.0)
async def check():
  # Can replace with any site with any class
  response = requests.get('https://classes.usc.edu/term-20223/classes/buad/').text
  
  soup = BeautifulSoup(response, 'html.parser')
  # Can replace with specific class and its details
  soup = soup.find('div', attrs={'id':'BUAD-497-details'})
  
  noProfessors = True
  for td in soup.findAll('td', attrs={'class':'instructor'}):
    # print("Instructor:", td.text)
    if td.text != "":
      noProfessors = False

  if not noProfessors:
    channel = client.get_channel(# INPUT DISCORD CHANNEL ID)
    await channel.send("Professors have been published for BUAD 497!")

keep_alive()
client.run(# INPUT DISCORD BOT TOKEN)
