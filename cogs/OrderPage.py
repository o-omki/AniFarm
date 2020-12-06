from discord.ext import commands 
import discord
import datetime



class OrderPage(commands.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id== 749183619020488735:
            return

        if message.channel.id != 737959554666725398:
            return
        else:                
            async for msg in message.channel.history(before= message.created_at):
                if msg.author.id == 749183619020488735:                    
                    await msg.delete()
                    embed= discord.Embed(title= "**__How To Order:__**", colour= discord.Colour.light_grey())
                    embed.add_field(name= "**Format:**", value="Your order should follow the following format: **xp card-name location(optional)** for example: \n *40000 xp Asuna loc 69-9  or  40k xp Asuna loc 69*", inline= False)
                    embed.add_field(name= "**P.S**", value= "Every message must contain only one order. For multiple orders, send different messages for each \nDo not use emojis or any other unnecessary phrases in your order too. Keep it simple haii! Danke!", inline= False )
                    await message.channel.send(embed= embed)
                    return
                    
                                        
                else:
                    embed= discord.Embed(title= "**__How To Order:__**", colour= discord.Colour.light_grey())
                    embed.add_field(name= "**Format:**", value="Your order should follow the following format: **xp card-name location(optional)** for example: \n *40000 xp Asuna loc 69-9  or  40k xp Asuna loc 69*", inline= False)
                    embed.add_field(name= "**P.S**", value= "Every message must contain only one order. For multiple orders, send different messages for each \nDo not use emojis or any unnecessary phrases in your order too. Keep it simple haii! Danke!", inline= False )
                    await message.channel.send(embed= embed)
                    return
                    

def setup(bot):
    bot.add_cog(OrderPage(bot))
