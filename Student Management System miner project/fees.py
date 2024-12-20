from tkinter import *
from tkinter import ttk
from datetime import datetime


class ComputerFee(object):
    def __init__(self) -> None:
        pass

def main():
    win=Tk()
    win.title('_Computer Fee ')
    win.iconbitmap('images/img/ss.ico')
    win.geometry('600x300')
    win.mainloop()

if __name__=='__main__':
    main()