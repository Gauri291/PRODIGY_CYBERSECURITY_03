import tkinter as tk
import re

def check_password():
    password = entry.get()
    strength = "Weak"
    msg = []

    if len(password) >= 8:
        msg.append("✔️ Length: Good")
    else:
        msg.append("❌ Length: Should be at least 8")

    if re.search(r"[A-Z]", password):
        msg.append("✔️ Uppercase: Present")
    else:
        msg.append("❌ Uppercase: Missing")

    if re.search(r"[a-z]", password):
        msg.append("✔️ Lowercase: Present")
    else:
        msg.append("❌ Lowercase: Missing")

    if re.search(r"[0-9]", password):
        msg.append("✔️ Number: Present")
    else:
        msg.append("❌ Number: Missing")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        msg.append("✔️ Special Character: Present")
    else:
        msg.append("❌ Special Character: Missing")

    criteria = sum([
        len(password) >= 8,
        bool(re.search(r"[A-Z]", password)),
        bool(re.search(r"[a-z]", password)),
        bool(re.search(r"[0-9]", password)),
        bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    ])

    if criteria >= 4:
        strength = "Strong"
    elif criteria == 3:
        strength = "Medium"

    msg.append(f"\nPassword Strength: {strength}")
    result.config(text="\n".join(msg))

# GUI Setup
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter Password:").pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=check_password).pack(pady=10)

result = tk.Label(root, text="", justify="left")
result.pack(pady=10)

root.mainloop()
