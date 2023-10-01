import flet as ft
from mipac.models.note import Note

from packages.shared.stores.notes import NoteStore
from packages.shared.utils.common import common_elements


class TimeLine(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.column = ft.Column([])
        NoteStore.bind(self.on_update_handler)

    async def _create_note_view(self, note: Note):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Image(
                                src=note.author.avatar_url, width=40, height=40
                            ),
                            title=ft.Text(
                                (note.author.nickname or note.author.username)
                                + "@"
                                + note.author.username
                                + (
                                    note.author.instance.name
                                    if note.author.instance
                                    else ""
                                )
                            ),
                            subtitle=ft.Text(note.content),
                        ),
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.REPLY,
                                    icon_size=14,
                                    tooltip="返信",
                                ),
                                ft.IconButton(
                                    icon=ft.icons.REPEAT,
                                    icon_size=14,
                                    tooltip="リノート",
                                ),
                                ft.IconButton(
                                    icon=ft.icons.ADD,
                                    icon_size=14,
                                    tooltip="リアクションを追加",
                                )
                            ]
                        ),
                    ]
                )
            )
        )

    async def on_update_handler(self, prevent_value: list[Note], value: list[Note]):
        notes = await common_elements(
            [i._note for i in prevent_value], [i._note for i in value], "id"
        )
        for note in notes:
            print(self.column.controls)
            self.column.controls.insert(
                0, await self._create_note_view(Note(note, client=value[0]._client))
            )
        await self.update_async()

    def build(self):
        return self.column
