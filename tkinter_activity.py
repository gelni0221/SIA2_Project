from tkinter import *
from tkinter.ttk import Combobox
def compute():
    try:
        passed = 0
        failed = 0
        english = float(englishgrade.get())
        math = float(mathgrade.get())
        science = float(sciencegrade.get())
        filipino = float(filipinograde.get())
        mapeh = float(mapehgrade.get())

        if english > 100:
            errorlabel.config(text="English grade should not exceed 100!")
            errorlabel.grid(column=1, row=10, padx=5, pady=5)
            return

        if math > 100:
            errorlabel.config(text="Math grade should not exceed 100!")
            errorlabel.grid(column=1, row=10, padx=5, pady=5)
            return

        if science > 100:
            errorlabel.config(text="Science grade should not exceed 100!")
            errorlabel.grid(column=1, row=10, padx=5, pady=5)
            return

        if filipino > 100:
            errorlabel.config(text="Filipino grade should not exceed 100!")
            errorlabel.grid(column=1, row=10, padx=5, pady=5)
            return

        if mapeh > 100:
            errorlabel.config(text="MAPEH grade should not exceed 100!")
            errorlabel.grid(column=1, row=10, padx=5, pady=5)
            return

        average = ((english + math + science + filipino + mapeh) / 5)
        averagecomputation.config(text=f"{average:.2f}")

        if 90 <= average <= 100:
            descriptorcomputation.config(text=f"Outstanding")
        elif 85 <= average <= 89:
            descriptorcomputation.config(text=f"Very Satisfactory")
        elif 80 <= average <= 84:
            descriptorcomputation.config(text=f"Satisfactory")
        elif 75 <= average <= 79:
            descriptorcomputation.config(text=f"Fairly Satisfactory")
        else:
            descriptorcomputation.config(text=f"Did not Meet Expectation")

        if 75 <= average <= 100:
            remarkscomputation.config(text="Passed")
        else:
            remarkscomputation.config(text="Failed")

        if 75 <= english <= 100:
            passed += 1
        else:
            failed += 1
        if 75 <= math <= 100:
            passed += 1
        else:
            failed += 1
        if 75 <= science <= 100:
            passed += 1
        else:
            failed += 1
        if 75 <= filipino <= 100:
            passed += 1
        else:
            failed += 1
        if 75 <= mapeh <= 100:
            passed += 1
        else:
            failed += 1
        subjectscomputation.config(text=f"Passed: {passed} | Failed: {failed}")

    except ValueError:
        errorlabel.config(text="Invalid Input!")
        errorlabel.grid(column=1, row=10,padx=5,pady=5)
def clear():
    # Clear all input fields
    englishgrade.delete(0, END)
    mathgrade.delete(0, END)
    sciencegrade.delete(0, END)
    filipinograde.delete(0, END)
    mapehgrade.delete(0, END)

    # Clear the result labels
    averagecomputation.config(text="")
    descriptorcomputation.config(text="")
    remarkscomputation.config(text="")
    subjectscomputation.config(text="")
    errorlabel.config(text="")
    errorlabel.grid_forget()

window = Tk()
window.title("GUI Average Program")
window.minsize(width=500,height=500)
window.config(padx=25,pady=25)

englishlabel = Label(text="English")
englishlabel.grid(column=0,row=0, padx=5,pady=5)
englishgrade = Entry(width=5)
englishgrade.grid(column=1,row=0)

mathlabel = Label(text="Math")
mathlabel.grid(column=0, row=1, padx=5,pady=5)
mathgrade = Entry(width=5)
mathgrade.grid(column=1, row=1)

sciencelabel = Label(text="Science")
sciencelabel.grid(column=0, row=2, padx=5,pady=5)
sciencegrade = Entry(width=5)
sciencegrade.grid(column=1, row=2)

filipinolabel = Label(text="Filipino")
filipinolabel.grid(column=0, row=3, padx=5,pady=5)
filipinograde = Entry(width=5)
filipinograde.grid(column=1, row=3)

mapehlabel = Label(text="MAPEH")
mapehlabel.grid(column=0, row=4, padx=5,pady=5)
mapehgrade = Entry(width=5)
mapehgrade.grid(column=1, row=4)


computeaverage = Button(text="Compute", command= compute)
clearbutton = Button(text="Clear", command=clear)


averagelabel = Label(text="Average:")
averagelabel.grid(column=0, row=5,padx=5,pady=5)

remarkslabel = Label(text="Remarks:")
remarkslabel.grid(column=0, row=6,padx=5,pady=5)

descriptorlabel = Label(text="Descriptor:")
descriptorlabel.grid(column=0, row=7,padx=5,pady=5)

subjectslabel = Label(text="Subjects:")
subjectslabel.grid(column=0, row=8,padx=5,pady=5)

averagecomputation = Label(text="...")
averagecomputation.grid(column=1, row=5,padx=5,pady=5)

remarkscomputation = Label(text="...")
remarkscomputation.grid(column=1, row=6,padx=5,pady=5)

descriptorcomputation = Label(text="...")
descriptorcomputation.grid(column=1, row=7,padx=5,pady=5)

subjectscomputation = Label(text="...")
subjectscomputation.grid(column=1, row=8,padx=5,pady=5)

errorlabel = Label(text="", font=("Arial",10,"bold"))




computeaverage.grid(column=2, row=5,padx=5,pady=5)
clearbutton.grid(column=3, row=5,padx=5,pady=5)











#pack is used to open the widgets or smth in the tk, the same as grid or place, but i can only pick one and stick with it unless it's another frame i can use any
#used to open the tk
window.mainloop()