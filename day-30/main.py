from tkinter import *
from tkinter import messagebox
import random
import string
from pathlib import Path
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    password_length = 12
    
    password_chars = random.choices(letters + numbers + symbols, k=password_length)
    password = ''.join(password_chars)
    
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    ui.clipboard_clear()  # Clear the clipboard
    ui.clipboard_append(password)  # Append the password to the clipboard
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username, 
            "password": password,
            }
        }
    
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Hold on now!", message="Please dont leave any fields blank!")
    else:
        with open("data.json", 'w') as data_file:
            json.dump(new_data, data_file, indent=4)
            
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    
# ---------------------------- DELETE TEXT FILE ------------------------------- #

def delete_text_file():
    file_path = Path(".secrete_logins.txt")
    
    if file_path.exists():
        file_path.unlink()
        print(f"{file_path} has been deleted.")
    else:
        print(f"{file_path} does not exist.")

# ---------------------------- UI SETUP ------------------------------- #
ui = Tk()
ui.title('Password Manager')
ui.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

#Buttons
password_btn = Button(text="Generate Password", width=11, command=generate_password)
password_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=33, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)
delete_btn = Button(text="Delete Text File", width=33, command=delete_text_file)
delete_btn.grid (row=5, column=1, columnspan=2)

ui.mainloop()