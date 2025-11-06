# Meditrack - Sprint 1 CMSC-355 Fall 2025
# By Zain Al Rawi, Ashely Kubyako, Samir Yesli, Kyle Uson, Jamie Torrico, Rayyan Siddiqui
# https://youtu.be/KW7Xd74p8Ns

import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Meditrack")
window.geometry('440x540')
window.configure(bg = "#0C1155")

# Temporary login data (will be changed to SQLite when scaled)
def login():
    dict_info = {
        "JohnDoe": "password123",
        "AliceSmith": "qwerty",
        "BobJohnson": "arandompass"
    }
    if "" in username_entry.get() or "" in password_entry.get():
        messagebox.showerror(title = "Invalid Login", message = "Please fill in all fields")
        return
        
    # Login user input
    username = username_entry.get()
    password = password_entry.get()
    if username in dict_info and dict_info[username] == password:
        messagebox.showinfo(title = "Login Success", message = "Login Success")
    else:
        messagebox.showerror(title = "Error", message = "Invalid login.")

frame = tkinter.Frame(bg = '#0C1155')

# Widget creation (buttons and labels)
login_label = tkinter.Label(
    frame, text = "Login", bg = '#0C1155', fg = "#7968A1", font = ("Arial", 30))
username_label = tkinter.Label(
    frame, text = "Username", bg = '#0C1155', fg = "#7968A1", font = ("Arial", 16))
username_entry = tkinter.Entry(frame, font = ("Arial", 16))
password_entry = tkinter.Entry(frame, show = "*", font = ("Arial", 16))
password_label = tkinter.Label(
    frame, text = "Password", bg = '#0C1155', fg = "#7968A1", font = ("Arial", 16))
login_button = tkinter.Button(
    frame, text = "Login", bg = "#0C1155", fg = "#7968A1", font = ("Arial", 16), command = login)

# Placing widgets on the grid (spacing)
login_label.grid(row = 0, column = 0, columnspan = 2, sticky = "news", pady = 20)
username_label.grid(row = 1, column = 0)
username_entry.grid(row = 1, column = 1, pady = 20)
password_label.grid(row = 2, column = 0)
password_entry.grid(row = 2, column = 1, pady = 20)
login_button.grid(row = 3, column = 0, columnspan = 2, pady = 30)

frame.pack()

window.mainloop()


