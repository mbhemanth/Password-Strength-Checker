import re
import tkinter as tk
from tkinter import messagebox

def check_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?":{}|<>]", password) is None

    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Medium"
    else:
        return "Weak"

def evaluate():
    pwd = entry.get()
    if not pwd:
        messagebox.showwarning("Warning", "Please enter a password!")
        return
    result = check_strength(pwd)
    label_result.config(text=f"Password Strength: {result}", fg=("green" if result == "Strong" else "orange" if result == "Medium" else "red"))

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.config(bg="#222")

title = tk.Label(root, text="🔐 Password Strength Checker", font=("Arial", 16, "bold"), bg="#222", fg="white")
title.pack(pady=15)

entry = tk.Entry(root, show="*", font=("Arial", 14), width=25, justify="center")
entry.pack(pady=10)

btn = tk.Button(root, text="Check Strength", command=evaluate, font=("Arial", 12), bg="#4CAF50", fg="white", relief="flat")
btn.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#222")
label_result.pack(pady=10)

root.mainloop()
