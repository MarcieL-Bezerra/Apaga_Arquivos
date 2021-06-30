import tkinter.filedialog as fdlg
import os
import tkinter as tk
import tkinter.messagebox as tkMessageBox
from tkinter import *
import pandas as pd

tinicial = tk.Tk()
tinicial.geometry("800x500+200+100")
tinicial.title("APAGA ARQUIVOS - SIS")
tinicial.resizable(width=False, height=False)
tinicial['bg'] = '#49A'
tinicial.iconphoto(True, PhotoImage(file='./arquivos/junta.png'))
image=PhotoImage(file='./arquivos/junta.png')

colunaum='Código da Loja'
colunadois='CPF'



caminhoinicial = './conversas'
files = os.listdir(caminhoinicial)
#df = pd.DataFrame()

files_mp3 =[caminhoinicial + '\\' + f for f in files if f[-3:]== 'mp3']


print(files_mp3)

for f in files_mp3:
	os.remove(f)



tinicial.mainloop()