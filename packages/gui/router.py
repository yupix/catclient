import flet as ft

from packages.gui.components.timeline import TimeLine

ROUTES = {
    '/': [ft.View('/', [ft.AppBar(title=ft.Text('Test'))])]
}

async def use_gui_router(page: ft.Page):


    async def router(handler: ft.TemplateRoute):
        troute = ft.TemplateRoute(handler.route)

        if troute.match('/'):
            page.views.append(ft.View('/', [ 
                ft.Row([
                                        ft.Column([ft.Text('test')]),

                    ft.Container(TimeLine(), width=450, height=500),
                                                            ft.Column([ft.Text('test')]),

                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                # ft.Row([
                    # ft.Column([ft.Text('test')]),
                    # ft.Column([TimeLine()]),
                    # ft.Column([ft.Text('test')]),
                # ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

                
                ]))
        await page.update_async()
    return router