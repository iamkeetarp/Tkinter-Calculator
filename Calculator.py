# Calculator
from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()
    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()

root.geometry("444x520")
root.title("Calculator")
root.wm_iconbitmap("calculator.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="leucine 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=28, pady=18, font="lucide 15 bold", bg="red")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text="8", padx=28, pady=18, font="lucide 15 bold", bg="red")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text="7", padx=28, pady=18, font="lucide 15 bold", bg="red")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="6", padx=28, pady=18, font="lucide 15 bold", bg="red")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text="5", padx=28, pady=18, font="lucide 15 bold", bg="red")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text="4", padx=28, pady=18, font="lucide 15 bold", bg="red")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="3", padx=28, pady=18, font="lucide 15 bold", bg="red")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text="2", padx=28, pady=18, font="lucide 15 bold", bg="red")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text="1", padx=28, pady=18, font="lucide 15 bold", bg="red")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="0", padx=31, pady=18, font="lucide 15 bold", bg="red")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text="-", padx=28, pady=18, font="lucide 15 bold", bg="blue")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text="*", padx=28, pady=18, font="lucide 15 bold", bg="blue")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="c", padx=26, pady=18, font="lucide 15 bold", bg="white")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text="%", padx=28, pady=18, font="lucide 15 bold", bg="blue")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
b = Button(f, text="=", padx=28, pady=18, font="lucide 15 bold", bg="black",fg="white")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=18, pady=5)
f.pack()

root.mainloop()
