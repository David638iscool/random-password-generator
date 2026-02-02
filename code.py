import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def show_password():
    # Get the length from the entry field and generate the password
    length = int(length_entry.get())
    password = generate_password(length)

    # Clear the text widget and insert the password (masked with '•' character)
    password_var.set('•' * length)
    password_entry.config(state='normal')
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state='readonly')

def copy_password():
    # Copy the password to the clipboard
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())

# Set up the main Tkinter window
window = tk.Tk()
window.title("Password Generator")

# Input for password length
tk.Label(window, text="Enter password length:").pack(pady=10)
length_entry = tk.Entry(window)
length_entry.pack(pady=10)

# Button to generate the password
generate_button = tk.Button(window, text="Generate Password", command=show_password)
generate_button.pack(pady=10)

# Display the masked password and allow copying
password_var = tk.StringVar()
password_entry = tk.Entry(window, textvariable=password_var, show='•', state='readonly', width=25)
password_entry.pack(pady=10)

# Button to copy the password to clipboard
copy_button = tk.Button(window, text="Copy Password", command=copy_password)
copy_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
