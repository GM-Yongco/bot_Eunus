# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to abstract away discord stuff
# Real Description	: all date based commands
# HEADERS ================================================================

import discord
import discord.ext.commands

# for bot tokens and ids and such things that need to be hidden from github
from dotenv import load_dotenv
import os

# ========================================================================
# FUNCTIONS 
# ========================================================================

def define_commands_channels(bot:discord.ext.commands.bot.Bot) -> None:

	load_dotenv()
	USER_ID_01:int = int(os.getenv("ID_USER_01"))
	USER_ID_02:int = int(os.getenv("ID_USER_02"))

	@bot.tree.command(name = "channel_clone_delete", description = "clones channels the command is done in")
	async def channel_clone_delete(interaction: discord.Interaction):

		function_prefix:str = "command : channel_clone_delete"

		# checking credentials
		if interaction.user.id == USER_ID_01 or interaction.user.id == USER_ID_02:
			await interaction.channel.clone()
			await interaction.channel.delete()
			function_prefix += " authorized"
		else:
			await interaction.response.send_message(f"```you dont have credentials for this bucko```")
			function_prefix += " not authorized"
			
		print(function_prefix)