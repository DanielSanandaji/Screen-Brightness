# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import wmi
import screen_brightness_control as sbc
import tkinter as tk
from tkinter import Scale

current = sbc.get_brightness()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Funktion som körs när värdet ändras
def update_value(value):
    sbc.set_brightness(value)
    value_label.config(text=f"Nytt värde: {value}")

    brightness = sbc.set_brightness(value)



# Skapa huvudfönstret
root = tk.Tk()
root.title("Justera ljusstyrka")

# Skapa en slider för värdejustering
value_scale = Scale(root, from_=1, to=100, orient="horizontal", label="Värde")
value_scale.pack(padx=200, pady=100)
value_scale.bind("<ButtonRelease-1>", lambda event: update_value(value_scale.get()))
print(value_scale.get())

# Skapa en etikett för att visa det nya värdet
value_label = tk.Label(root, text="Nytt värde: 1")
value_label.pack(pady=5)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    brightness = sbc.set_brightness(100)
    root.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
