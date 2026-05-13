import customtkinter as ctk

from logic import calculate_as_str
from assets import get_asset_config

class CalculatorGui:
    def __init__(self):
        self.app: ctk.CTk = ctk.CTk()
        self.app.title("Calcualtor")
        self.app.geometry("320x432")

        self.number_buttons: dict[int, ctk.CTkButton] = {}
        self.asset_config: dict = get_asset_config(self)

        # generate grid
        self.rows: int = 6
        self.columns: int = 4

        for row in range(self.rows):
            for column in range(self.columns):
                self.app.grid_rowconfigure(row, weight=1)
                self.app.grid_columnconfigure(column, weight=1)


        # calculation label
        self.label_calculation: ctk.CTkLabel = ctk.CTkLabel(master=self.app, text="")
        self.label_calculation.grid(row=0, column=0, columnspan=4, sticky="nsew")


        # numbers
        button_number_9: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["numbers"]["9"])
        button_number_9.grid(row=2, column=2, padx=2, pady=2, sticky="nsew")
        self.number_buttons[9] = button_number_9

        button_number_8: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["numbers"]["8"])
        button_number_8.grid(row=2, column=1, padx=2, pady=2, sticky="nsew")
        self.number_buttons[8] = button_number_8

        button_number_7: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["numbers"]["7"])
        button_number_7.grid(row=2, column=0, padx=2, pady=2, sticky="nsew")
        self.number_buttons[7] = button_number_7

        button_number_6: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["numbers"]["6"])
        button_number_6.grid(row=3, column=2, padx=2, pady=2, sticky="nsew")
        self.number_buttons[6] = button_number_6

        button_number_5: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["numbers"]["5"])
        button_number_5.grid(row=3, column=1, padx=2, pady=2, sticky="nsew")
        self.number_buttons[5] = button_number_5

        button_number_4: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["numbers"]["4"])
        button_number_4.grid(row=3, column=0, padx=2, pady=2, sticky="nsew")
        self.number_buttons[4] = button_number_4

        button_number_3: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["numbers"]["3"])
        button_number_3.grid(row=4, column=2, padx=2, pady=2, sticky="nsew")
        self.number_buttons[3] = button_number_3

        button_number_2: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["numbers"]["2"])
        button_number_2.grid(row=4, column=1, padx=2, pady=2, sticky="nsew")
        self.number_buttons[2] = button_number_2

        button_number_1: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["numbers"]["1"])
        button_number_1.grid(row=4, column=0, padx=2, pady=2, sticky="nsew")
        self.number_buttons[1] = button_number_1

        button_number_0: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["numbers"]["0"])
        button_number_0.grid(row=5, column=1, padx=2, pady=2, sticky="nsew")
        self.number_buttons[0] = button_number_0


        # divide button
        self.button_divide: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["operators"]["/"])
        self.button_divide.grid(row=2, column=3, padx=2, pady=2, sticky="nsew")

        # multiplication button
        self.button_multiplication: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["operators"]["*"])
        self.button_multiplication.grid(row=3, column=3, padx=2, pady=2, sticky="nsew")

        # subtraction button
        self.button_subtraction: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["operators"]["-"])
        self.button_subtraction.grid(row=4, column=3, padx=2, pady=2, sticky="nsew")

        # addition button
        self.button_addition: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["operators"]["+"])
        self.button_addition.grid(row=5, column=3, padx=2, pady=2, sticky="nsew")


        # equals button
        self.button_equals: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["special"]["="])
        self.button_equals.grid(row=5, column=2, padx=2, pady=2, sticky="nsew")

        # back button
        self.button_back: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["special"]["back"])
        self.button_back.grid(row=1, column=3, padx=2, pady=2, sticky="nsew")

        # clear button
        self.button_clear: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["special"]["clear"])
        self.button_clear.grid(row=1, column=2, padx=2, pady=2, sticky="nsew")

        # open bracket button
        self.button_open_bracket: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["special"]["("])
        self.button_open_bracket.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")

        # close bracket button
        self.button_close_bracket: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["special"][")"])
        self.button_close_bracket.grid(row=1, column=1, padx=2, pady=2, sticky="nsew")

        # dot button
        self.button_dot: ctk.CTkButton = ctk.CTkButton(**self.asset_config["buttons"]["special"]["."])
        self.button_dot.grid(row=5, column=0, padx=2, pady=2, sticky="nsew")


        self.app.mainloop()

    def append(self, msg: str) -> None:
        self.label_calculation.configure(text=f"{self.label_calculation.cget("text")}{msg}")


    def calculate(self) -> None:
        try:
            self.label_calculation.configure(text=f"{calculate_as_str(self.label_calculation.cget("text"))}")
        except Exception:
            self.label_calculation.configure(text="Invalid")


    def remove_last_char(self) -> None:
        self.label_calculation.configure(text=f"{self.label_calculation.cget("text")[:-1]}")

calc = CalculatorGui()