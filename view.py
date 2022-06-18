import tkinter
from tkinter import *
from tkinter import ttk

import showPlot
from reader import *
from main import *
from showPlot import show
root = Tk()
symbol_var = tkinter.StringVar()
poly_var = tkinter.StringVar()
guess_var = tkinter.StringVar()
iterations_var = tkinter.StringVar()
roots = []
def compute():
    roots.clear()
    s = symbol_var.get()
    p = poly_var.get()
    g = guess_var.get().split(", ")
    i = iterations_var.get()
    reader = Reader(s)
    reader.read(p)
    poly_derivative = reader.poly_derivative()
    p = p.replace(s, "x")
    for val in g:
        resses = []
        root = newton(float(val), p.replace("x", "*x"), poly_derivative, int(i), 0, resses)
        roots.append(root)
        for d in resses[-4:]:
           if (abs(root-d)) > 0.0001:
               roots.remove(root)
               break


def computeAndReload():
    compute()
    label.configure(text=roots)


def plot():
    if not len(roots) == 0:
        s = symbol_var.get()
        show(poly_var.get().replace(s, "*"+s), roots, s)


frm = ttk.Frame(root, padding=10)
frm.grid()
symbolText = ttk.Label(frm, text="Input symbol (x,t,r etc.)")
symbolText.pack()
symbolEntry = ttk.Entry(frm, textvariable=symbol_var)
symbolEntry.pack()
polynomialText = ttk.Label(frm, text="Input polynomial")
polynomialText.pack()
polynomialEntry = ttk.Entry(frm, textvariable=poly_var)
polynomialEntry.pack()
inputText = ttk.Label(frm, text="Input guesses")
inputText.pack()
inputEntry = ttk.Entry(frm, textvariable=guess_var)
inputEntry.pack()
iterationsText = ttk.Label(frm, text="Input iterations")
iterationsText.pack()
iterationsEntry = ttk.Entry(frm, textvariable=iterations_var)
iterationsEntry.pack()
computeText = ttk.Label(frm, text="Compute roots")
computeText.pack()
computeButton = ttk.Button(frm, text="Compute", command=computeAndReload)
computeButton.pack()
computedRoots = ttk.Label(frm, text="Computed roots")
computedRoots.pack()
label = ttk.Label(frm, text=str(roots))
label.pack()
plotButton = ttk.Button(frm, text="Show plot", command=plot)
plotButton.pack()

root.mainloop()


