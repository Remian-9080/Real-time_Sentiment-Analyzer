import tkinter as tk
from analyzer import SentimentAnalyzer  # Make sure analyzer.py exists and returns scores between -1 and 1


class SentimentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sentiment Visualizer")
        self.root.configure(bg="black")
        self.root.geometry("400x350")  # Adjusted window size

        self.analyzer = SentimentAnalyzer()

        # Instruction label
        self.label = tk.Label(
            root,
            text="Type your text:",
            fg="white",
            bg="black",
            font=("Arial", 12)
        )
        self.label.pack(pady=(20, 5))

        # Text input field
        self.text_input = tk.Entry(
            root,
            width=40,
            font=("Arial", 12),
            justify="center"
        )
        self.text_input.pack(pady=(0, 20))
        self.text_input.bind("<KeyRelease>", self.analyze_sentiment)

        # Emoji label
        self.emoji_label = tk.Label(
            root,
            text="😐",
            font=("Segoe UI Emoji", 70),
            bg="black",
            fg="#FFD700"  # Yellowish tone
        )
        self.emoji_label.pack(pady=10)

        # Bar canvas background and bar
        self.bar_canvas = tk.Canvas(root, width=300, height=25, bg="#333333", highlightthickness=0)
        self.bar_canvas.pack(pady=10)
        self.bar_rect = self.bar_canvas.create_rectangle(0, 0, 150, 25, fill="gray", outline="")

    def analyze_sentiment(self, event=None):
        text = self.text_input.get().strip()
        if not text:
            self.reset_display()
            return

        score = self.analyzer.analyze(text)  # Returns float between -1 and 1

        # Emoji and color mapping
        if score > 0.4:
            emoji = "😊"
            color = "lime green"
        elif score < -0.4:
            emoji = "😠"
            color = "red"
        else:
            emoji = "😐"
            color = "gold"

        self.emoji_label.config(text=emoji, fg="#FFD700")

        # Update sentiment bar: map score -1 → 0, 0 → 150, +1 → 300
        bar_width = int((score + 1) / 2 * 300)
        self.bar_canvas.coords(self.bar_rect, 0, 0, bar_width, 25)
        self.bar_canvas.itemconfig(self.bar_rect, fill=color)

    def reset_display(self):
        self.emoji_label.config(text="😐", fg="#FFD700")
        self.bar_canvas.coords(self.bar_rect, 0, 0, 150, 25)
        self.bar_canvas.itemconfig(self.bar_rect, fill="gray")


if __name__ == "__main__":
    root = tk.Tk()
    app = SentimentApp(root)
    root.mainloop()
