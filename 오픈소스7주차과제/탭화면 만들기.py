from tkinter import *
from tkinter import ttk

window = Tk()
window.iconbitmap('python.ico')            ##2021041022 박범준

baseTab = ttk.Notebook(window)

tabDog = ttk.Frame(baseTab)
baseTab.add(tabDog, text='강아지')
tabCat = ttk.Frame(baseTab)
baseTab.add(tabCat, text='고양이')

baseTab.pack(expand=1, fill="both")

photoDog = PhotoImage(file="gifdog.gif")
labelDog = Label(tabDog, image=photoDog)
labelDog.pack()

photoCat = PhotoImage(file="gifcat.gif")
labelCat = Label(tabCat, image=photoCat)
labelCat.pack()
window.mainloop()
