import flet as ft

def main(page: ft.Page):
    def passou(e):
        if(e.control.bgcolor == "lightblue"):
            e.control.bgcolor = "green"
        
        else:
            e.control.bgcolor = "lightblue"
        





    page.title = "Aula 6 - Container"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    def clicou(e):
            page.add(
                ft.Text("DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-LHE RATÃOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"),
            ),



    page.add(
        ft.Container(
            content=ft.Text(''),
                            bgcolor='lightblue',
                            padding=20,
                            margin=15,
                            border=ft.Border.all(3, ft.Colors.BLACK),
                            border_radius= 10,
                            width=300,
                            height=300,
                            on_click= clicou,
                            on_hover= passou,
                            image=ft.DecorationImage(
                                src="image/ratao.jpg",
                                fit=ft.BoxFit.COVER
                                
                            ),

        )
    )

ft.run(main)