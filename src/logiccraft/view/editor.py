import flet as ft

class DiagramEditor(ft.GestureDetector):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.content = ft.Stack()
        self.on_tap_down = self.handle_tap
        self.mouse_cursor = ft.MouseCursor.PRECISE

    def handle_tap(self, e: ft.TapEvent):
        # В твоей версии координаты лежат здесь:
        # e.local_position — это объект с атрибутами x и y
        x = getattr(e.local_position, "x", 0)
        y = getattr(e.local_position, "y", 0)

        print(f"Final coordinates: X={x}, Y={y}")

        self.content.controls.append(
            ft.Container(
                content=ft.Text("New Class", color=ft.Colors.WHITE, size=10),
                bgcolor=ft.Colors.BLUE_600,
                width=100,
                height=60,
                border_radius=5,
                # ИСПРАВЛЕНО: Alignment теперь только так
                alignment=ft.Alignment(0, 0),
                left=x,
                top=y,
                shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK26)
            )
        )
        self.update()