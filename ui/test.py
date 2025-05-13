import tkinter as tk

root = tk.Tk()
root.configure(bg="white")  # Set background color
label = tk.Label(root, text="Hello, World!", bg="white", fg="black")
label.pack(padx=20, pady=20)
root.update()  # Force update
root.mainloop()