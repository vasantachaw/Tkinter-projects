from tkinter import *
from tkinter.font import BOLD
from tkinter import Label, Button
from PIL import Image, ImageTk
from tkinter import filedialog, Message
import qrcode


def fileopens():
    filepaths = filedialog.askopenfilename(
        initialfile="")

    filetext = open(filepaths, 'r')
    textfield.insert('1.0', filetext.read())


def cleartext():
    textfield.delete('1.0', 'end')


def savefile():
    saves = textfield.get('1.0', 'end')
    savefiles = filedialog.asksaveasfile(
        initialfile="untiled txt", defaultextension='.txt', mode='w', filetypes=[('TXT', '*.txt')])

    try:
        savefiles.write(saves)

    except:
        Message('unsuccessfully')


def qr(qrtxt):
    qrimage = qrcode.make(qrtxt)
    qrimage = qrimage.resize((150, 150), Image.ANTIALIAS)
    qrimage.save('images/graphs/qrcode.png')

    image = PhotoImage(file='images/graphs/qrcode.png')
    Qrfield.config(image=image,height=170,width=180)
    Qrfield.image = image  # to prevent garbage collection from deleting the image


def QRcodess():
    st1 = textfield.get('1.0', 'end')
    qr(st1)


window = Tk()
window.config(background='#b8cfc7')
window.title("_Qr code")
window.geometry("550x220")
window.iconbitmap('images/img/ss.ico')

Qrlabel = Label(text="QRcode", font=('Arial', 15, BOLD),
                foreground='gray', background="#c1cee3")
Qrlabel.place(x=620, y=6)
Qrfield = Label(width=25, height=11, relief=GROOVE, text=" No QRcode",fg='orange')
Qrfield.place(x=350, y=35)

textfield = Text(window, width=40, height=11, relief=GROOVE,background='#f0f4fa')
textfield.place(x=13, y=35)

openbutton = Button(text="Open", relief=GROOVE,
                    width=8, command=fileopens)
openbutton.place(x=70, y=5)

savebutton = Button(text="Save",
                    relief=GROOVE, width=8, command=savefile)
savebutton.place(x=150, y=5)

clearbutton = Button(text="Clear", command=cleartext,
                     relief=GROOVE, width=8)
clearbutton.place(x=230, y=5)

Createqrbutton = Button(text="Create QR", command=QRcodess,
                        relief=GROOVE, width=8)
Createqrbutton.place(x=400, y=5)



myself = Label(text="developed by basanta chaudhary", fg='black',
               font=('Arial', 5, BOLD), background='#b8cfc7')
myself.place(x=177, y=373)
filepaths = StringVar()
#window.resizable(False, False)
window.mainloop()
