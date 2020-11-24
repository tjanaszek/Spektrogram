import tkinter as tk
import random

#import soundfile as sf
#import sounddevice as sd

#import matplotlib
#matplotlib.use('TKAgg')
#from matplotlib.backends.backend_tkagg import FigureCanvasTKAgg

class Aplikacja(tk.Frame):
   
    def fun(self, arg1):
        print("test "+str(arg1))

    def fun2(self, arg1):
        print("test "+ arg1)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        #######################
        menubar = tk.Menu(self)

        submenu1 = tk.Menu(menubar, tearoff=0)
        submenu1.add_command(label="Otwórz", command=lambda:self.fun2("test 11"))
        submenu1.add_command(label="Zapisz", command=lambda:self.fun2("test 12"))
        #submenu1.add_separator()
        #submenu1.add_command(label="Test 3", command=lambda:self.fun2("test 13"))
        menubar.add_cascade(label="Plik", menu=submenu1)

        submenu2 = tk.Menu(menubar, tearoff=0)
        #submenu2.add_command(label="Test 1", command=lambda:self.fun2("test 21"))
        #submenu2.add_command(label="Test 2", command=lambda:self.fun2("test 22"))
        #submenu2.add_separator()
        #submenu2.add_command(label="Test 3", command=lambda:self.fun2("test 23"))
        menubar.add_cascade(label="Edycja", menu=submenu2)

        menubar.add_cascade(label="Widok", menu=submenu2)

        menubar.add_cascade(label="Pomoc", menu=submenu2)
        ########################

        self.parent.config(menu=menubar)
    
        btn1 = tk.Button(self, text="Play", command=lambda:self.fun(1), state=tk.ACTIVE)
        btn1.place(x=2, y=2, width=50, height=25)
        btn2 = tk.Button(self, text="Pause", command=lambda:self.fun(1), state=tk.ACTIVE)
        btn2.place(x=52, y=2, width=50, height=25)
        btn3 = tk.Button(self, text="Nagraj", command=lambda:self.fun(1), state=tk.ACTIVE)
        btn3.place(x=102, y=2, width=50, height=25)
        btn4 = tk.Button(self, text=" ", command=lambda:self.fun(1), state=tk.ACTIVE)
        btn4.place(x=152, y=2, width=50, height=25)
        btn5 = tk.Button(self, text=" ", command=lambda:self.fun(1), state=tk.ACTIVE)
        btn5.place(x=202, y=2, width=50, height=25)

        #lbl = tk.Label(self, text="label 1", anchor=tk.E)
        #lbl.place(x=100, y=50, width=100, height=25)
        # tk.Button
        # tk.Label
        # tk.Menu
        # tk.Radiobutton
        # tk.Checkbutton
        # tk.Entry

        widget1 = tk.Canvas(self, bg="blue", height=100).place(x= 10, y=30, width=500, height=300)
        #lbl = tk.Label(self, text="Opis pliku dźwiękowego", anchor=tk.E).grid(column=1, columnspan=6, sticky="w")
        widget2 = tk.Canvas(self, bg="black").place(x= 10, y=350, width=500, height=80)

        # grid // kratka
        # place// dokładnie ustawiamy
        # pack //




        self.pack(side="top", fill="both", expand=True)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Spektrogram")
    root.geometry("600x450")
    root.resizable(False,False)
    app = Aplikacja(root)
    root.mainloop()