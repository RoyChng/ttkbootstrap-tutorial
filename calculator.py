import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Calculator(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(padding=10, *args, **kwargs)
        self.pack(fill="both", expand=True)
        ttk.Style().configure("TButton", font="TkFixedFont 16")

        display_frame = ttk.Frame(self)
        display_frame.pack(side="top", fill="both", expand=True)

        display_label = ttk.Label(display_frame, text="00")
        display_label.configure(font=("Arial", 16, "bold"))
        display_label.pack(side="right", fill="both", expand=True)

        numpad_frame = ttk.Frame(self)
        numpad_frame.pack(side="top", fill="both", expand=True)

        button_del = ttk.Button(numpad_frame, text="DEL", style=SECONDARY)
        button_del.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)

        button_c = ttk.Button(numpad_frame, text="C", style=SECONDARY)
        button_c.grid(row=0, column=2, sticky="nsew", padx=1, pady=1)

        button_9 = ttk.Button(numpad_frame, text="9", style=PRIMARY)
        button_9.grid(row=1, column=2, sticky="nsew", padx=1, pady=1)

        button_8 = ttk.Button(numpad_frame, text="8", style=PRIMARY)
        button_8.grid(row=1, column=1, sticky="nsew", padx=1, pady=1)

        button_7 = ttk.Button(numpad_frame, text="7", style=PRIMARY)
        button_7.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)

        button_6 = ttk.Button(numpad_frame, text="6", style=PRIMARY)
        button_6.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)

        button_5 = ttk.Button(numpad_frame, text="5", style=PRIMARY)
        button_5.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)

        button_4 = ttk.Button(numpad_frame, text="4", style=PRIMARY)
        button_4.grid(row=2, column=0, sticky="nsew", padx=1, pady=1)

        button_3 = ttk.Button(numpad_frame, text="3", style=PRIMARY)
        button_3.grid(row=3, column=2, sticky="nsew", padx=1, pady=1)

        button_2 = ttk.Button(numpad_frame, text="2", style=PRIMARY)
        button_2.grid(row=3, column=1, sticky="nsew", padx=1, pady=1)

        button_1 = ttk.Button(numpad_frame, text="1", style=PRIMARY)
        button_1.grid(row=3, column=0, sticky="nsew", padx=1, pady=1)

        button_divide = ttk.Button(numpad_frame, text="÷", style=SECONDARY)
        button_divide.grid(row=0, column=3, sticky="nsew", padx=1, pady=1)

        button_multiply = ttk.Button(numpad_frame, text="×", style=SECONDARY)
        button_multiply.grid(row=1, column=3, sticky="nsew", padx=1, pady=1)

        button_subtract = ttk.Button(numpad_frame, text="-", style=SECONDARY)
        button_subtract.grid(row=2, column=3, sticky="nsew", padx=1, pady=1)

        button_add = ttk.Button(numpad_frame, text="+", style=SECONDARY)
        button_add.grid(row=3, column=3, sticky="nsew", padx=1, pady=1)

        button_0 = ttk.Button(numpad_frame, text="0", style=PRIMARY)
        button_0.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)

        button_decimal = ttk.Button(numpad_frame, text=".", style=PRIMARY)
        button_decimal.grid(row=4, column=2, sticky="nsew", padx=1, pady=1)

        button_equal = ttk.Button(numpad_frame, text="=", style=SUCCESS)
        button_equal.grid(row=4, column=3, sticky="nsew", padx=1, pady=1)

        for i in range(4):
            numpad_frame.columnconfigure(index=i, weight=1)

        for i in range(5):
            numpad_frame.rowconfigure(index=i, weight=1)


if __name__ == "__main__":
    app = ttk.Window("Calculator", themename="superhero")
    app.geometry("500x600")
    Calculator(app)
    app.mainloop()

        


