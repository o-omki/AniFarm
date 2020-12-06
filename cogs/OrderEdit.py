import discord
from discord.ext import commands


class MsgEdit(commands.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.channel.id== 737959554666725398:
            ROLE= discord.utils.get(after.guild.roles, id=737954110883627079)
            if ROLE in after.author.roles:
                if after.content== before.content:
                    return
                if after.author.bot:
                    return
                if "a:BTtick:749907713558839357" in before.reactions:
                    await after.channel.send(f"<@{after.author.id}> avoid editing an Order which has already been registered by the bot. Incase you still intend to make any change, ping a Farmer/ Helper for further instructions." , delete_after= 10)
                else:
                    await after.channel.send(f"<@{after.author.id}> ummm... edited messages do not count! If your order was missing the emote <a:BTtick:749907713558839357> , do post another fresh order with the correct format.", delete_after= 10)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.channel.id== 737959554666725398:
            ROLE= discord.utils.get(message.guild.roles, id=737954110883627079)
            if ROLE in message.author.roles:
                if "a:BTtick:749907713558839357" in message.reactions:
                    await message.channel.send(f"<@{message.author.id}> do not delete your farming orders registered by the bot. If you wanna make changes to your order, please ping a Farmer/Helper and wait for further instructions.", delete_after= 10)
                    
               #     logchnl= self.bot.get_channel(751421780228440161)
               #     pfp= message.author.avatar_url
               #     embed= discord.Embed(colour= discord.Colour.red())
                #    embed.set_author(icon_url= pfp, name= f"**{message.author.name}**")
               #     embed.add_field(name= f"**Registered Order deleted by <@{message.author.id}> in <#751421780228440161>", value= f"Message: {message.content}", inline= False)
             #       await logchnl.send(embed= embed)
                    return


def setup(bot):
    bot.add_cog(MsgEdit(bot))
