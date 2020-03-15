#IMPORT Modules
import discord,asyncio,re,requests
from bs4 import BeautifulSoup

#BOT INFO
CHANNEL_ID = process.env.CHANNEL_ID #ENTER ID
client = discord.Client()

#BOOT UP
print("Now online!")

@client.event
async def on_message(message):
    #STATUS
    await client.change_presence(activity=discord.Game(name='Counting Covid-19 Cases')) #CHANGE STATUS TO ANYTHING
    
    #TOTAL
    if message.content.find("!total") != -1:

        #FETCHES STATS
        URL = 'https://www.worldometers.info/coronavirus/'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.findAll("div", {"class" :'maincounter-number'})
    
        #Variables
        data = [] #0= Cases, 1= deaths, 2= recovered
        for old in results:
            data.append(old.text.strip())
        
        #STR TO INT
        data[0] = int(re.sub('[^0-9]','', data[0]))
        data[1] = int(re.sub('[^0-9]','', data[1]))
        data[2] = int(re.sub('[^0-9]','', data[2]))

        #EMBED
        new_embed = ["","",""]
        new_embed[0] = str(data[0])
        new_embed[1] = str(data[1])
        new_embed[2] = str(data[2])
        
        embed = discord.Embed(title="__Covid-19 Total Stats__")
        embed.add_field(name="Total cases:", value=new_embed[0])
        embed.add_field(name="Total deaths:", value=new_embed[1])
        embed.add_field(name="Total recoveries:", value=new_embed[2])

        await message.channel.send(content=None, embed=embed)
    
    #UK
    if message.content.find("!uk") != -1:
        #FETCHES STATS
        uk_URL = 'https://www.worldometers.info/coronavirus/country/uk/'
        uk_page = requests.get(uk_URL)
        uk_soup = BeautifulSoup(uk_page.content, 'html.parser')
        uk_results = uk_soup.findAll("div", {"class" :'maincounter-number'})

        #Variables
        uk_data = []
        for old in uk_results:
            uk_data.append(old.text.strip())
            
        #STR TO INT
        uk_data[0] = int(re.sub('[^0-9]','', uk_data[0]))
        uk_data[1] = int(re.sub('[^0-9]','', uk_data[1]))
        uk_data[2] = int(re.sub('[^0-9]','', uk_data[2]))
        
        #EMBED
        new_uk_embed = ["","",""]
        new_uk_embed[0] = str(uk_data[0])
        new_uk_embed[1] = str(uk_data[1])
        new_uk_embed[2] = str(uk_data[2])
        
        uk_embed = discord.Embed(title="__Covid-19 UK Stats__")
        uk_embed.add_field(name="Total cases:", value=new_uk_embed[0])
        uk_embed.add_field(name="Total deaths:", value=new_uk_embed[1])
        uk_embed.add_field(name="Total recoveries:", value=new_uk_embed[2])

        await message.channel.send(content=None, embed=uk_embed)

client.run(process.env.BOT_TOKEN)
