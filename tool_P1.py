from tkinter import messagebox
from datetime import datetime

def Calcu_Age(entryBD):
    try:
        today = datetime.today()
        birthDate = datetime.strptime(entryBD.get(), "%Y-%m-%d")
        age = today.year - birthDate.year - ((today.month, today.day)<(birthDate.month, birthDate.day))
        return age
    except ValueError:
        messagebox.showerror("Input Error", "Invalid date format! Use YYYY-MM-DD")
        return None

def Update_Zip(cbxTown, townZip, lblZip):
    lblZip.config(text=f"Zip code: {townZip.get(cbxTown.get())}")

def Valid_Input(char, value):
    if char == "" or char.isdigit(): return True
    return False