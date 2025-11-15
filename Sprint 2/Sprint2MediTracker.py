# Meditrack - Sprint 2 CMSC-355 Fall 2025
# By Zain Al Rawi, Ashely Kubyako, Samir Yesli, Kyle Uson, Jamie Torrico, Rayyan Siddiqui
# https://youtu.be/wLo_eb8KOt4

import tkinter
from tkinter import messagebox
import re  # needed for email validation

window = tkinter.Tk()
window.title("Meditrack")
window.geometry('440x540')
window.configure(bg="#0C1155")

# Very small "database"
users = {
    "existinguser@example.com": {"name": "Existing User", "password": "ExistingPassword"}
}

def open_register_window():
    reg = tkinter.Toplevel(window)
    reg.title("Create Account")
    reg.geometry("380x260")
    reg.configure(bg="#0C1155")

    # Widgets
    tk_label = lambda text: tkinter.Label(reg, text=text, bg="#0C1155", fg="#7968A1", font=("Arial", 14))
    tk_entry = lambda show=None: tkinter.Entry(reg, font=("Arial", 14), show=show, width=25)

    name_label = tk_label("Full name")
    name_entry = tk_entry()

    email_label = tk_label("Email")
    email_entry = tk_entry()

    pw_label = tk_label("Password")
    pw_entry = tk_entry(show="*")

    confirm_label = tk_label("Confirm password")
    confirm_entry = tk_entry(show="*")

    def create_account():
        full = name_entry.get()
        email = email_entry.get()
        pw = pw_entry.get()
        cpw = confirm_entry.get()

        # EMPTY FIELD CHECK
        if full == "" or email == "" or pw == "" or cpw == "":
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # TC04 – INVALID EMAIL FORMAT
        email_pattern = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_pattern, email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return

        # TC02 – PASSWORD TOO SHORT
        if len(pw) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters.")
            return

        # PASSWORD MISMATCH
        if pw != cpw:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # TC03 – DUPLICATE EMAIL
        if email in users:
            messagebox.showerror("Error", "Email already exists.")
            return

        # TC01 – SUCCESS
        users[email] = {"name": full, "password": pw}
        messagebox.showinfo("Success", "Account created successfully.")
        reg.destroy()

    # Layout
    name_label.grid(row=0, column=0, padx=20, pady=10)
    name_entry.grid(row=0, column=1)

    email_label.grid(row=1, column=0, padx=20, pady=10)
    email_entry.grid(row=1, column=1)

    pw_label.grid(row=2, column=0, padx=20, pady=10)
    pw_entry.grid(row=2, column=1)

    confirm_label.grid(row=3, column=0, padx=20, pady=10)
    confirm_entry.grid(row=3, column=1)

    tkinter.Button(
        reg, text="Create Account", bg="#0C1155", fg="#7968A1",
        font=("Arial", 14), command=create_account
    ).grid(row=4, column=0, columnspan=2, pady=20)

# Main UI
tkinter.Button(
    window, text="Create Account", bg="#0C1155", fg="#7968A1",
    font=("Arial", 16), command=open_register_window
).pack(pady=200)

window.mainloop()