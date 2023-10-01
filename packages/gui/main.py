import flet as ft

from packages.gui.router import use_gui_router

async def gui_main(page: ft.Page):
    page.views.clear()
    page.on_route_change = await use_gui_router(page)
    await page.go_async(page.route)