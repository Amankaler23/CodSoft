import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400")

        self.root.title("Password Generator")
        

        self.user_label = tk.Label(root, text="Username:")
        self.user_label.pack(padx = 10 , pady = 10)

        self.user_entry = tk.Entry(root)
        self.user_entry.pack()

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(padx = 10 , pady =10)

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", bg = "blue" , fg = "white" , width = 50, command=self.generate_password )
        self.generate_button.pack(padx = 10 , pady =20)

        
        self.password_label = tk.Label(root, text="" )
        self.password_label.pack()

        self.reset_button = tk.Button(root, text="Reset",fg = "blue" , width = 8 ,command=self.reset)
        self.reset_button.pack(padx = 10, pady = 10)

        Accept_button = tk.Button(root, text= "accept" , fg = "blue" , width = 8 )
        Accept_button.pack(padx = 20 , pady = 20)

        

    def generate_password(self):
        username = self.user_entry.get()
        password_length = int(self.length_entry.get())
        
        if username and password_length > 0:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(password_length))
            self.password_label.config(text=f"Generated Password for {username}: {password}")
        else:
            self.password_label.config(text="Please provide a valid username and password length.")

    def reset(self):
        self.user_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.password_label.config(text="")
    

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)


    root.mainloop()
