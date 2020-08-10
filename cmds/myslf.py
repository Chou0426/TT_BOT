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
    async def pttB(self,ctx,num:int,wantNum:int):
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
            urltitles = root.find_all("div",class_="title")

            await ctx.send("第"+str(i+1)+"頁的內容:")
            
            for urltitle in urltitles:
                if urltitle.a != None:
                    if count < wantNum:
                        if not "[公告]" in (urltitle.a.string):
                            Link=urltitle.find("a")
                            await ctx.send(str(count+1)+'.'+str(Link.string))
                            await ctx.send('https://www.ptt.cc/'+Link['href'])
                            await asyncio.sleep(0.01) #單位:秒 
                            # webbrowser.open_new('https://www.ptt.cc/'+Link['href']) 
                    count = count + 1
            
            await ctx.send("==========================================================")
            
            nextLinkTag=root.find("a",string="‹ 上頁")
            nextLink = nextLinkTag['href']
            myUrl = nextLink
            url = 'https://www.ptt.cc/' + myUrl           

            i = i + 1
            count = 0
            
    @commands.command()
    async def pttB2(self,ctx,picUrl):
        request=req.Request(picUrl,headers={
                "cookie":"over18=1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"})
        with req.urlopen(request) as response:
            data=response.read().decode("utf-8")
            #解析原始碼，取得每篇文章的標題
        root=bs4.BeautifulSoup(data,"html.parser") #讓BeautifulSoup協助我們解析HTML格式文件
        titles=root.find_all("a") 
        for title in titles:
            if str(title.string).endswith("jpg"):
                await asyncio.sleep(0.1) #單位:秒
                await ctx.send(title["href"])
                # await ctx.send(str(title.string))
    
def setup(bot):
    bot.add_cog(Myslf(bot))