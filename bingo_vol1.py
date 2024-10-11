import tkinter as tk
import random

class BingoSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("ビンゴ司会システム Ver.1")
        self.numbers = list(range(1, 76))  
        self.selected_numbers = []  
        self.label = tk.Label(root, text="ビンゴゲームを開始します", font=("Arial", 24))
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="数字を引く", command=self.pick_number, font=("Arial", 16))
        self.button.pack(pady=20)

        self.history_label = tk.Label(root, text="履歴: ", font=("Arial", 14))
        self.history_label.pack(pady=20)

    def pick_number(self):
        if len(self.numbers) > 0:
            selected = random.choice(self.numbers)  
            self.numbers.remove(selected)  
            self.selected_numbers.append(selected)  
            self.label.config(text=f"次の数字: {selected}")  

            history_text = "履歴: " + ", ".join(map(str, self.selected_numbers))
            self.history_label.config(text=history_text)
        else:
            self.label.config(text="全ての数字が引かれました")

if __name__ == "__main__":
    root = tk.Tk()
    app = BingoSystem(root)
    root.mainloop()
