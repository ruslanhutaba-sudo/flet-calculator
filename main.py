import flet as ft
import sympy as sp

def main(page: ft.Page):
    page.title = "Инженерный калькулятор"
    page.window_width = 380
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#17171C"
    
    expression = ""

    txt_display = ft.TextField(
        value="0", 
        text_align=ft.TextAlign.RIGHT, 
        text_size=36, 
        border=ft.InputBorder.NONE,
        read_only=True,
        color="#FFFFFF"
    )

    def button_click(e):
        nonlocal expression
        data = e.control.text
        
        if data == "C":
            expression = ""
            txt_display.value = "0"
        elif data == "⌫":
            expression = expression[:-1]
            txt_display.value = expression if expression else "0"
        elif data == "=":
            try:
                # Заменяем знаки для SymPy
                expr_str = expression.replace("×", "*").replace("÷", "/")
                expr_str = expr_str.replace("√(", "sqrt(").replace("π", "pi")
                
                result = sp.sympify(expr_str).evalf()
                
                if result.is_integer:
                    txt_display.value = str(int(result))
                else:
                    txt_display.value = f"{result:.8g}"
                expression = txt_display.value
            except:
                txt_display.value = "Ошибка"
                expression = ""
        elif data in ["sin", "cos", "tan", "√", "log"]:
            expression += f"{data}("
            txt_display.value = expression
        else:
            if txt_display.value == "0" and data not in ["+", "-", "×", "÷"]:
                expression = data
            else:
                expression += data
            txt_display.value = expression
            
        page.update()

    def btn(text, bg_color="#2E2F38", text_color="#FFFFFF", flex=1):
        return ft.Container(
            content=ft.Text(text, size=20, color=text_color, weight=ft.FontWeight.BOLD),
            alignment=ft.alignment.center,
            bg_color=bg_color,
            border_radius=25,
            expand=flex,
            on_click=button_click,
            animate=ft.animation.Animation(200, "easeOut")
        )

    page.add(
        ft.Container(content=txt_display, padding=20, expand=2),
        ft.Column(
            expand=8,
            controls=[
                ft.Row(controls=[btn("sin", "#4E505F"), btn("cos", "#4E505F"), btn("tan", "#4E505F"), btn("log", "#4E505F")], expand=1),
                ft.Row(controls=[btn("√", "#4E505F"), btn("π", "#4E505F"), btn("^", "#4E505F"), btn("⌫", "#4E505F")], expand=1),
                ft.Row(controls=[btn("C", "#A5A5A5", "#000000"), btn("(", "#4E505F"), btn(")", "#4E505F"), btn("÷", "#FF9F0A")], expand=1),
                ft.Row(controls=[btn("7"), btn("8"), btn("9"), btn("×", "#FF9F0A")], expand=1),
                ft.Row(controls=[btn("4"), btn("5"), btn("6"), btn("-", "#FF9F0A")], expand=1),
                ft.Row(controls=[btn("1"), btn("2"), btn("3"), btn("+", "#FF9F0A")], expand=1),
                ft.Row(controls=[btn("0", flex=2), btn("."), btn("=", "#FF9F0A")], expand=1),
            ]
        )
    )

ft.app(target=main)
