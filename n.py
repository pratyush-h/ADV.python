import tkinter as tk
from PIL import Image, ImageTk
import os

class StudentForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Form")
        try:
            if os.path.exists("pixel3.ico"):
                self.root.iconbitmap("pixel3.ico")
        except Exception as e:
            print(f"Warning: Could not set icon: {e}")

        self.root.geometry('500x500+0+0')
        self.root.configure(background="#FF0101")

        # Load image with exception handling
        self.img = None
        try:
            img = Image.open('star.png')
            resize_img = img.resize((100, 70))
            self.img = ImageTk.PhotoImage(resize_img)
        except FileNotFoundError:
            print("Error: star.png not found. Skipping image.")
        except Exception as e:
            print(f"Error loading image: {e}")

        if self.img:
            img_label = tk.Label(self.root, image=self.img)
            img_label.pack(pady=10, padx=20)

        # Text label
        text_label = tk.Label(self.root, text="Spidy Bucks", font=('Arial', 18, 'bold'), bg="#F384D4", fg='white')
        text_label.pack(pady=10, padx=20)

        # Email
        email_label = tk.Label(self.root, text="Email", font=('Arial', 18, 'bold'), bg="#FE9539", fg='white')
        email_label.pack(pady=(20, 5))

        self.email_entry = tk.Entry(self.root, font=('Arial', 18, 'bold'), fg='white', bg='grey')
        self.email_entry.pack(pady=(5, 10))

        # Password
        password_label = tk.Label(self.root, text="Password", font=('Arial', 18, 'bold'), bg="#000000", fg='white')
        password_label.pack(pady=(20, 5))

        self.password_entry = tk.Entry(self.root, font=('Arial', 18, 'bold'), fg='white', bg='grey', show='*')
        self.password_entry.pack(pady=(5, 10))

        # Login button
        login_btn = tk.Button(self.root, text="Login", font=('Arial', 18, 'bold'), bg="#56DFFA", fg='white', command=self.login)
        login_btn.pack(pady=(5, 10))

    def login(self):
        try:
            email = self.email_entry.get().strip()
            password = self.password_entry.get().strip()
            if not email:
                raise ValueError("Email cannot be empty")
            if not password:
                raise ValueError("Password cannot be empty")
            if '@' not in email:
                raise ValueError("Invalid email format")
            # Here you could add actual authentication logic
            print("Login successful!")
        except ValueError as e:
            print(f"Login error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentForm(root)
    root.mainloop()