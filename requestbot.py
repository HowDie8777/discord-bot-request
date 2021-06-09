import discord
from discord.ext import commands
import json,os,random,asyncio,datetime
import bs4
import urllib.request as req


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">> bot online<<")
    bot.loop.create_task(baha())

@bot.command()
async def baha():
    while True:
        channel = bot.get_channel()#Your channel's ID
        url = f"https://forum.gamer.com.tw/A.php?bsn=60076"
        request = req.Request(url , headers={
            "User-Agent":""#Your User Agent
        })
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")
        root = bs4.BeautifulSoup(data,"html.parser")
        a = root.find("tr",class_="b-list__row b-list-item b-imglist-item")
        che = a.find("p",class_="b-list__count__number")
        if int(a.find("span").string) == 0:
            b = a.find("td",class_="b-list__main")
            text = b.find("div",class_="b-list__tile").find("p").string
            link = b.find("a").get("href")
            await channel.send(f'{text}\nhttps://forum.gamer.com.tw/{link}')
        await asyncio.sleep(5) 


if __name__ == "__main__":
    bot.run('')#Your discord  bot token