from mipac.models.note import Note

from packages.shared.utils.state import UseState


NoteStore = UseState[list[Note]]([])