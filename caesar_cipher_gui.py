import tkinter as tk
from tkinter import messagebox

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher Tool")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f0f0')
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="Caesar Cipher Tool", 
            font=('Arial', 18, 'bold'),
            bg='#f0f0f0'
        )
        title_label.pack(pady=20)
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Message:", bg='#f0f0f0').grid(row=0, column=0, padx=5, pady=5)
        self.message_entry = tk.Entry(input_frame, width=40)
        self.message_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Shift Value:", bg='#f0f0f0').grid(row=1, column=0, padx=5, pady=5)
        self.shift_entry = tk.Entry(input_frame, width=10)
        self.shift_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        
        # Buttons Frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        self.encrypt_btn = tk.Button(
            button_frame, 
            text="Encrypt", 
            command=self.encrypt,
            bg='#4CAF50',
            fg='white',
            font=('Arial', 12),
            width=10
        )
        self.encrypt_btn.grid(row=0, column=0, padx=10)
        
        self.decrypt_btn = tk.Button(
            button_frame, 
            text="Decrypt", 
            command=self.decrypt,
            bg='#2196F3',
            fg='white',
            font=('Arial', 12),
            width=10
        )
        self.decrypt_btn.grid(row=0, column=1, padx=10)
        
        # Result Frame
        result_frame = tk.Frame(self.root, bg='#f0f0f0')
        result_frame.pack(pady=10)
        
        tk.Label(result_frame, text="Result:", bg='#f0f0f0', font=('Arial', 12, 'bold')).pack()
        self.result_text = tk.Text(result_frame, height=4, width=50, font=('Arial', 10))
        self.result_text.pack(pady=5)
    
    def caesar_cipher(self, text, shift, mode):
        """Encrypt or decrypt text using Caesar Cipher"""
        result = ""
        
        if mode == 'decrypt':
            shift = -shift
        
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted_char = chr((ord(char) - base + shift) % 26 + base)
                result += shifted_char
            else:
                result += char
        
        return result
    
    def encrypt(self):
        """Handle encryption"""
        try:
            message = self.message_entry.get()
            shift = int(self.shift_entry.get())
            
            if not message:
                messagebox.showwarning("Input Error", "Please enter a message")
                return
            
            encrypted = self.caesar_cipher(message, shift, 'encrypt')
            self.display_result(f"Encrypted message:\n{encrypted}")
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid shift number")
    
    def decrypt(self):
        """Handle decryption"""
        try:
            message = self.message_entry.get()
            shift = int(self.shift_entry.get())
            
            if not message:
                messagebox.showwarning("Input Error", "Please enter a message")
                return
            
            decrypted = self.caesar_cipher(message, shift, 'decrypt')
            self.display_result(f"Decrypted message:\n{decrypted}")
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid shift number")
    
    def display_result(self, text):
        """Display result in the text widget"""
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, text)

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
