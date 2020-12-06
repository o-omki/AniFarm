import discord
from discord.ext import commands
import sqlite3
import discord.utils
from constants import Constants

class FinishedPoster(commands.Cog):
        def __init__(self, bot):
                self.bot= bot
        


        @commands.Cog.listener()
        async def on_raw_reaction_add(self, payload):
                reactionchannel= self.bot.get_channel(payload.channel_id)
                message= await reactionchannel.fetch_message(payload.message_id)
                user= self.bot.get_user(payload.user_id)

                for emote in message.reactions:
                    if(str(emote.emoji)!= Constants.REACTION_EMOTE):
                        pass
                    else:
                        if reactionchannel.id== Constants.PROGRESS_CHANNEL:
                                finishedchnl= self.bot.get_channel(Constants.FINISHED_CHANNEL)
                                if user== self.bot.user:
                                    return
                                flag= True
                                ROLE= discord.utils.get(message.guild.roles, id=737954110883627079)
                                if ROLE in message.author.roles:
                                    flag= False
                                    return await message.remove_reaction(Constants.REACTION_EMOTE, user)

                                if flag:
                                    FarmID= message.embeds[0].fields[0].value
                                    mydb= sqlite3.connect("farm.sqlite")
                                    cursor= mydb.cursor()
                                    
                                    cursor.execute(f"select * from FARM where Farm_ID= {FarmID} and Farmer_ID= {user.id}")
                                    result= cursor.fetchone()

                                    if not result:
                                        await message.remove_reaction(Constants.REACTION_EMOTE, user)
                                        return await message.channel.send("You ain't working on this order!", delete_after= 5)

                                    else: 
                                        buyer= str(result[1])
                                        card= str(result[2])
                                        xp= str(result[3])                                        
                                        price= str(result[5])
                                        price= str(price)

                                        cursor.execute(f"select Custom_Msg from CUSTOM where Farmer_ID= {user.id}")
                                        result= cursor.fetchone()
                                        if result== None:
                                            await finishedchnl.send(f"Heyaa <@{buyer}>! Your order for {xp} XP {card} has been completed at a grand total of {price} gold. Please ping <@{user.id}> in Anitrade 1/2/3 at your earliest convenience!!")

                                        else:
                                            msg= str(result[0])
                                            msg= msg.replace("BUYER", f"<@{buyer}>")
                                            msg= msg.replace("CARD", card)
                                            msg= msg.replace("EXP", xp)
                                            msg= msg.replace("PRICE", price)
                                            msg= msg.replace("FARMER", f"<@{user.id}>")

                                            await finishedchnl.send(msg)
                                            

                                        cursor.execute(f"delete from FARM where Farm_ID= {FarmID} and Farmer_ID= {user.id}")
                                        await message.delete()

                                    mydb.commit()
                                    cursor.close()
                                    mydb.close()

def setup(bot):
        bot.add_cog(FinishedPoster(bot))    
