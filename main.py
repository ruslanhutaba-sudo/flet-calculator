import flet as ft
import sympy as sp

def main(page: ft.Page):
    page.title = "Калькулятор"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#17171c"
    
    # Переменная для хранения выражения
    page.expr = ""

    txt_display = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        read_only=True,
        border=ft.InputBorder.NONE,
        text_size=40,
        color="white"
    )

    def button_click(e):
        data = e.control.data
        if data == "C":
            page.expr = ""
            txt_display.value = "0"
        elif data == "⌫":
            page.expr = page.expr[:-1]
            txt_display.value = page.expr if page.expr else "0"
        elif data == "=":
            try:
                # Базовая замена символов для sympy
                clean_expr = page.expr.replace("√", "sqrt").replace("π", "pi").replace("e", "E")
                result = sp.sympify(clean_expr).evalf()
                if result.is_integer:
                    txt_display.value = str(int(result))
                else:
                    txt_display.value = f"{result:.6g}"
                page.expr = txt_display.value
            except:
                txt_display.value = "Ошибка"
                page.expr = ""
        else:
            page.expr += str(data)
            txt_display.value = page.expr
        
        page.update()

    def btn(text, bg="#212124", text_color="white"):
        return ft.ElevatedButton(
            text=text,
            bgcolor=bg,
            color=text_color,
            on_click=button_click,
            data=text,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
            expand=True
        )

    page.add(
        ft.Column([
            ft.Container(content=txt_display, padding=20),
            ft.Row([btn("sin", "#2c2c35"), btn("cos", "#2c2c35"), btn("tan", "#2c2c35"), btn("ln", "#2c2c35")], expand=True),
            ft.Row([btn("π", "#2c2c35"), btn("e", "#2c2c35"), btn("√", "#2c2c35"), btn("^", "#2c2c35")], expand=True),
            ft.Row([btn("C", "#a5a5a5", "black"), btn("⌫", "#a5a5a5", "black"), btn("(", "#a5a5a5", "black"), btn("/", "#ff9f0a")], expand=True),
            ft.Row([btn("7"), btn("8"), btn("9"), btn("*", "#ff9f0a")], expand=True),
            ft.Row([btn("4"), btn("5"), btn("6"), btn("-", "#ff9f0a")], expand=True),
            ft.Row([btn("1"), btn("2"), btn("3"), btn("+", "#ff9f0a")], expand=True),
            ft.Row([btn("0"), btn("."), btn(")", "#212124"), btn("=", "#ff9f0a")], expand=True),
        ], expand=True)
    )

ft.app(target=main)
