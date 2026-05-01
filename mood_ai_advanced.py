import tkinter as tk
from textblob import TextBlob
import random

# Suggestions
positive_tips = [
    "Keep smiling 😊",
    "Share your happiness with others 🎉",
    "Do something creative 🎨"
]

negative_tips = [
    "Take a deep breath 🌿",
    "Talk to a friend 📞",
    "Listen to calming music 🎧"
]

neutral_tips = [
    "Stay balanced ⚖️",
    "Take a short break ☕",
    "Go for a walk 🚶"
]

history = []

# Function
def detect_mood():
    text = entry.get()
    if text == "":
        result.set("⚠️ Please enter some text")
        return

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        mood = "😊 Positive"
        tip = random.choice(positive_tips)
    elif polarity < 0:
        mood = "😔 Negative"
        tip = random.choice(negative_tips)
    else:
        mood = "😐 Neutral"
        tip = random.choice(neutral_tips)

    output = f"Mood: {mood}\nPolarity Score: {round(polarity,2)}\nTip: {tip}"
    result.set(output)

    # Save history
    history.append(output)

# Clear function
def clear_text():
    entry.delete(0, tk.END)
    result.set("")

# Show history
def show_history():
    history_text = "\n\n".join(history[-5:])  # last 5 entries
    result.set(history_text if history else "No history yet")

# GUI Window
window = tk.Tk()
window.title("MoodMate AI (Advanced)")
window.geometry("450x400")
window.configure(bg="#1e1e2f")

# Title
tk.Label(window, text="MoodMate AI", font=("Arial", 18, "bold"), fg="white", bg="#1e1e2f").pack(pady=10)

# Entry
entry = tk.Entry(window, width=40, font=("Arial", 12))
entry.pack(pady=10)

# Buttons Frame
frame = tk.Frame(window, bg="#1e1e2f")
frame.pack(pady=10)

tk.Button(frame, text="Detect Mood", command=detect_mood, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(frame, text="Clear", command=clear_text, bg="#f44336", fg="white").grid(row=0, column=1, padx=5)
tk.Button(frame, text="History", command=show_history, bg="#2196F3", fg="white").grid(row=0, column=2, padx=5)

# Output
result = tk.StringVar()
tk.Label(window, textvariable=result, wraplength=350, fg="white", bg="#1e1e2f", font=("Arial", 11)).pack(pady=20)

# Run
window.mainloop()