import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("600x400")


root.grid_rowconfigure(0, weight=1)  # Space above the widgets
root.grid_rowconfigure(1, weight=0)  # UserID row  <---- Use weight=0 so that there isn't a gap btwn widgets when window is resized
root.grid_rowconfigure(2, weight=0)  # Password row
root.grid_rowconfigure(3, weight=0)  # Login button row
root.grid_rowconfigure(4, weight=1)  # Space below the widgets
    
root.grid_columnconfigure(0, weight=1)  # Space to the left
root.grid_columnconfigure(1, weight=0)  # Widgets column
root.grid_columnconfigure(2, weight=0)  # Widgets column
root.grid_columnconfigure(3, weight=1)  # Space to the right

# Widgets
user_label = tk.Label(root, text="UserID:")
password_label = tk.Label(root, text="Password:")
user_entry = tk.Entry(root)
password_entry = tk.Entry(root)
login_button = tk.Button(root, text="Login")

# Place widgets into the grid
user_label.grid(row=1, column=1, padx=5, pady=5, sticky="e")
user_entry.grid(row=1, column=2, padx=5, pady=5, sticky="w")
password_label.grid(row=2, column=1, padx=5, pady=5, sticky="e")
password_entry.grid(row=2, column=2, padx=5, pady=5, sticky="w")
login_button.grid(row=3, column=1, columnspan=2, pady=10)

root.mainloop()
