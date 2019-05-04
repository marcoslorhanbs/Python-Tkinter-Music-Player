# coding: utf-8
from tkinter import *
from tkinter import messagebox
from pygame import *
from pygame import mixer
from playsound import playsound
import time


jan = Tk()
jan.title("Music Player")
jan.geometry("380x400")


frame = Frame(jan, width=300, height=100)
scrollbar = Scrollbar(frame, orient=VERTICAL)
listbox = Listbox(frame, yscrollcommand=scrollbar.set, width=300 ,font=("Century Gothic", 16), bd=3, bg="#0065fb", activestyle="none",selectbackground="#00398c", selectforeground="white")
for item in ["Trial By The Archon - Blind Guardian", "The Throne - Blind Guardian", "Thorn - Blind Guardian", "Time Stand Still - Blind Guardian"]:
    listbox.insert(END, item)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
frame.pack()



playimage = PhotoImage(file="MusicPlayer(Tkinter)/playbutton.png")
pauseimage = PhotoImage(file="MusicPlayer(Tkinter)/pausebutton.png")
stopimage = PhotoImage(file="MusicPlayer(Tkinter)/stopbutton.png")
nextimage = PhotoImage(file="MusicPlayer(Tkinter)/nextbutton.png")
backimage = PhotoImage(file="MusicPlayer(Tkinter)/backbutton.png")

#=============== Comandos e Definições ================================
def play():
    musica = listbox.get(ACTIVE)
    if (musica == "Trial By The Archon - Blind Guardian"):
            playbutton["image"] = pauseimage
            time.sleep(1)
            playsound('MusicPlayer(Tkinter)/Musicas/12 - Trial By The Archon (Demo Version).mp3')


playbutton = Button(jan, image=playimage, bd=0, command=play)
playbutton.place(x=150, y=300)

nextbutton = Button(jan, image=nextimage, bd=0)
nextbutton.place(x=240, y=310)

backbutton = Button(jan, image=backimage, bd=0)
backbutton.place(x=80, y=310)

stopbutton = Button(jan, image=stopimage, bd=0)
stopbutton.place(x=20, y=310)


jan.mainloop()