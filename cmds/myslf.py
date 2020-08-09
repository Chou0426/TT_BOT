import discord
from discord.ext import commands
from core.classes import Cog_Extention
import urllib.request as req
import bs4
import asyncio
import sys
from selenium import webdriver
import webbrowser
import random
import re

class Myslf(Cog_Extention):
    
    @commands.command()
    async def pttB(self,ctx,num:int):
        count = 0
        i = 0
        global url
        url = "https://www.ptt.cc/bbs/Beauty/index.html"
        global myUrl
        myUrl = ""
        #抓取ptt表特版的網頁原始碼(HTML)
        #建立一個 Request 物件，附加 Request headers 的資訊
        while i < num:
            request=req.Request(url,headers={
                "cookie":"over18=1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"})
            with req.urlopen(request) as response:
                data=response.read().decode("utf-8")
            #解析原始碼，取得每篇文章的標題
            root=bs4.BeautifulSoup(data,"html.parser") #讓BeautifulSoup協助我們解析HTML格式文件
            titles=root.find_all("a") 
            urltitles = root.find_all("div",class_="title")
    
            await ctx.send("第"+str(i+1)+"頁的內容:")

            for urltitle in urltitles:
                if count < 5:
                    if urltitle.a != None:
                        Link=urltitle.find("a")
                        
                        await ctx.send(str(count+1)+'.'+str(Link.string))
                        await ctx.send('https://www.ptt.cc/'+Link['href'])
                        await asyncio.sleep(0.1) #單位:秒 
                        # webbrowser.open_new('https://www.ptt.cc/'+Link['href']) 
                count = count + 1
            
            await ctx.send("---------------------------------------------")
            
            nextLinkTag=root.find("a",string="‹ 上頁")
            nextLink = nextLinkTag['href']
            myUrl = nextLink
                        

                        # nextLinkCon=urltitle.find("a")
                        # await ctx.send("下一頁的內容:")
                        # await ctx.send(str(nextLinkCon.string))
                        # await ctx.send('https://www.ptt.cc/'+nextLinkCon['href'])
                        # await asyncio.sleep(0.1) #單位:秒 
                        # # webbrowser.open_new('https://www.ptt.cc/'+nextLinkCon['href'])     
            url = 'https://www.ptt.cc/' + myUrl
            # await ctx.send("下一頁的網址:"  + url)
            
            # nextLink=root.find("a",string="‹ 上頁") #找到內文是 ‹ 上頁的a標籤
            # return nextLink["href"]
            # for title in titles:
            #     if str(title.string).endswith("jpg"):
            #         await asyncio.sleep(0.1) #單位:秒
            #         # await ctx.send(nextLink["href"])
            #         await ctx.send(str(title.string))
            i = i + 1
            count = 0
            
#     @commands.command()
#     async def pttB2(self,ctx):
#         B2url = myUrl
#         count = 0
#         #抓取ptt表特版的網頁原始碼(HTML)
#         #建立一個 Request 物件，附加 Request headers 的資訊
#         for i in B2url:
#             request=req.Request(i,headers={
#                 "cookie":"over18=1",
#                 "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"})
#             with req.urlopen(request) as response:
#                 data=response.read().decode("utf-8")
#             #解析原始碼，取得每篇文章的標題
#             root=bs4.BeautifulSoup(data,"html.parser") #讓BeautifulSoup協助我們解析HTML格式文件
#             titles=root.find_all("a") 
#             urltitles = root.find_all("div",class_="title")
            
#             for urltitle in urltitles:
#                 if urltitle.a != None:
#                     if count < 5:
#                         Link=urltitle.find("a")
#                         await ctx.send(str(count+1)+'.'+str(Link.string))
#                         await ctx.send('https://www.ptt.cc/'+Link['href'])
#                         await asyncio.sleep(0.1) #單位:秒 
#                         # webbrowser.open_new('https://www.ptt.cc/'+Link['href'])
                        
#                     # elif count == 5 :
#                     #     nextLinkTag=root.find("a",string="‹ 上頁")
#                     #     nextLink2 = 'https://www.ptt.cc/'+nextLinkTag['href']
#                     #     await ctx.send("下一頁的網址:" + nextLink2)
#                     #     nextLink22 = nextLink2
                        
                        
#                         # nextLinkCon=urltitle.find("a")
#                         # await ctx.send("下一頁的內容:")
#                         # await ctx.send(str(nextLinkCon.string))
#                         # await ctx.send('https://www.ptt.cc/'+nextLinkCon['href'])
#                         # await asyncio.sleep(0.1) #單位:秒 
#                         # # webbrowser.open_new('https://www.ptt.cc/'+nextLinkCon['href'])
#                     count = count + 1
        
def setup(bot):
    bot.add_cog(Myslf(bot))