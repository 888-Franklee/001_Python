import tkinter as tk

class SimpleTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Timer")
        self.elapsed_time = 0
        self.running = False

        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT)

    def format_time(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hours:02}:{minutes:02}:{secs:02}"

    def update_timer(self):
        if self.running:
            self.elapsed_time += 1
            self.time_label.config(text=self.format_time(self.elapsed_time))
            self.root.after(1000, self.update_timer)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text=self.format_time(self.elapsed_time))

if __name__ == "__main__":
    root = tk.Tk()
    timer = SimpleTimer(root)
    root.mainloop()