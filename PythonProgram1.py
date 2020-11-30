import tkinter as tk
from tkinter import filedialog as fd
import random

import soundfile as sf
import sounddevice as sd
from scipy.io.wavfile import write
import wave

class Nagranie:
    nazwa = " "

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
            self.nagranie.nazwa=name;
            print(name)

    def play(self):
        if self.nagranie.nazwa!= " ":
            data, fs = sf.read(self.nagranie.nazwa, dtype='float32')
            sd.play(data, fs)

    def recordFun(self, fs, s):
        #fs=44100 #próbki/s
        #s = 3
        print("nagranie 1")
        nagranie = sd.rec(int(fs*s), samplerate=fs, channels=2)
        sd.wait()
        write("filename1.wav", fs, nagranie)
        #files.append('filename1.wav')
        print("nagranie 2")
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
            print("tutaj")
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
        from scipy.io.wavfile import write
        self.btn3['state'] = 'normal'
        nagranie = sd.rec(int(fs * s), samplerate=fs, channels=2)
        sd.wait()
        sd.play(nagranie, fs)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        #######################
        menubar = tk.Menu(self)

        submenu1 = tk.Menu(menubar, tearoff=0)
        submenu1.add_command(label="Otwórz", command=lambda:self.otwórz())
        submenu1.add_command(label="Zapisz", command=lambda:self.fun2("test 12"))
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
        btn2 = tk.Button(self, text="Pause", command=lambda:self.fun(1), state=tk.ACTIVE)
        btn2.place(x=52, y=2, width=50, height=25)
        self.btn3 = tk.Button(self, text="Nagraj", command=lambda:self.nagraj(44100, 2), state=tk.ACTIVE)
        self.btn3.place(x=102, y=2, width=50, height=25)
        btn4 = tk.Button(self, text=" ", command=lambda:self.fun(1), state=tk.ACTIVE)
        btn4.place(x=152, y=2, width=50, height=25)
        btn5 = tk.Button(self, text=" ", command=lambda:self.fun(1), state=tk.ACTIVE)
        btn5.place(x=202, y=2, width=50, height=25)


        widget1 = tk.Canvas(self, bg="white", height=100).place(x= 10, y=30, width=500, height=300)
        #lbl = tk.Label(self, text="Opis pliku dźwiękowego", anchor=tk.E).grid(column=1, columnspan=6, sticky="w")
        widget2 = tk.Canvas(self, bg="white").place(x= 10, y=350, width=500, height=80)




        self.pack(side="top", fill="both", expand=True)



if __name__ == "__main__":

   root = tk.Tk()
   root.title("Spektrogram")
   root.geometry("600x450")
   root.resizable(False,False)
   app = Aplikacja(root)
   root.mainloop()

   
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