import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Password Generator")
        self.master.geometry("500x400")
        self.master.resizable(False, False)
        
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        self.create_widgets()
        
    def create_widgets(self):
        main_frame = ttk.Frame(self.master, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(main_frame, text="Password Generator", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Label(main_frame, text="Password Length:").grid(row=1, column=0, sticky="w", pady=5)
        self.length_var = tk.StringVar(value="12")
        length_entry = ttk.Entry(main_frame, textvariable=self.length_var, width=5)
        length_entry.grid(row=1, column=1, sticky="w", pady=5)
        
        ttk.Label(main_frame, text="Complexity:").grid(row=2, column=0, sticky="w", pady=5)
        self.complexity_var = tk.StringVar(value="medium")
        complexities = [("Simple", "simple"), ("Medium", "medium"), ("Strong", "strong")]
        for i, (text, value) in enumerate(complexities):
            ttk.Radiobutton(main_frame, text=text, value=value, variable=self.complexity_var).grid(row=2+i, column=1, sticky="w", pady=2)
        
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(main_frame, text="Lowercase", variable=self.use_lowercase).grid(row=6, column=0, sticky="w", pady=2)
        ttk.Checkbutton(main_frame, text="Uppercase", variable=self.use_uppercase).grid(row=7, column=0, sticky="w", pady=2)
        ttk.Checkbutton(main_frame, text="Digits", variable=self.use_digits).grid(row=8, column=0, sticky="w", pady=2)
        ttk.Checkbutton(main_frame, text="Symbols", variable=self.use_symbols).grid(row=9, column=0, sticky="w", pady=2)
        
        generate_button = ttk.Button(main_frame, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=10, column=0, columnspan=2, pady=(20, 10))
        
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(main_frame, textvariable=self.password_var, width=30, font=("Courier", 12))
        password_entry.grid(row=11, column=0, columnspan=2, pady=(0, 10))
        
        copy_button = ttk.Button(main_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=12, column=0, columnspan=2)
        
    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length < 4:
                raise ValueError("Password length must be at least 4 characters.")
            
            char_sets = []
            if self.use_lowercase.get():
                char_sets.append(string.ascii_lowercase)
            if self.use_uppercase.get():
                char_sets.append(string.ascii_uppercase)
            if self.use_digits.get():
                char_sets.append(string.digits)
            if self.use_symbols.get():
                char_sets.append(string.punctuation)
            
            if not char_sets:
                raise ValueError("At least one character type must be selected.")
            
            all_chars = ''.join(char_sets)
            password = ''.join(random.choice(all_chars) for _ in range(length))
            
            for char_set in char_sets:
                if not set(password).intersection(set(char_set)):
                    replace_index = random.randint(0, length - 1)
                    password = password[:replace_index] + random.choice(char_set) + password[replace_index + 1:]
            
            self.password_var.set(password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()