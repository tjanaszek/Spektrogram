import tkinter as tk
from tkinter import filedialog as fd
import random

import soundfile as sf
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io import wavfile as wav
import wave

import matplotlib
matplotlib.use('TKAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from matplotlib.widgets import SpanSelector



class Nagranie:
    nazwa = " "
    plik = " "

class Aplikacja(tk.Frame):

    nagranie = Nagranie

    def fun(self, arg1):
        print("test "+str(arg1))

    def fun2(self, arg1):
        print("test "+ arg1)

    def otwórz(self):
        name = fd.askopenfilename()
        if name:
            #data, fs = sf.read(name, dtype='float32')
            #sd.play(data, fs)
            self.nagranie.nazwa=name
            self.variable.set(name)
            self.rysuj(name)


    def zapisz(self):
        if self.nagranie.plik!= " ":
            filename = fd.asksaveasfilename(filetypes=[("Plik dźwiękowy",".wav")]) # wywołanie okna dialogowego save file
        
        #if filename:
            #with open(filename, "w", -1, "utf-8") as file:
                #file.write(self.text.get(1.0, tk.END))


    def play(self):
        if self.nagranie.nazwa!= " ":
            data, fs = sf.read(self.nagranie.nazwa, dtype='float32')
            sd.play(data, fs)
        elif self.nagranie.plik != " ":
            sd.play(self.nagranie.plik)

    def pause(self):
        sd.stop()

    def recordFun(self, fs, s):
        nagranie = sd.rec(int(fs*s), samplerate=fs, channels=2)
        sd.wait()
        write("filename1.wav", fs, nagranie)
        #files.append('filename1.wav')
        nagranie = sd.rec(int(fs*s), samplerate=fs, channels=2)
        sd.wait()
        write("filename2.wav", fs, nagranie)
        #files.append('filename2.wav')
        #files.append(nagranie)
        filename1="filename1.wav"
        filename2="filename2.wav"
        files =[filename1, filename2]
        outfile="wyjsciowy.wav"
        data=[]
        for file in files:
            with wave.open(file, "rb") as w:
                data.append([w.getparams(), w.readframes(w.getnframes())])
        with wave.open(outfile, "wb") as output:
            output.setparams(data[0][0])
            for i in range(len(data)):
                output.writeframes(data[i][1])
        #nagranie = sd.rec(int(fs*s), samplerate=fs, channels=2)
        #sd.wait()
        #write("test.wav", fs, nagranie)
        sd.play(nagranie)
        #sd.wait()

    def nagraj(self, fs, s):
        self.btn3['state'] = 'normal'
        nagranie = sd.rec(int(fs * s), samplerate=fs, channels=2)
        print(type(nagranie))
        sd.wait()
        self.nagranie.plik=nagranie

    def rysuj(self, filename):
        rate, data = wav.read(filename)
        channel1 = data[:,0]
        fig = Figure(linewidth=1, edgecolor='#000000')
        a = fig.add_subplot(111)
        a.plot(channel1, color = 'black')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().place(x=10, y=355, width=600, height=200)
        #a.axis('off')
        a.invert_yaxis()
        a.set_yticklabels([])
        a.set_xticklabels([])
        fig.tight_layout()
        canvas.draw()

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        #######################
        menubar = tk.Menu(self)

        submenu1 = tk.Menu(menubar, tearoff=0)
        submenu1.add_command(label="Otwórz", command=lambda:self.otwórz())
        submenu1.add_command(label="Zapisz", command=lambda:self.zapisz())
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
    
        btn1 = tk.Button(self, text="Play", command=lambda:self.play(), state=tk.ACTIVE)
        btn1.place(x=2, y=2, width=50, height=25)
        btn2 = tk.Button(self, text="Pause", command=lambda:self.pause(), state=tk.ACTIVE)
        btn2.place(x=52, y=2, width=50, height=25)
        self.btn3 = tk.Button(self, text="Nagraj", command=lambda:self.nagraj(44100, 5), state=tk.ACTIVE)
        self.btn3.place(x=102, y=2, width=50, height=25)
        btn4 = tk.Button(self, text=" ", command=lambda:self.fun(1), state=tk.ACTIVE)
        btn4.place(x=152, y=2, width=50, height=25)
        btn5 = tk.Button(self, text=" ", command=lambda:self.fun(1), state=tk.ACTIVE)
        btn5.place(x=202, y=2, width=50, height=25)


        widget1 = tk.Canvas(self, bg="white", height=100).place(x= 10, y=30, width=600, height=300)
        self.variable = tk.StringVar();
        self.variable.set("Opis pliku")
        lbl = tk.Label(self, textvariable = self.variable, anchor=tk.E).place(x= 10, y=330, height=20)
        widget2 = tk.Canvas(self, bg="white").place(x= 10, y=350, width=600, height=200)

       

        self.pack(side="top", fill="both", expand=True)



if __name__ == "__main__":

   root = tk.Tk()
   root.title("Spektrogram")
   root.geometry("800x600")
   root.resizable(False,False)
   app = Aplikacja(root)
   root.mainloop()


   #rate, data = wav.read('miasto_słońca.wav')
   rate, data = wav.read('test.wav')

   channel1 = data[:,0]
   channel2 = data[:,1]

   # otwarcie pliku
   #filename1 = "miasto_słońca.wav"
   #data, fs = sf.read(filename1, dtype='float32')
   #print(fs)
   #sd.play(data, fs)
   #sd.wait()

   #nagranie pliku
   #fs=44100 #próbki/s
   #s = 3
   #nagranie = sd.rec(int(fs*s), samplerate=fs, channels=2)
   #sd.wait()
   #write("test.wav", fs, nagranie)

   """
   #łączenie plików
   filename1 = "test.wav"
   filename2 = "filename2.wav"
   files = [filename1, filename2]
   outputfile = "test2.wav"
   data = []

   for file in files:
       #w = wave.open(file, "rb")
       #w.close()
       with wave.open(file, 'r') as w:
           data.append([w.getparams(), w.readframes(w.getnframes())])

   with wave.open(outputfile, 'wb') as output:
        output.setparams(data[0][0])
        for i in range(len(data)):
            output.write(frames(data[i][1]))
  
            """