import tkinter as tk

window = tk.Tk()
window.config(background="azure4")
window.title("Kotta-Coffee")
window.geometry("{}x{}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))


def new_pencere(button_text):
    # new_window = tk.Toplevel(window)
    # new_window.geometry("600x825+{}+{}".format(window.winfo_screenwidth() - 700, window.winfo_screenheight() - 950))
    # new_window.config(pady=50,background="aquamarine3")
    # new_window.title(button_text)

    receipt_label = tk.Label(window, text=button_text, background="aquamarine3", width=70, height=50, anchor="n")
    receipt_label.place(x=1200, y=100)


def button_click(button_text):
    return lambda: new_pencere(button_text)


masa_positions = [(50, 250), (350, 250), (650, 250), (50, 550), (350, 550), (650, 550)]
masa_names = ["MASA-1", "MASA-2", "MASA-3", "MASA-4", "MASA-5", "MASA-6"]

for i in range(6):
    button = tk.Button(window, text=masa_names[i], command=button_click(masa_names[i]),
                       background="aquamarine3", borderwidth=0, width=30, height=15)
    button.pack()
    button.place(x=masa_positions[i][0], y=masa_positions[i][1])

window.mainloop()
