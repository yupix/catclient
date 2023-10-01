import asyncio
import flet as ft

from packages.gui.main import gui_main
from packages.misskey_client.main import misskey_client_main



async def main():
    await asyncio.gather(*[ft.app_async(gui_main), misskey_client_main()])
    await asyncio.gather(*[ft.app_async(gui_main)])

if __name__ == '__main__':

    asyncio.run(main())