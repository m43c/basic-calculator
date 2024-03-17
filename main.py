from tkinter import Tk, Text, Button, END
from tkinter.font import Font


class Application:
    def __init__(self, master):
        # Main window setting
        self.master = master
        self.master.title("Calculate")
        self.master.config(padx=5, pady=5)

        # My font style
        self.font_style = Font(family="Monospace", size=10)

        # Settings and location of the screen
        self.screen = Text(
            master,
            font=("Monospace", 14),
            width=20,
            height=1,
            state="disabled",
        )
        self.screen.grid(row=0, column=0, columnspan=5, pady=5)

        # Operation variable for each mathematical operations
        self.operation = ""

        # Button definition
        btn7 = self.create_button(7)
        btn8 = self.create_button(8)
        btn9 = self.create_button(9)
        del_btn = self.create_button("DEL", writing=False)
        ac_btn = self.create_button("AC", writing=False)

        btn4 = self.create_button(4)
        btn5 = self.create_button(5)
        btn6 = self.create_button(6)
        mult_btn = self.create_button("*")
        div_btn = self.create_button("/")

        btn1 = self.create_button(1)
        btn2 = self.create_button(2)
        btn3 = self.create_button(3)
        add_btn = self.create_button("+")
        sub_btn = self.create_button("-")

        btn0 = self.create_button(0)
        point_btn = self.create_button(".")
        equal_btn = self.create_button("=", writing=False, breadth=14)

        # Button location
        buttons = [
            btn7,
            btn8,
            btn9,
            del_btn,
            ac_btn,
            btn4,
            btn5,
            btn6,
            mult_btn,
            div_btn,
            btn1,
            btn2,
            btn3,
            add_btn,
            sub_btn,
            btn0,
            point_btn,
            equal_btn,
        ]

        row = 0
        column = 5

        for i in range(1, 5):
            if i == 4:
                column = 3

            for j in range(column):
                buttons[row].grid(row=i, column=j)
                row += 1

        buttons[17].grid(row=4, column=2, columnspan=3)

    def create_button(self, value, writing=True, breadth=2):
        return Button(
            self.master,
            text=value,
            width=breadth,
            cursor="hand2",
            font=self.font_style,
            command=lambda: self.capture_text(value, writing),
        )

    def capture_text(self, text, writing):
        if not writing:
            if text == "=" and self.operation != "":
                result = str(eval(self.operation))
                # self.operation = ""
                self.all_clear()
                self.show_text(result)
            elif text == "DEL":
                self.delete()
            elif text == "AC":
                self.operation = ""
                self.all_clear()

        else:
            self.operation += str(text)
            self.show_text(text)

    def all_clear(self):
        self.screen.configure(state="normal")
        self.screen.delete("1.0", "end-1c")
        self.screen.configure(state="disabled")

    def delete(self):
        self.screen.configure(state="normal")
        self.screen.delete("end-2c")
        self.screen.configure(state="disabled")

    def show_text(self, value):
        self.screen.configure(state="normal")
        self.screen.tag_configure("right", justify="right")
        self.screen.insert(END, value, "right")
        self.screen.configure(state="disabled")


if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
