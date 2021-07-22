from telethon import TelegramClient, sync
from telethon.tl.types import Chat, Channel, InputChannel
from telethon.tl.functions.channels import InviteToChannelRequest
import json
import time

api_id = '1940009424'
api_hash = 'AAGgjapJNAyrN-qazFR7nNip85oiqY1w6Y8'
user_file = 'users.json'

with TelegramClient('session_name', api_id, api_hash) as client:
    client.start()

# READING USERS FROM A GROUP AND WRITING THEM INTO A JSON FILE
    data = {}

    for member in client.get_participants('MillionTokenHolders', limit=5):
        memberToAdd = {}
        if (member.username != None and member.bot == False):
            memberToAdd['username'] = member.username
            if (member.first_name != None):
                memberToAdd['first_name'] = member.first_name
            if (member.last_name != None):
                memberToAdd['last_name'] = member.last_name
            data[member.id] = memberToAdd

    with open('new_users.json', 'w') as outfile:
        json.dump(data, outfile)
