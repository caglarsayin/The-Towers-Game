# To change this template, choose Tools | Templates
# and open the template in the editor.

from Tkinter import *
import Classes
import tkFileDialog
import tkMessageBox
#import random

__author__="caglar"
__date__ ="$Nov 20, 2010 9:19:39 PM$"
puzzle=Classes.Puzzle()
T=list()

def Load():
    PuzzleDestroyer()
    opened=tkFileDialog.askopenfile()
    puzzle.size=int(opened.read(1))
    print puzzle.size
    if(opened):
        opened.read(1)
        for i in range(puzzle.size):
            puzzle.hint.hintsup.append(opened.read(1))
        opened.read(1)
        for i in range(puzzle.size):
            puzzle.hint.hintsdown.append(opened.read(1))
        opened.read(1)
        for i in range(puzzle.size):
            puzzle.hint.hintsright.append(opened.read(1))
        opened.read(1)
        for i in range(puzzle.size):
            puzzle.hint.hintsleft.append(opened.read(1))
        for i in range(puzzle.size):
            puzzle.boxes.append(list())
            for j in range(puzzle.size):
                puzzle.boxes[i].append(Classes.Box())
        PuzzleMaker()

def Save():
    savefile=tkFileDialog.asksaveasfile()
    if(savefile):
        savefile.write(str(puzzle.size))
        savefile.write("\n")
        for i in range(puzzle.size):
            savefile.write(str(puzzle.hint.hintsup[i]))
        savefile.write("\n")
        for i in range(puzzle.size):
            savefile.write(str(puzzle.hint.hintsdown[i]))
        savefile.write("\n")
        for i in range(puzzle.size):
            savefile.write(str(puzzle.hint.hintsright[i]))
        savefile.write("\n")
        for i in range(puzzle.size):
            savefile.write(str(puzzle.hint.hintsleft[i]))

def Solvef():
    result=puzzle.solver()
    if(result==1):
        for i in range(puzzle.size*puzzle.size):
                puzzle.boxes[i/puzzle.size][i%puzzle.size].entry.set(str(puzzle.boxes[i/puzzle.size][i%puzzle.size].value))
                T[i].config(foreground='red')
    else:
        tkMessageBox.showwarning('Wrong puzzle!','it is a kind of wrong puzzle')
def Clearf():

    for i in range(puzzle.size*puzzle.size):
        puzzle.boxes[i/puzzle.size][i%puzzle.size].entry.set("")


def Checkf():
    for i in range(puzzle.size):
        for j in range(puzzle.size):
            puzzle.boxes[i][j].value=puzzle.boxes[i][j].entry.get()

    result=puzzle.checker()
    if(result==0):
        tkMessageBox.showinfo("Wrong Answer"," It is wrong try it again")
    else:
        tkMessageBox.showinfo("Right Answer","Congratulation")
        Generate()


def GenerateDo2():
    huplabel=list()
    hdownlabel=list()
    hleftlabel=list()
    hrightlabel=list()
    huplabelv=list()
    hdownlabelv=list()
    hleftlabelv=list()
    hrightlabelv=list()
    def Manhinter():
        for i in range(puzzle.size):
            puzzle.boxes.append(list())
            for j in range(puzzle.size):
                puzzle.boxes[i].append(Classes.Box())
                puzzle.boxes[i][j].value=((puzzle.size+i+j)%puzzle.size)+1
            puzzle.hint.hintsup.append(huplabelv[i].get())
            puzzle.hint.hintsdown.append(hdownlabelv[i].get())
            puzzle.hint.hintsleft.append(hleftlabelv[i].get())
            puzzle.hint.hintsright.append(hrightlabelv[i].get())
        window2.destroy()
        PuzzleMaker()
    window2=Toplevel()
    window2.title("Give The Hints")
    framehints=Frame(window2, borderwidth=1, relief=RAISED)
    for i in range(puzzle.size):
        huplabelv.append(IntVar())
        huplabel.append(Entry(framehints,width=2, font=("asdsas",30, ),justify=CENTER,textvariable=huplabelv[i]))
        huplabel[i].grid(row=0, column=i+1)
        huplabel[i].bind('<KeyRelease>',SizeCont)
        huplabel[i].bind('<Key>',LimitBox)
        hdownlabelv.append(IntVar())
        hdownlabel.append(Entry(framehints,width=2, font=("asdsas",30, ),justify=CENTER,textvariable=hdownlabelv[i]))
        hdownlabel[i].grid(row=(puzzle.size+1), column=i+1)
        hdownlabel[i].bind('<KeyRelease>',SizeCont)
        hdownlabel[i].bind('<Key>',LimitBox)
        hleftlabelv.append(IntVar())
        hleftlabel.append(Entry(framehints,width=2, font=("asdsas",30, ),justify=CENTER,textvariable=hleftlabelv[i]))
        hleftlabel[i].grid(row=i+1, column=puzzle.size+1)
        hleftlabel[i].bind('<KeyRelease>',SizeCont)
        hleftlabel[i].bind('<Key>',LimitBox)
        hrightlabelv.append(IntVar())
        hrightlabel.append(Entry(framehints,width=2, font=("asdsas",30, ),justify=CENTER,textvariable=hrightlabelv[i]))
        hrightlabel[i].grid(row=i+1, column=0)
        hrightlabel[i].bind('<KeyRelease>',SizeCont)
        hrightlabel[i].bind('<Key>',LimitBox)
    framehints.pack(side=RIGHT, pady=4, padx=4)
    Button(window2, text="Okey", command=Manhinter).pack(side=BOTTOM)

def Generate():
    PuzzleDestroyer()
    level=IntVar()
    level.set(1)
    window=Toplevel()
    window.title("Generate the Game")
    window.minsize(width=200, height=100)
    framesize=Frame(window, borderwidth=1, relief=RAISED)
    Label(framesize, text="The Size").pack(side=LEFT)
    number=Entry(framesize, width=2)
    number.pack(side=RIGHT)
    def GenerateDo():
        if(level.get()==1):
            puzzle.size=int(number.get())
            window.destroy()
            puzzle.generate()
            PuzzleMaker()
        if(level.get()==2):
            puzzle.size=int(number.get())
            window.destroy()
            GenerateDo2()

    framesize.pack(side=RIGHT, pady=4, padx=4)
    framelevel=Frame(window, borderwidth=1, relief=RAISED)
    Label(framelevel, text="Type of game").pack(side=LEFT)
    Radiobutton(framelevel, text="Generate it automaticly", value=1, variable=level).pack(side=TOP)
    Radiobutton(framelevel, text="I Will write hints", value=2,  variable=level).pack(side=TOP)
    framelevel.pack(side=LEFT, pady=4, padx=4)
    Button(window, text="Submit", command=GenerateDo).pack(side=BOTTOM)

anapencere=Tk()
anapencere.title("Apartmanlar")
anapencere.minsize()
F=Frame(anapencere)
F.pack(side=TOP, expand=YES, fill=BOTH)


def PuzzleDestroyer():
    for i in range(puzzle.size*puzzle.size):
        T[i].destroy()
    for i in range(puzzle.size*puzzle.size-1,-1,-1):
        T.remove(T[i])
        
    for i in range(puzzle.size):
        puzzle.hint.huplabel[i].destroy()
        puzzle.hint.hdownlabel[i].destroy()
        puzzle.hint.hleftlabel[i].destroy()
        puzzle.hint.hrightlabel[i].destroy()
    for i in range(puzzle.size-1,-1,-1):
        puzzle.hint.huplabel.remove(puzzle.hint.huplabel[i])
        puzzle.hint.hdownlabel.remove(puzzle.hint.hdownlabel[i])
        puzzle.hint.hleftlabel.remove(puzzle.hint.hleftlabel[i])
        puzzle.hint.hrightlabel.remove(puzzle.hint.hrightlabel[i])
    puzzle.clean()

def LimitBox(event):
    event.widget.delete(0, END)

def SizeCont(event):
    try:
        if (not(int(event.char)<=puzzle.size and int(event.char)>0)):
            event.widget.delete(0, END)
    except:
        event.widget.delete(0, END)
def PuzzleMaker():
    for i in range(puzzle.size*puzzle.size):
        T.append(Entry(F, width=2, font=("asdsas",30, ),justify=CENTER))
        T[i].grid(row=(i/puzzle.size+1), column=(i%puzzle.size)+1)
        T[i].config(textvariable=puzzle.boxes[i/puzzle.size][i%puzzle.size].entry)
        T[i].bind('<Key>',LimitBox)
        T[i].bind('<KeyRelease>',SizeCont)
    Clearf()
    for i in range(puzzle.size):
        puzzle.hint.huplabel.append(Label(F, width=1,  height = 1, text = str(puzzle.hint.hintsup[i]),font=("asdsas",30, ), padx=15))
        puzzle.hint.huplabel[i].grid(row=0, column=i+1)
        puzzle.hint.hdownlabel.append(Label(F, width=1,  height = 1,text = str(puzzle.hint.hintsdown[i]), font=("asdsas",30, ), padx=15))
        puzzle.hint.hdownlabel[i].grid(row=(puzzle.size+1), column=i+1)
        puzzle.hint.hleftlabel.append(Label(F, width=1,  height = 1,text = str(puzzle.hint.hintsleft[i]), font=("asdsas",30, ), padx=15))
        puzzle.hint.hleftlabel[i].grid(row=i+1, column=puzzle.size+1)
        puzzle.hint.hrightlabel.append(Label(F, width=1,  height = 1,text = str(puzzle.hint.hintsright[i]), font=("asdsas",30, ), padx=15))
        puzzle.hint.hrightlabel[i].grid(row=i+1, column=0)

Checkb=Button(anapencere)
Checkb.config(text="Check",  command=Checkf)
Solveb=Button(anapencere)
Solveb.config(text="Solve",  command=Solvef)
Clearb=Button(anapencere)
Clearb.config(text="Clear",  command=Clearf)
Checkb.pack(side=LEFT)
Solveb.pack(side=LEFT)
Clearb.pack(side=LEFT)

topmenu=Menu(anapencere)
anapencere.config(menu=topmenu)
Play=Menu(topmenu)
Play.add_command(label="Generate",underline = 0, command=Generate)
Play.add_command(label="Load",underline = 0, command=Load)
Play.add_command(label="Save",underline = 0, command=Save)
Play.add_separator()
Play.add_command(label="Quit",underline = 0, command=anapencere.quit)
topmenu.add_cascade(label="Play",underline = 0,  menu=Play)
anapencere.mainloop()