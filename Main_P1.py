from tkinter import*
from tkinter import ttk as k
from tool_P1 import*

townZip = {"Borongan":"1600", "Sulat":"1618", "San Julian":"1900"}
def Submit():
    age = Calcu_Age(entryBD)
    Zipcode = townZip.get(cbxTown.get(), "Unknown")
    if not all([entryName.get(), entryBD.get(), entryPN.get()]):
        messagebox.showerror("Error", "Please fill up all fields.")
        return
    if age is None: return
    messagebox.showinfo("Information Details", f"""
    Name:  {entryName.get()}
    Birthday:  {entryBD.get()}
    Age:  {age}
    Sex:  {cbxSex.get()}
    Civil Status:  {cbxCS.get()}
    Town:  {cbxTown.get()} (Zip Code: {Zipcode})
    Scholar Status:  {SS_var.get()}
    Phone Number:  {entryPN.get()}
    """)

root = Tk()
x, y = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"650x400+{(x//2)-(650//2)}+{(y//2)-(400//2)}")

Label(root, text="Name:", font="Arial 12").place(x=20, y=30)
entryName = Entry(root, font="Arial 12")
entryName.place(x=20, y=55)

Label(root, text="Birthday (YYYY-MM-DD):", font="Arial 12").place(x=20, y=100)
entryBD = Entry(root, font="Arial 12")
entryBD.place(x=20, y=130)

Label(root, text="Phone Number:", font="Arial 12").place(x=20, y=170)
entryPN = Entry(root, font="Arial 12", validate="key", validatecommand=(root.register(Valid_Input), "%S", "%P"))
entryPN.place(x=20, y=190)

Label(root, text="Sex:", font="Arial 12").place(x=300, y=30)
cbxSex = k.Combobox(root, font="Arial 12", values=["Male", "Female", "Other"])
cbxSex.set("Male")
cbxSex.place(x=300, y=55)

Label(root, text="Civil Status:", font="Arial 12").place(x=300, y=100)
cbxCS = k.Combobox(root, font="Arial 12", values=["Single", "Married", "Divorced", "Widowed"])
cbxCS.set("Single")
cbxCS.place(x=300, y=130)

Label(root, text="Town:", font="Arial 12").place(x=300, y=170)
cbxTown = k.Combobox(root, font="Arial 12", values=list(townZip.keys()))
cbxTown.set("Borongan")
cbxTown.place(x=300, y=190)
cbxTown.bind("<<ComboboxSelected>>", lambda event: Update_Zip(cbxTown, townZip, lblZip))
lblZip = Label(root, text="Zip Code: 1600")
lblZip.place(x=510, y=190)

Label(root, text="Scholar Status:", font="Arial 12").place(x=300, y=240)
SS_var = StringVar(value="No")
rdY = k.Radiobutton(root, text="Yes", variable=SS_var, value="Yes")
rdY.place(x=480, y=240)
rdN = k.Radiobutton(root, text="No", variable=SS_var, value="No")
rdN.place(x=520, y=240)

Button(root, text="Submit", font="Arial 12", command=Submit).pack(pady=(340,0))
root.after(100, entryName.focus_set())
root.mainloop()