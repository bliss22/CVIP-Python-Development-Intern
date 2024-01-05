import tkinter as tk
import random
import time

def start_typing_test():
    words = ["python", "java", "programming", "code", "developer", "tkinter", "application", "speed", "typing", "test","apple","mango","delusion","dart","flutter"]

    def display_new_word():
        random_word = random.choice(words)
        word_label.config(text=random_word)
        entry.delete(0, tk.END)
        entry.focus()

    def calculate_speed():
        end_time = time.time()
        typed_text = entry.get()
        typed_words = typed_text.split()
        correct_words = [w for w in typed_words if w == word_label.cget("text")]
        accuracy = len(correct_words) / len(typed_words) * 100 if len(typed_words) > 0 else 0
        elapsed_time = end_time - start_time
        speed = len(correct_words) / elapsed_time * 60 if elapsed_time > 0 else 0

        result_label.config(text=f"Speed: {speed:.2f} WPM | Accuracy: {accuracy:.2f}%")

    start_time = time.time()

    # GUI setup
    root = tk.Tk()
    root.title("Typing Speed Tester")

    word_label = tk.Label(root, text="", font=("Helvetica", 20))
    word_label.pack(pady=20)

    entry = tk.Entry(root, font=("Helvetica", 16))
    entry.pack(pady=10)
    entry.bind("<Return>", lambda event: calculate_speed())

    result_label = tk.Label(root, text="", font=("Helvetica", 16))
    result_label.pack(pady=20)

    start_button = tk.Button(root, text="Start Test", command=display_new_word, font=("Helvetica", 14))
    start_button.pack(pady=10)

    root.mainloop()

start_typing_test()
