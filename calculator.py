from tkinter import Tk, Frame, Entry, Button, StringVar, messagebox


# -----------------------------------------------------------------
# Color palette — soft dark theme (GitHub Dark inspired)
# -----------------------------------------------------------------
WINDOW_BG   = "#010409"
DISPLAY_BG  = "#0D1117"    # Screen background
DISPLAY_FG  = "#58D68D"    # Soft green digits

NUM_BG      = "#21262D"    # Number buttons
NUM_FG      = "#E6EDF3"

OP_BG       = "#388BFD"    # Operators
OP_FG       = "#FFFFFF"

EQUAL_BG    = "#2EA043"    # Equals
EQUAL_FG    = "#FFFFFF"

CLEAR_BG    = "#DA3633"    # Clear
CLEAR_FG    = "#FFFFFF"

ACTION_BG   = "#30363D"    # Backspace, sign, %
ACTION_FG   = "#E6EDF3"

OPERATORS   = {"+", "-", "*", "/", "%"}


class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator App")
        self.window.configure(bg=WINDOW_BG)
        self.window.resizable(False, False)

        # The full expression currently shown on the display
        self.expression = ""

        # Build UI
        self.create_frame()
        self.create_display()
        self.create_buttons()

        # Show the "About" popup shortly after the window appears,
        # so the main window is drawn first and the popup feels natural.
        self.window.after(300, self.show_about)

    # -------------------------------------------------------------
    # UI
    # -------------------------------------------------------------
    def create_frame(self):
        """Parent frame that holds the display and buttons."""
        self.frame = Frame(self.window, bg=WINDOW_BG)
        self.frame.pack(padx=10, pady=10)

    def create_display(self):
        """Read-only Entry used as the calculator display."""
        self.input_string = StringVar()

        self.display = Entry(
            master=self.frame,
            textvariable=self.input_string,
            font=("Consolas", 22, "bold"),
            width=16,
            justify="right",
            bd=20,
            insertwidth=4,
            bg=DISPLAY_BG,
            fg=DISPLAY_FG,
            readonlybackground=DISPLAY_BG,
            disabledbackground=DISPLAY_BG,
            disabledforeground=DISPLAY_FG,
            state="readonly",
        )
        self.display.grid(row=0, column=0, columnspan=5, sticky="we", pady=(0, 8))

    def create_buttons(self):
        """Create every button using a compact layout table."""
        # (label, row, column, style)
        # style: "num" | "op" | "equal" | "clear" | "action"
        layout = [
            ("C",  1, 0, "clear"),  ("7",  1, 1, "num"), ("8",  1, 2, "num"), ("9",  1, 3, "num"), ("/",  1, 4, "op"),
            ("<",  2, 0, "action"), ("4",  2, 1, "num"), ("5",  2, 2, "num"), ("6",  2, 3, "num"), ("*",  2, 4, "op"),
            ("%",  3, 0, "action"), ("1",  3, 1, "num"), ("2",  3, 2, "num"), ("3",  3, 3, "num"), ("-",  3, 4, "op"),
            ("+/-",4, 0, "action"), ("0",  4, 1, "num"), (".",  4, 2, "num"), ("=",  4, 3, "equal"), ("+", 4, 4, "op"),
        ]

        for label, row, column, style in layout:
            self._create_button(label, row, column, style)

    def _create_button(self, label, row, column, style):
        """Create one styled button and bind its callback."""
        if style == "op":
            bg, fg = OP_BG, OP_FG
        elif style == "equal":
            bg, fg = EQUAL_BG, EQUAL_FG
        elif style == "clear":
            bg, fg = CLEAR_BG, CLEAR_FG
        elif style == "action":
            bg, fg = ACTION_BG, ACTION_FG
        else:
            bg, fg = NUM_BG, NUM_FG

        if label == "=":
            command = self.equal
        elif label == "C":
            command = self.clear_input
        elif label == "<":
            command = self.backspace
        elif label == "+/-":
            command = self.negate
        else:
            command = lambda t=label: self.button_click(t)

        Button(
            master=self.frame,
            text=label,
            font=("Consolas", 16, "bold"),
            width=4,
            height=2,
            bg=bg,
            fg=fg,
            activebackground=bg,
            activeforeground=fg,
            bd=0,
            command=command,
        ).grid(row=row, column=column, padx=2, pady=2, sticky="nsew")

    def show_about(self):
        """Startup popup — shown once when the app opens."""
        messagebox.showinfo(
            "About",
            "Calculator App\n\n"
            "Written by Mohammad\n"
            "Built with Python in 2023"
        )

    # -------------------------------------------------------------
    # Handlers
    # -------------------------------------------------------------
    def button_click(self, char):
        """Append a digit, dot, or operator to the expression."""
        # Prevent two operators in a row (e.g. "5++3")
        if char in OPERATORS and self.expression and self.expression[-1] in OPERATORS:
            self.expression = self.expression[:-1]

        # Prevent multiple dots in the same number
        if char == ".":
            if "." in self._current_number():
                return

        self.expression += char
        self._update_display()

    def backspace(self):
        """Remove the last character."""
        self.expression = self.expression[:-1]
        self._update_display()

    def clear_input(self):
        """Reset the calculator."""
        self.expression = ""
        self._update_display()

    def negate(self):
        """Toggle the sign of the whole expression."""
        if not self.expression:
            return
        if self.expression.startswith("-"):
            self.expression = self.expression[1:]
        else:
            self.expression = "-" + self.expression
        self._update_display()

    def equal(self):
        """Evaluate the expression and show the result."""
        if not self.expression:
            return

        try:
            # eval() is acceptable here because the expression comes
            # only from this app's own buttons, never from raw text.
            result = str(eval(self.expression))

            # Normalize integer results (6.0 -> 6)
            if result.endswith(".0"):
                result = result[:-2]

        except ZeroDivisionError:
            self.expression = ""
            self._update_display("Cannot divide by 0")
            return

        except Exception:
            self.expression = ""
            self._update_display("Error")
            return

        self.expression = result
        self._update_display()

    # -------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------
    def _current_number(self):
        """Part of the expression after the last operator."""
        number = ""
        for ch in reversed(self.expression):
            if ch in OPERATORS:
                break
            number = ch + number
        return number

    def _update_display(self, value=None):
        """Refresh the Entry widget with the current expression."""
        self.display.configure(state="normal")
        self.input_string.set(self.expression if value is None else value)
        self.display.configure(state="readonly")


def main():
    calc = Calculator()
    calc.window.mainloop()


if __name__ == "__main__":
    main()