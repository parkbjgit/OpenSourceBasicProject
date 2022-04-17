from tkinter import *
from tkinter.filedialog import *

filename = ""
#함수 선언 부분                                     ##2021041022 박범준
def func_open() :
    filename = askopenfilename(parent = window,
                               filetypes = (("gif파일", "*.gif"),
                               ("모든 파일","*.*")))
    photo = PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image = photo

def func_exit():
        window.quit()
        window.destroy()

def func_zoom(event):
    photo=PhotoImage(file = "gifdog.gif")
    photo=photo.zoom(5, 5)
    pLabel.configure(image=photo)
    pLabel.image=photo
    pLabel.pack(expand=1,anchor = CENTER)

def func_subsample(event):
    photo=PhotoImage(file = "gifdog.gif")
    photo=photo.subsample(2, 2)
    pLabel.configure(image=photo)
    pLabel.image=photo
    pLabel.pack(expand=1, anchor=CENTER)

#메인
window=Tk()
window.geometry("400x400")
window.title("사진 확대축소")

photo=PhotoImage()
pLabel=Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)


mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.bind("<Up>", func_zoom)
window.bind("<Down>", func_subsample)

window.mainloop()