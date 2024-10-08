# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

from class_discord import *

import asyncio
from functions_daily import bot_time_log
from commands_restart import define_commands_restart, restart_file
from commands_motivate import define_commands_motivate
from commands_channels import define_commands_channels

# ========================================================================
# NEW CLASS
# ========================================================================

class EunusBot(DiscordBot):
	
	# new functions
	def define_on_ready(self) -> None:
		@self.bot.event
		async def on_ready():
			# get channel can only be used after the bot has been ready
			self.define_log_channel() 

			# synch the current commands
			synced:List[discord.app_commands.models.AppCommand] = await self.bot.tree.sync()
			print(f"Synched {len(synced)} commands:")
			for index, command in enumerate(synced):
				print(f"{index + 1:3} : {command}")

			# ready
			print(f"{self.bot.user} is now ready")
			print("-" * 50)

			# tasks for bot after setup
			bot_log = asyncio.create_task(bot_time_log(channel = self.LOG_CHANNEL, interval_seconds = 300))
			await asyncio.gather(bot_log)

	# ====================================================================
	
	# new functions
	def define_on_disconnect(self) -> None:
		@self.bot.event
		async def on_disconnect():
			print(f"{self.bot.user} has disconnected, initializing restart")
			await self.bot.close()
			restart_file()

	# ====================================================================

	# an override
	def define_bot_commands(self)->None:
		define_commands_restart(self.bot)
		define_commands_motivate(self.bot)
		define_commands_channels(self.bot)

	# ====================================================================

	# an override
	def run(self):
		self.get_references()
		self.define_bot()

		self.initialization_functions.insert(0, self.define_bot_events)
		self.initialization_functions.insert(0, self.define_bot_commands)

		for functions in self.initialization_functions:
			try:
				functions()
				print(f"initialization_functions : {functions.__name__} - success")
			except Exception as e:
				print(f"initialization_functions : {functions.__name__} - ERROR\n\t{e}")
		
		# ================================================================
		# the new part
		# would raise a cant connect to discord error

		try:
			self.bot.run(self.TOKEN)
		except Exception as e:
			print('='*50)
			print(e)
			print('='*50)
			restart_file()
			exit()