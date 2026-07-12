import flet as ft
import sympy as sp

def main(page: ft.Page):
    page.title = "Калькулятор"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#17171c"

    expression = ""

    txt_display = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        read_only=True,
        border=ft.InputBorder.NONE,
        text_size=38,
        color="white"
    )

    def button_click(e):
        nonlocal expression
        data = e.control.data

        if data == "C":
            expression = ""
            txt_display.value = "0"
        elif data == "⌫":
            expression = expression[:-1]
            txt_display.value = expression if expression else "0"
        elif data == "=":
            try:
                expr_str = expression.replace("√", "sqrt").replace("π", "pi").replace("e", "E")
                expr = sp.sympify(expr_str)
                result = expr.evalf()
                
                if result.is_integer:
                    txt_display.value = str(int(result))
                else:
                    txt_display.value = f"{result:.6g}"
                expression = txt_display.value
            except Exception:
                txt_display.value = "Ошибка"
                expression = ""
        elif data in ["sin", "cos", "tan", "ln", "log"]:
            expression += f"{data}("
            txt_display.value = expression
        elif data == "√":
            expression += "√("
            txt_display.value = expression
        else:
            expression += data
            txt_display.value = expression

        page.update()

    def btn(text, bg_color="#212124", text_color="white"):
        return ft.Container(
            content=ft.Text(text, color=text_color, weight=ft.FontWeight.BOLD, size=18),
            alignment=ft.alignment.center,
            border_radius=10,
            bgcolor=bg_color,
            expand=True,
            on_click=button_click,
            data=text
        )

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Container(content=txt_display, padding=10, expand=1),
                ft.Row([btn("sin", "#2c2c35"), btn("cos", "#2c2c35"), btn("tan", "#2c2c35"), btn("ln", "#2c2c35"), btn("log", "#2c2c35")], expand=True),
                ft.Row([btn("π", "#2c2c35"), btn("e", "#2c2c35"), btn("√", "#2c2c35"), btn("^", "#2c2c35"), btn("(", "#2c2c35"), btn(")", "#2c2c35")], expand=True),
                ft.Row([btn("C", "#a5a5a5", "black"), btn("⌫", "#a5a5a5", "black"), btn("%", "#a5a5a5", "black"), btn("/", "#ff9f0a")], expand=True),
                ft.Row([btn("7"), btn("8"), btn("9"), btn("*", "#ff9f0a")], expand=True),
                ft.Row([btn("4"), btn("5"), btn("6"), btn("-", "#ff9f0a")], expand=True),
                ft.Row([btn("1"), btn("2"), btn("3"), btn("+", "#ff9f0a")], expand=True),
                ft.Row([btn("0"), btn("."), btn("=", "#ff9f0a")], expand=True),
            ], alignment=ft.MainAxisAlignment.END, expand=True),
            padding=10,
            expand=True
        )
    )

ft.app(target=main)
