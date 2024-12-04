
# Password Manager

A simple and secure password manager application built with Python and Tkinter. This application allows users to generate strong passwords, save them along with associated usernames and websites, and easily copy passwords to the clipboard.

## Features

- **Password Generation**: Create strong, random passwords with a mix of letters, numbers, and symbols.
- **Save Passwords**: Store passwords securely in a JSON file.
- **User-Friendly Interface**: Intuitive graphical user interface (GUI) built with Tkinter.
- **Clipboard Support**: Automatically copies generated passwords to the clipboard for easy pasting.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)
- `pyperclip` library (for clipboard functionality)

You can install the `pyperclip` library using pip:

```bash
pip install pyperclip
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone this project
   cd password-manager
   py install pyperclip
   ```

2. **Run the Application**:
   Make sure you have Python installed, then run the following command:
   ```bash
   python pass_manager.py
   ```

## Usage

1. **Generate a Password**:
   - Click the "New" button to generate a random password.
   - The generated password will be displayed in the password entry field and copied to your clipboard.

2. **Save a Password**:
   - Fill in the website, username, and password fields.
   - Click the "Add" button to save the password. A confirmation dialog will appear to confirm the details before saving.

3. **View Saved Passwords**:
   - The passwords are saved in a file named `passwords.txt` in JSON format. You can open this file to view your saved passwords.

## File Structure

```
password-manager/
│
├── main.py                # Main project, contains tkinter Gui
├── pass_manager.py        # Class for saving and generating passwords
├── passwords.txt          # File to store saved passwords
└── logo.png               # Logo image for the application
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
