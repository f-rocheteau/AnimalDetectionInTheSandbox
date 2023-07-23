import os
import tkinter as tk
from tkinter import messagebox
from threading import Thread

# Function to start the command
def start_command():
    # Replace 'your_command_here' with the actual command you want to run
    command = 'python detect.py --source screen'
    os.system(command)

# Function to stop the command
def stop_command():
    # Replace 'your_command_name' with the name of the process you want to stop
    command_name = 'python'
    os.system(f'taskkill /F /IM {command_name}.exe')

# Create the GUI
app = tk.Tk()
app.title("Start/Stop Application")
app.geometry("300x150")

# Start button
start_button = tk.Button(app, text="Start", command=lambda: Thread(target=start_command).start())
start_button.pack(pady=20)

# Stop button
stop_button = tk.Button(app, text="Stop", command=stop_command)
stop_button.pack(pady=5)

# Run the application
app.mainloop()