# 🔐 Caesar Cipher Tool

A beginner-friendly Python application that provides both **CLI** and **GUI** (Tkinter) interfaces for encrypting and decrypting text using the classic Caesar cipher. This tool demonstrates substitution-based encryption with customizable shift values, input validation, and a clean user experience—ideal for students, educators, and developers learning foundational cryptography and Python GUI programming.

---

## ✅ Features

| Feature | Description |
|--------:|-------------|
🔑 **Encryption / Decryption** | Shift-based substitution cipher (case-preserving A–Z / a–z)  
🖥️ **Dual Interfaces** | Command-line menu and Tkinter graphical UI  
🎯 **Beginner Friendly** | Clear prompts, validation, and helpful messages  
⚙️ **Input Validation** | Handles non-alpha characters and invalid shift values  
📚 **Educational** | Illustrates core cryptography logic and modular code  
🔄 **Bidirectional** | Easy encrypt and decrypt workflows with the same algorithm  

---

## 🧠 How It Works

This project implements the Caesar cipher by:

- Reading user input (message + numeric shift)  
- Preserving letter case and non-letter characters  
- Shifting letters by the provided offset (wrap-around A↔Z)  
- Supporting both encryption and decryption (inverse shift)  
- Providing two interfaces: a CLI menu and a Tkinter GUI

---

## 🛠 Tech Stack

| Tool / Library | Purpose |
|----------------|---------|
Python 3 | Core application logic and CLI  
Tkinter | Desktop GUI interface  
Standard library | Input handling, string processing  

---

## 📦 Requirements

- **Python 3.8+** (or any modern 3.x)  
- **Tkinter** (usually included with standard Python distributions)  
- Cross-platform (Windows / macOS / Linux) — CLI works everywhere; GUI requires Tkinter

---

## ⬇️ Sample CLI Menu
=== Caesar Cipher Tool ===

Encrypt a message

Decrypt a message

Exit

---

## 📊 Example Output (CLI)
Enter choice: 1

Enter message to encrypt: Hello, World!

Enter shift value (1-25): 3

Encrypted message: Khoor, Zruog!


Enter choice: 2

Enter message to decrypt: Khoor, Zruog!

Enter shift value (1-25): 3

Decrypted message: Hello, World!

---

## 🏆 Achievements

✅ Demonstrates classical cipher implementation clearly  
✅ Supports both CLI and GUI usage patterns  
✅ Robust handling of non-alphabetic characters  
✅ Educational: great for classroom demos and tutorials  
✅ Clean, modular code suited for extension (brute-force, files)

---

## ⚠️ Legal & Ethical Use

This is an educational cryptography demonstration and **not** intended for securing sensitive production data. Use responsibly:

✅ For learning and classroom exercises  
✅ For practice encoding/decoding messages locally  

❌ Do NOT use this as a substitute for modern cryptographic standards (e.g., AES) for protecting real sensitive information.

---
