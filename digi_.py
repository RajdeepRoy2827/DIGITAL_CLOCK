import tkinter as tk
from time import strftime

# create the main window
root = tk.Tk()
root.title("My Advanced Digital Clock")

# set window size
root.geometry("700x200")

# function to update time and date
def time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%A, %d %B %Y')
    label_time.config(text=current_time)
    label_date.config(text=current_date)
    label_time.after(1000, time)

# create a frame for the clock with gradient-like background
top_frame = tk.Frame(root, bg="#0D47A1")
top_frame.pack(fill="both", expand=True)

# create a label to display the time
label_time = tk.Label(
    top_frame,
    font=("Helvetica", 80, "bold"),
    background="#0D47A1",
    foreground="white"
)
label_time.pack(anchor="center", pady=10)

# create a label to display the day and date
label_date = tk.Label(
    top_frame,
    font=("Helvetica", 30, "bold"),
    background="#0D47A1",
    foreground="white"
)
label_date.pack(anchor="center")

# initialize the time function 
time()

# run the application
root.mainloop()
