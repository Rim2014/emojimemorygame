import tkinter as tk
import random

dificullty_leveels = {
    "Easy": ["🐶", "😺", "🐭", "🐹"],
    "Medium": [
        "🐶", "😺", "🐭", "🐹"
        "🦊", "🐻", "🐼", "🐸"
    ],
    "Hard": [
        "🐶", "😺", "🐭", "🐹"
        "🦊", "🐻", "🐼", "🐸"
        "🐵", "🦁", "🐯", "🐨"
    ]     
}


class EmojiMemoryGame:

    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Emoji Memory Match")
        self.root.geometry("600x650")

        self.difficulty = tk.StringVar(value="Easy")

        self.create_menu()

    def create_menu(self):

        tk.Label(
            self.root,
            text="🧠 Emoji Memory match",
            font=("Arial", 24)
        ).pack(pady=20)
        
        tk.Label(self.root,
                 )
