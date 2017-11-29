from business import *
import discord
import asyncio

client = discord.Client()

class discordbot:
    def __init__(self, token):
        client.run(token)

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
    
    @client.event
    async def on_message(message):
        if message.content.startswith('!dw'):
            mybusiness = dispatcher()
            reply = mybusiness.dispatcher(message)
            await discordbot.send_message(message.channel, reply)
    
    async def send_message(channel, message):
        await client.send_message(channel, message)
