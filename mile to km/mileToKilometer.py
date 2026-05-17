from tkinter import * 

window = Tk()
window.title("My first GUI program")

window.minsize(width=50, height=30)
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(entry.get()) 
    kilometer = miles * 1.60934
    labelkm.config(text=f"{kilometer} km")

#! Entry
entry = Entry(width=30)
entry.grid(column=1, row=0)

#! Labels
mileslabel = Label(text="Miles", font=('Arial',24))
mileslabel.grid(column=2, row=0)

label2 = Label(text="is equal to", font=('Arial',24))
label2.grid(column=0, row=1)

labelkm = Label(text="0 km", font=('Arial',24))
labelkm.grid(column=1, row=1)

#! Button
button1 = Button(text="convert", command=miles_to_km)
button1.grid(column=1, row=2)

window.mainloop()
