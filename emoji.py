import tkinter as tk
import random

dificullty_levels = {
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
                text="Choose difficulty",
                font=("Arial", 16)
        ).pack()

        for level in difficulty_levels:
            tk.Radiobutton(
                self.root,
                text=level,
                variable=self.difficulty,
                value=level,
                font=("Arial", 14)
            ).pack()

        tk.button(
            self.root,
            text="🚀 Start game",
            font=("Arial", 16),
            command=self.start_game
        ).pack(pady=20)


    def start_game (self):

        for widget in self.root.winfo_children():
            widget.destroy()

        self.moves = 0
        self.matches = 0
        self.open_cards = []

        emojis = difficulty_levels[self.difficulty.get()]

        self.cards =  emojis * 2
        random.shuffle(self.cards)

        self.info = tk.Label 

        #----------------#



            #--------------#




        self.buttons[a]["text"]="?"
        self.buttons[b]["text"]="?"
        
        self.message.config(text="❌ try again")
        
        self.open_cards=[]

        self.update_info()

        if self.matches==len(self.cards)//2:

            self