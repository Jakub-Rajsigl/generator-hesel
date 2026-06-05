import customtkinter as ctk
import random
import string

def generuj():
    znaky = string.ascii_letters + string.digits + "!?@#$*"
    heslo = "".join(random.choice(znaky) for _ in range(12))
    vysledek_label.configure(text=heslo)
    kopirovat_tlacitko.configure(text="Kopírovat heslo", fg_color=["#3B8ED0", "#1F6AA5"])

def kopiruj():
    heslo = vysledek_label.cget("text")
    if heslo != "----":
        app.clipboard_clear()
        app.clipboard_append(heslo)
        kopirovat_tlacitko.configure(text="Zkopírováno", fg_color="green")

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Generátor náhodného Hesla")
app.geometry("400x350") 

nadpis = ctk.CTkLabel(app, text="Generátor Hesla", font=("Arial", 20, "bold"))
nadpis.pack(pady=20)

vysledek_label = ctk.CTkLabel(app, text="----", font=("Consolas", 18))
vysledek_label.pack(pady=10)

tlacitko = ctk.CTkButton(app, text="Vytvořit nové heslo", command=generuj)
tlacitko.pack(pady=15)

kopirovat_tlacitko = ctk.CTkButton(app, text="Kopírovat heslo", command=kopiruj)
kopirovat_tlacitko.pack(pady=5)

app.mainloop()