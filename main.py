import tkinter as tk
from tkinter import messagebox
from plyer import notification
import time

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x200")
        
        self.timer_label = tk.Label(root, text="00:00", font=("Helvetica", 32))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=20)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.RIGHT, padx=10, pady=20)

        self.running = False
        self.time_left = 25 * 60  # 25 minutes in seconds

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def reset_timer(self):
        self.running = False
        self.time_left = 25 * 60
        self.timer_label.config(text="25:00")

    def update_timer(self):
        if self.running:
            mins, secs = divmod(self.time_left, 60)
            self.timer_label.config(text=f"{mins:02}:{secs:02}")
            if self.time_left > 0:
                self.time_left -= 1
                self.root.after(1000, self.update_timer)
            else:
                self.running = False
                self.notify()

    def notify(self):
        notification.notify(
            title="Time's Up!",
            message="Take a break or start your next session.",
            timeout=5
        )
        messagebox.showinfo("Pomodoro Timer", "Time's up! Take a break.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
