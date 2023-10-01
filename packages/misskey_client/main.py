import os
from typing import Any

from aiohttp.client_ws import ClientWebSocketResponse
from mipa.ext import commands
from mipac.models.note import Note
from mipac.models.notification import NotificationReaction
from win11toast import toast_async
from dotenv import load_dotenv

from packages.shared.stores.notes import NoteStore

class MisskeyClient(commands.Bot):
    def __init__(self):
        super().__init__()

    async def on_ready(self, ws: ClientWebSocketResponse):
        await self.router.connect_channel(['global', 'main'])
        print('接続しました')
    
    async def on_note(self, note: Note):
        notes = list(await NoteStore.get())
        notes.append(note)
        await NoteStore.set(notes)
        # print(note.content)

    async def on_reaction(self, notice: NotificationReaction):
        _emoji = None
        async for emoji in self.client.admin.emoji.action.gets(get_all=True):
            if emoji.name == notice.reaction:
                _emoji = emoji
                break
        print(notice.user.avatar_url)
        if _emoji:
            await toast_async(f'{notice.user.username}さんに{notice.reaction}されました', icon=notice.user.avatar_url, image=_emoji.url)
        else:
            await toast_async(f'{notice.user.username}さんに{notice.reaction}されました', icon=notice.user.avatar_url)

async def misskey_client_main():
    client = MisskeyClient()
    load_dotenv()
    await client.start(os.environ.get('MISSKEY_INSTANCE_URL'), os.environ.get('MISSKEY_TOKEN'))
