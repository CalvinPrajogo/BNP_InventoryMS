import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("600x400")


root.grid_rowconfigure(0, weight=1)  # Space above the widgets
root.grid_rowconfigure(1, weight=0)  # UserID row  <---- Use weight=0 so that there isn't a gap btwn widgets when window is resized
root.grid_rowconfigure(2, weight=0)  # Password row
root.grid_rowconfigure(3, weight=0)  # Login button row
root.grid_rowconfigure(4, weight=0)  # Login Err row
root.grid_rowconfigure(5, weight=1)  # Space below the widgets
    
root.grid_columnconfigure(0, weight=1)  # Space to the left
root.grid_columnconfigure(1, weight=0)  # Widgets column
root.grid_columnconfigure(2, weight=0)  # Widgets column
root.grid_columnconfigure(3, weight=1)  # Space to the right

#Commands
def toggle_password():
    #Check whether the password box is currently masked or not
    if password_entry.cget("show") == "*":
        #Currently masked, make it visible
        password_entry.config(show="")
        togglepass_button.config(text="Hide Password")
    else:
        #Currently visible, make it hidden
        password_entry.config(show="*")
        togglepass_button.config(text="Show Password")
        
def login_attempt():
    username = user_entry.get()
    password = password_entry.get()
    if not username or not password:
        loginerr_label.config(text="Username and Password cannot be empty!")
        loginerr_label.grid(row=3, column=1, columnspan=2, pady=10)
        login_button.grid(row=4, column=1, columnspan=2, pady=10)
    else:
        print("Placeholder for backend, attempt made with username: " + username + ", password: " + password)
        loginerr_label.config(text="")
        loginerr_label.grid(row=4, column=1, columnspan=2, pady=10)
        login_button.grid(row=3, column=1, columnspan=2, pady=10)
    
def on_enter(event):
    #Widget represents which entry box the cursor was when enter was pressed
    widget = event.widget
    if widget == user_entry:
        #Move the cursor to the password box
        password_entry.focus_set()
    elif widget == password_entry:
        login_attempt()

# Widgets
user_label = tk.Label(root, text="UserID:")
password_label = tk.Label(root, text="Password:")
user_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")
login_button = tk.Button(root, text="Login", command=login_attempt)
togglepass_button = tk.Checkbutton(root, text="Show Password", command=toggle_password)
loginerr_label = tk.Label(root, text="", fg="red")

# Place widgets into the grid
user_label.grid(row=1, column=1, padx=5, pady=5, sticky="e")
user_entry.grid(row=1, column=2, padx=5, pady=5, sticky="w")
password_label.grid(row=2, column=1, padx=5, pady=5, sticky="e")
password_entry.grid(row=2, column=2, padx=5, pady=5, sticky="w")
login_button.grid(row=3, column=1, columnspan=2, pady=10)
togglepass_button.grid(row=2, column=3, sticky="w")


root.mainloop()
