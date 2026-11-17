# Python Calculator (Tkinter)

A simple calculator app built with Python and Tkinter.
It supports basic arithmetic, decimals, percentages, and a soft dark UI.

This is a learning project, originally written in 2023.

## Features

- Dark UI with color-coded buttons
- Basic operations: `+`, `-`, `*`, `/`, `%`
- Decimal numbers (`.`)
- Sign toggle (`+/-`)
- Backspace (`<`)
- Clear (`C`)
- Multiple-dot and double-operator protection
- Friendly error messages (`Cannot divide by 0`, `Error`)
- Read-only display (input only via buttons)
- Startup "About" popup

## Requirements

- Python 3.8 or newer
- Tkinter (usually included with Python)

On Linux you may need to install Tkinter separately:

```bash
# Debian / Ubuntu
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

No third-party Python packages are required.

## How to Run

### 1. Check that Python is installed

```bash
python --version
```

If that does not work, try:

```bash
python3 --version
```

### 2. Download or clone the project

```bash
git clone https://github.com/USERNAME/python-calculator.git
cd python-calculator
```

Or simply download the files and open a terminal in the project folder.

### 3. Run the app

```bash
python calculator.py
```

If `python` is not recognized:

```bash
python3 calculator.py
```

A window should open. If it does not, make sure Tkinter is installed.

## How to Use

- Click the number buttons to enter digits.
- Use `.` for decimals.
- Use `+`, `-`, `*`, `/`, `%` for operations.
- Press `=` to see the result.
- Press `C` to clear everything.
- Press `<` to delete the last character.
- Press `+/-` to toggle the sign of the expression.

## Project Structure

```
.
├── calculator.py    # Main app
├── README.md        # This file
├── LICENSE          # MIT License
└── .gitignore       # Ignored files
```

## Possible Future Improvements

- Keyboard input support
- Calculation history
- Memory buttons (`M+`, `M-`, `MR`, `MC`)
- Parentheses support
- Unit conversion tab

## Author

**Mohammad**

Built with Python and Tkinter.

## License

This project is open source and available under the MIT License.