import random
import json
from pathlib import Path
import pyperclip


LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
path = Path("password.txt")

class PasswordManager:
    def __init__(self, p_entry, uname_entry, m_box, web_entry, end_point):
        self.password_entry = p_entry
        self.website_entry = web_entry
        self.messagebox = m_box
        self.user_name_entry = uname_entry
        self.END  = end_point

    def generate_password(self):
        self.password_entry.delete(0, "end")
        nr_letters = random.randint(8, 12)
        nr_symbols = random.randint(5, 8)
        nr_numbers = random.randint(3, 6)
        password_letters = [random.choice(LETTERS) for _ in range(1, nr_letters + 1)]
        password_symbols = [random.choice(SYMBOLS) for _ in range(1, nr_symbols + 1)]
        password_numbers = [random.choice(NUMBERS) for _ in range(1, nr_numbers + 1)]
        password_list = password_letters + password_symbols + password_numbers
        random.shuffle(password_list)
        password = "".join(password_list)
        print(password)
        self.password_entry.insert(self.END, password)
        pyperclip.copy(password)

    def save_password(self):
        web_url = self.website_entry.get()
        u_name = self.user_name_entry.get()
        passwrd = self.password_entry.get()
        if len(web_url) == 0 or len(passwrd) == 0:
            self.messagebox.showinfo(title="Oops", message="Make sure you didn't leave any field empty")
        else:

            login = {
                "website": web_url,
                "user_name": u_name,
                "password": passwrd,
            }
            data = {}
            if path.is_file():
                print("exists")
                with open(file="passwords.txt") as f:
                    data += json.load(f)
            data.update(login)

            is_ok = self.messagebox.askokcancel(title=login["website"], message=f" Save website:{web_url} "
                                                                           f"\nuser name: {u_name}"
                                                                           f"\npassword: {passwrd} ?")

            if is_ok:
                with open(file="passwords.txt", mode="a") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)

    # ---------------------------- UI SETUP ------------------------------- #