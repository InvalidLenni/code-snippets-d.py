"""
# WARNING: This file is not supported anymore, use the button components they are very cool and better! This has 1 - 3 bugs maybe idk
"""
import discord
from discord.ext import commands


class Testhelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hilfe")
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.guild_only()
    async def _hilfe(self, ctx):
        if ctx.author.bot:
            return
        embed = discord.Embed(title=f'Command Overview',
                              description='Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et', # Here can you write your own embed description for the help command
                              color=0x1abc9c)
        msg = await ctx.send(embed=embed)

        await msg.add_reaction("")
        await msg.add_reaction("")
        await msg.add_reaction("")
"""
# Optional... If you need more reactions then you must remove the 3 "!
        await msg.add_reaction("")
        await msg.add_reaction("")
        await msg.add_reaction("")
        await msg.add_reaction("")
        await msg.add_reaction("")
"""

        def check(reaction, user):
            return user.bot is False

        while True:
            reaction, user = await self.bot.wait_for("reaction_add", check=check)
            if str(reaction.emoji) == "<a:info:826762028059328512>":
                await msg.remove_reaction(reaction, user)
                embed = discord.Embed(
                    title=f'Embed Title', # Your own embed title for reaction 1
                    description="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et", # Your own embed description for reaction 1
                    color=0x1abc9c)
                await msg.edit(embed=embed)
            elif str(reaction.emoji) == "<:fun:824275399680851978>":
                await msg.remove_reaction(reaction, user)
                embed = discord.Embed(
                    title=f'Embed Title', # Your own embed title for reaction 2
                    description="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et", # Your own embed description for reaction 2
                    color=0x1abc9c)
                await msg.edit(embed=embed)
            elif str(reaction.emoji) == "<a:music:824578259009536010>":
                await msg.remove_reaction(reaction, user)
                embed = discord.Embed(
                    title=f'Embed Title', # Your own embed title for reaction 3
                    description="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et", # Your own embed description for reaction 3
                    color=0x1abc9c)
                await msg.edit(embed=embed)
            elif str(reaction.emoji) == "<:moderation:824377687329472553>":
                await msg.remove_reaction(reaction, user)
                embed = discord.Embed(
                    title=f'Embed Title', # Your own embed title for reaction 4
                    description="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et", # Your own embed description for reaction 4
                    color=0x1abc9c)
                await msg.edit(embed=embed)
            elif str(reaction.emoji) == "<:log:825440417021558836>":
                await msg.remove_reaction(reaction, user)
                embed = discord.Embed(
                    title=f'Embed Title', # Your own embed title for reaction 5
                    description="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et", # Your own embed description for reaction 5
                    color=0x1abc9c)
                await msg.edit(embed=embed)
            elif str(reaction.emoji) == "<:misc:825440900233691158>":
                await msg.remove_reaction(reaction, user)
                embed = discord.Embed(
                    title=f'Embed Title', # Your own embed title for reaction 6
                    description="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et", # Your own embed description for reaction 6
                    color=0x1abc9c)
                await msg.edit(embed=embed)
            elif str(reaction.emoji) == "<:nsfw:827163756235980810>":
                await msg.remove_reaction(reaction, user)
                embed = discord.Embed(
                    title=f'Embed Title', # Your own embed title for reaction 7
                    description="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et", # Your own embed description for reaction 7
                    color=0x1abc9c)
                await msg.edit(embed=embed)
            elif str(reaction.emoji) == "<a:working:824280364117262357>":
                await msg.remove_reaction(reaction, user)
                embed = discord.Embed(
                    title=f'Embed Title', # Your own embed title for reaction 8
                    description="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et", # Your own embed description for reaction 8
                    color=0x1abc9c)
                await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(Testhelp(bot))
