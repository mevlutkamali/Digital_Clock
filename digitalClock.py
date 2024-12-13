
import time
import threading
from cProfile import label
from tkinter import Tk, Label, Button, Entry, messagebox

def digitalClock():
    # Clock.
    timeInfo = time.strftime("%H:%M:%S")
    label.config(text=timeInfo)
    # Date.
    dateInfo =time.strftime("%d / %B / %Y")
    dateLabel.config(text=dateInfo)

    if alarmTime and timeInfo == alarmTime:
        triggerAlarm()

    # Clock update.
    label.after(200, digitalClock)

def triggerAlarm():
    global alarmTriggered

    if not alarmTriggered:
        alarmTriggered = True
        messagebox.showinfo("ALARM", "Alarm Zamanı Geldi")

def digitalAlarm():
    global alarmTime, alarmTriggered

    alarmTime = alarmEntry.get()
    alarmTriggered = False

    if not alarmTime:
        messagebox.showerror("HATA","Lütfen geçerli formatta değer giriniz.")
        return

    try:
        time.strptime(alarmTime, "%H:%M:%S")
        messagebox.showinfo("ALARM KURULDU", f"Alarm Saati : {alarmTime}")

    except ValueError:
        messagebox.showerror("HATA", "Saat formatı geçersiz. Lütfen HH:MM:SS formatında girin.")

alarmTime = None
alarmTriggered = None

appWindow = Tk()
appWindow.title("Dijital Saat")
appWindow.configure(bg="gray")
appWindow.geometry("700x260")
appWindow.resizable(0, 0)

borderWidht = 10
foreground = "white"
background = "gray"
textFont = ("Boulder", 36, "bold")

appWindow.grid_rowconfigure(0, weight=1)
appWindow.grid_rowconfigure(1, weight=1)
appWindow.grid_rowconfigure(2, weight=1)
appWindow.grid_columnconfigure(0, weight=1)
appWindow.grid_columnconfigure(1, weight=1)
appWindow.grid_columnconfigure(2, weight=1)

label = Label(appWindow, bd=borderWidht, fg=foreground, bg=background, font=textFont)
label.grid(row=0, column=1, padx=10, pady=10)

dateLabel = Label(appWindow, bd=borderWidht, fg=foreground, bg=background, font=textFont)
dateLabel.grid(row=1, column=1, padx=10, pady=10)

alarmEntry = Entry(appWindow, bd=borderWidht, fg="black", bg="white", font=("Arial", 14), width=10)
alarmEntry.grid(row=2, column=1, padx=10, pady=10)

alarmButton = Button(appWindow, text="Alarm Kur", command=digitalAlarm, bd=borderWidht, fg=foreground, bg=background, font=("Arial", 14))
alarmButton.grid(row=2, column=2, padx=10, pady=10)

digitalClock()
appWindow.mainloop()

print("Finish")
