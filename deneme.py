import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.config(background="azure4")
window.title("Kotta-Coffee")
window.geometry("{}x{}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))


# Load the image

def new_pencere(button_text):
    receipt_label = tk.Label(window, text=button_text, background="aquamarine3", width=70, height=50, anchor="n")
    receipt_label.place(x=1200, y=100)
    urun_button = tk.Button(window, text="ürün ekle", background="aquamarine3", width=12, height=4)
    urun_button.pack()
    urun_button.place(x=window.winfo_screenwidth() - 2230, y=200)
    urun_sil = tk.Button(window, text="ürün sil", background="aquamarine3", width=12, height=4)
    urun_sil.pack()
    urun_sil.place(x=window.winfo_screenwidth() - 2230, y=300)
    hesap_al_button = tk.Button(window, text="Hesap Al", command=lambda: show_payment_options(button_text),
                                background="aquamarine3", width=12, height=4)
    hesap_al_button.pack()
    hesap_al_button.place(x=window.winfo_screenwidth() - 2630, y=850)


def show_payment_options(button_text):
    global kredi_karti_button, nakit_button
    nakit_image = Image.open("para.png")
    resized_image1 = nakit_image.resize((120, 85))
    image_nakit = ImageTk.PhotoImage(resized_image1)
    nakit_button = tk.Button(window, image=image_nakit,

                             command=lambda: hesap_ode(button_text, "Kredi Kartı"),
                             background="aquamarine3", width=120, height=75)
    nakit_button.image = image_nakit
    nakit_button.pack()
    nakit_button.place(x=window.winfo_screenwidth() - 2500, y=850)

    # Load and resize the image
    original_image = Image.open("kredi.png")
    resized_image = original_image.resize((120, 50))
    image_kredi = ImageTk.PhotoImage(resized_image)

    kredi_karti_button = tk.Button(window, image=image_kredi,

                                   command=lambda: hesap_ode(button_text, "Kredi Kartı"),
                                   background="aquamarine3", width=120, height=75)
    kredi_karti_button.image = image_kredi
    kredi_karti_button.pack()
    kredi_karti_button.place(x=window.winfo_screenwidth() - 2370, y=850)


def hesap_ode(button_text, payment_method):
    kredi_karti_button.destroy()
    nakit_button.destroy()


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
