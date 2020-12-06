import discord
from discord.ext import commands
import secrets
import re
import datetime 
import sqlite3
from constants import Constants

class ProgressPoster(commands.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        reactionchannel= self.bot.get_channel(payload.channel_id)
        user= self.bot.get_user(payload.user_id)
        message= await reactionchannel.fetch_message(payload.message_id)

        progchnl= self.bot.get_channel(Constants.PROGRESS_CHANNEL)

        if reactionchannel.id== Constants.QUEUE_CHANNEL:
            for emote in message.reactions:
                if str(emote.emoji)== Constants.REACTION_EMOTE:
                    if user== self.bot.user:
                        return
                    
                    flag= True
                    ROLE= discord.utils.get(message.guild.roles, id=737954110883627079)
                    if ROLE in message.author.roles:
                        flag= False
                        return await message.remove_reaction(Constants.REACTION_EMOTE, user)

                    if flag:
                        buyer= message.embeds[0].fields[0].value
                        card= message.embeds[0].fields[1].value
                        location= message.embeds[0].fields[2].value
                        xp= message.embeds[0].fields[3].value 
                        price= message.embeds[0].fields[4].value
                        catch= re.search("[0-9]+", buyer)
                        ids= catch.start()
                        ide= catch.end()
                        buyerid= buyer[ids:ide] 

                        footers= ["Ughh... sushi cum kimchi, will it taste good?", "So ladies n' gentlemen, I got the medicine so you should keep ya eyes on the ball", "Believe me, waifus > stats!", "Everyday is my birthday!", "you love me... you love me not. you love me...","Say it! You're missing our hime sama :(", "Suji initially wanted me to be a hentai-ish bot *sad moans*", "Mark's looking for loli emotes, help when?", "te amo mami!", "Shanks from One Piece?", "Fun Fact: Nee goes by Neshuwu too!", "Do say a 'hi' to our beloved traps here", "one sushi... two sushi...", "omg wtf ily!", "Simp a sugar daddy when?", "Feel free to ping Lotus to remind them that they're a cute!", "Ha-ha-how you like that", "Oh love me Mister, oh Mister"]
                        randfoot= secrets.choice(footers)

                        FarmID= secrets.randbelow(10000)

                        embed= discord.Embed(title= f"__**Under Progress**__", timestamp= datetime.datetime.now(), colour= discord.Colour.blue())
                        embed.add_field(name= "**Order ID:** ", value= str(FarmID), inline= True)
                        embed.add_field(name= "**Card Name:** ", value= card, inline= False)
                        embed.set_thumbnail(url= user.avatar_url)
                        embed.add_field(name= "**Location:** ", value= location, inline= False)
                        embed.add_field(name= "**XP:** ", value= xp, inline= False)
                        embed.add_field(name= "**Price:** ", value= price, inline= False)
                        embed.set_footer(text= randfoot)

                        msg= await progchnl.send(f"**Buyer:** <@{buyerid}> \n**Farmer:** <@{user.id}>", embed= embed)
                        await msg.add_reaction(Constants.REACTION_EMOTE)

                        
                        mydb= sqlite3.connect("farm.sqlite")
                        cursor= mydb.cursor()
                        cmd= "insert into FARM values(?, ?, ?, ?, ?, ?, ?)"
                        val=(user.id, buyerid, card, xp, location, price, FarmID)
                        cursor.execute(cmd, val)

                        await message.delete()
                        mydb.commit()
                        cursor.close()
                        mydb.close()

def setup(bot):
    bot.add_cog(ProgressPoster(bot))


