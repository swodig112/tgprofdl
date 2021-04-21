#!/usr/bin/env python3
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from config import *

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

chats = []
groups = []
chats = client.get_dialogs()

for chat in chats:
    try:
        if chat.is_group == True:
            groups.append(chat)
    except:
        continue

print('Listing the groups...')
for i in range(len(groups)):
    print(str(i) + '- ' + groups[i].title)
    target_group = groups[i]
target_group = groups[int(input("\nEnter the number of the group: "))]

print('Fetching members of {0}...'.format(target_group.name))
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print("Downloading profilce pictures...")
for user in all_participants:
    print(user.id)
    for photo in client.iter_profile_photos(user):
        client.download_media(photo,
                              file="./{0}/{1}/{2}.jpg".format(target_group.id, user.id, photo.id))
