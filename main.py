from tkinter import *
from tkinter import messagebox



from pass_manager import PasswordManager


BG_COLOR = "#FEFBF6"




window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)
window.resizable(width=False, height=False)

canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:", bg=BG_COLOR)
website.grid(column=0, row=1)

user_name = Label(text="Email/Username:", bg=BG_COLOR)
user_name.grid(column=0, row=2)

password_label = Label(text="Password:", bg=BG_COLOR)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=42)
website_entry.grid(column=1, row=1, columnspan=3)
website_entry.focus()

user_name_entry = Entry(width=42)
user_name_entry.insert(END, "agra@email.com")
user_name_entry.grid(column=1, row=2, columnspan=3)

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)


p_manager = PasswordManager(p_entry=password_entry, web_entry=website_entry, uname_entry=user_name_entry, end_point=END, m_box=messagebox)
# Buttons
password_btn = Button(text="New", width=5, command=p_manager.generate_password)
password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=35, command=p_manager.save_password)
add_btn.grid(column=1, row=4, columnspan=3)

window.mainloop()



