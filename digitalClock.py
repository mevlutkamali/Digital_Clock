
import time
from tkinter import Label, Tk, Button

current_format = "24"

app_window = Tk()
app_window.title("Digital Clock")
app_window.configure(bg="gray")
app_window.geometry("300x150")
app_window.resizable(0, 0)

background = "gray"
foreground = "white"
text_font = ("Boulder", 18, 'bold')
border_widht = 20

clock_label = Label(app_window, font=text_font, bg=background, fg=foreground)
clock_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

date_label = Label(app_window, font=text_font, bg=background, fg=foreground)
date_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

def timeClock():
    global current_format
    if current_format == "24":
        time_clock = time.strftime("%H:%M:%S")
    else:
        time_clock = time.strftime("%I:%M:%S %p")
    clock_label.config(text=time_clock)

    dateInfo = time.strftime("%d %B %Y")
    date_label.config(text=dateInfo)

    clock_label.after(1000, timeClock)

def timeMode():
    time_mode = int(time.strftime("%H"))

    if time_mode >= 18 or time_mode < 6:
        app_window.configure(bg="black")
        clock_label.config(bg="black", fg="white")
        date_label.config(bg="black", fg="white")
    else:
        app_window.configure(bg="white")
        clock_label.config(bg="white", fg="black")
        date_label.config(bg="white", fg="black")

    clock_label.after(1000, timeMode)

def toogleFormat():
    global current_format

    if current_format == "24":
        current_format = "12"
    else:
        current_format = "24"

    timeClock()

format_button = Button(app_window, text="Toggle Format", command=toogleFormat, font=("Arial", 12))
format_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

app_window.grid_rowconfigure(0, weight=1)
app_window.grid_rowconfigure(1, weight=1)
app_window.grid_rowconfigure(2, weight=1)

app_window.grid_columnconfigure(0, weight=1)
app_window.grid_columnconfigure(1, weight=1)
app_window.grid_columnconfigure(2, weight=1)

timeClock()
timeMode()

app_window.mainloop()
