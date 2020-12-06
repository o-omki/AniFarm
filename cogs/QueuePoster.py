import discord
from discord.ext import commands 
import re
import datetime
import random


def PriceCalc(self, xp, loc):
    spechar= re.compile(r"[/\|:-]")
    clcatch= spechar.search(loc)
    if clcatch != None:
        specharindex= clcatch.start()
        ratefloor= int(loc[:specharindex])
        if ratefloor <=20:
            ratecharge= 0.5
        else:
            ratecharge= 0.4

        kchars= [re.compile(p) for p in ['k', 'K']]
        for kchar in kchars:
            kcatch= kchar.search(xp)
            if kcatch != None:
                i= kcatch.start()
                cmount= xp[:i].strip()
                camount= int(cmount)*1000
                totalprice= ratecharge * camount
                return totalprice
            else:
                cmount= xp.strip()
                camount= int(cmount)
                totalprice= ratecharge* camount 
                return totalprice

    else:
        ratefloor= int(loc)
        if ratefloor <=20:
            ratecharge= 0.5
        else:
            ratecharge= 0.4

        kchars= [re.compile(p) for p in ['k', 'K']]
        for kchar in kchars:
            kcatch= kchar.search(xp)
            if kcatch != None:
                i= kcatch.start()
                cmount= xp[:i].strip()
                camount= int(cmount)*1000
                totalprice= ratecharge * camount
                return totalprice
            else:
                cmount= xp.strip()
                camount= int(cmount)
                totalprice= ratecharge* camount 
                return totalprice



def xpxp(self, txt):
    txt= txt.lower()
    if "exp" in txt:
            xpcatch= re.search("exp", txt)
            xstart= xpcatch.start()
            xend= xpcatch.end()    
            return (xstart) , (xend)
    elif "xp" in txt:        
            xpcatch= re.search("xp", txt)
            xstart= xpcatch.start()
            xend= xpcatch.end()
            return (xstart) , (xend)



def locloc(self, Txt):
    Txt= Txt.lower()
    if "loc" in Txt:
            loccatch= re.search("loc", Txt)
            lstart= loccatch.start()
            lend= loccatch.end()
            return (lstart), (lend)
    elif "location" in Txt:
            loccatch= re.search("location", Txt)
            lstart= loccatch.start()
            lend= loccatch.end()
            return (lstart), (lend)


def locs(self, TXT):
    for locindex, c in enumerate(TXT):
            if c.isdigit():
                
                    locnumstart= locindex
                    if locnumstart:
                            for locindex2, c2 in enumerate(TXT[locnumstart:]):
                                    if c2.isalpha():
                                            locnumend= locindex2
                                            floor= TXT[locnumstart:locnumend]
                                            return (floor)
                                    else:
                                            floor= TXT[locnumstart:]
                                            return (floor)
                    else:
                            floor= "Not Mentioned"
                            return (floor)


class QueuePoster(commands.Cog):
        def __init__(self, bot):
                self.bot= bot 


        @commands.Cog.listener()         
        async def on_message(self, message):
                queuechnl= self.bot.get_channel(737984943862579241)
                if message.channel.id != 737959554666725398: 
                        return
                else:
                    if(message.author== self.bot.user):
                        return
                    
                     
                    text= message.content


                    text= text.replace('.', ' ')
                    text= text.replace(',', '')
                    text= text.replace('(', ' ')
                    text= text.replace(')', ' ')
                    
                    check= 0
                    xpstart, xpend=    xpxp(self, text)     
           
                                    
                                    
                    for xpindex, c in enumerate(text[0:xpstart]):
                            if c.isdigit():
                                    amountstart= xpindex 
                                    check=1
                                    break
                    CardAmount= text[amountstart:xpstart]

                    CardLocation= "Not Mentioned"
                    CardName= " "
                    if "loc" in text or "LOC" in text or "LOCATION" in text or "location" in text or "Loc" in text or "Location" in text:
                        locstart, locend= locloc(self, text)

                        if locstart != None and locend != None:
                            CardLocation= locs(self, text[locend:])
                            CardName= text[xpend:locstart]
                        else:
                            CardName= text[xpend:]
                    else:
                        CardName= text[xpend:]

                    FarmingRate= 0
                    if (CardLocation == "Not Mentioned"):
                            FarmingRate= "Can't calculate 'cos location not provided."
                    else:
                            FarmingRate= PriceCalc(self, CardAmount, CardLocation)
                    
                    footers= ["Ughh... sushi cum kimchi, will it taste good?", "So ladies n' gentlemen, I got the medicine so you should keep ya eyes on the ball", "Believe me, waifus > stats!", "Everyday is my birthday!", "you love me... you love me not. you love me...","Say it! You're missing our hime sama :(", "Suji initially wanted me to be a hentai-ish bot *sad moans*", "Mark's looking for loli emotes, help when?", "te amo mami!", "Shanks from One Piece?", "Fun Fact: Nee goes by Neshuwu too!", "Do say a 'hi' to our beloved traps here", "one sushi... two sushi...", "omg wtf ily!", "Simp a sugar daddy when?", "Feel free to ping Lotus to remind them that they're a cute!", "Ha-ha-how you like that", "Oh love me Mister, oh Mister"]
                    randfoot= random.choice(footers)

                    embed= discord.Embed(title= "__**ORDER**__", timestamp= datetime.datetime.now(), colour= discord.Colour.blue())
                    embed.set_thumbnail(url= self.bot.user.avatar_url)
                    embed.add_field(name="**Buyer:** ", value= f"<@{message.author.id}>", inline= False)
                    embed.add_field(name="**Card Name:** ", value= str(CardName), inline= False) 
                    embed.add_field(name="**Location:** ", value= str(CardLocation), inline= False)
                    embed.add_field(name="**XP Amount:** ", value= str(CardAmount), inline= False)
                    embed.add_field(name="**Price:** ", value= str(FarmingRate), inline= False)
                    embed.set_footer(text= randfoot)
                    if check==1:
                            msg= await queuechnl.send(embed= embed)
                            await msg.add_reaction("<:OwlBlush:708020553235169290>")
                            await message.add_reaction("<a:BTtick:749907713558839357>")



def setup(bot):
        bot.add_cog(QueuePoster(bot))              
