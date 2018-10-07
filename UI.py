"""
Use the matrix containing the index position of the predicted class. Here I hav used random numbers just for demonstration purpose
"""



import tkinter
import random
window = tkinter.Tk()
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
f = tkinter.Text(window, height=200, width=200)
f.pack()
#tkinter.mainloop()
while True:
    n = random.randrange(0,25,1)
    f.insert(tkinter.END,str(alpha[n]))
    window.update_idletasks()
    window.update()
    
