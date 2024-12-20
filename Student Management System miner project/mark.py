
from tkinter.font import BOLD
import mysql.connector as mq
from tkinter import*
from tkinter import ttk
import pyttsx3 as pt


def Speak(audio):
    engine = pt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()


class Marks(object):
    def deletedata(self):
        conn = mq.connect(host='localhost', user='root',
                          password='', database='dbsms')
        cur = conn.cursor()
        if(conn.is_connected()):
            if(conn.is_connected() != 0):
                sql = ('delete from marksheet where id={0}').format(
                    self.delvalue.get())
                cur.execute(sql)
                conn.commit()
                Speak('successfully deleted your data')
            else:
                Speak('Unsuccessfully deleted your data')
        else:
            Speak('Connection failed')

    def clearfill(self):
        self.fname.delete(0, END)
        self.lname.delete(0, END)
        self.minerP.delete(0, END)
        self.computerNet.delete(0, END)
        self.com.delete(0, END)
        self.Dc.delete(0, END)
        self.ces.delete(0, END)
        self.javas.delete(0, END)
        self.tll.delete(0, END)
        self.miss.delete(0, END)
        self.OS.delete(0, END)

    def updatingValue(self):
        conn = mq.connect(host='localhost', user='root',
                          password='', database='dbsms')
        cur = conn.cursor()
        if(conn.is_connected()):
            if(conn.is_connected() != 0):
                sql = ('update marksheet set {0}={1} where id={2}').format(
                    self.comOption.get(), self.valuesss.get(), self.id.get())
                cur.execute(sql)
                conn.commit()
                Speak('successfully deleted your data')
            else:
                Speak('Unsuccessfully deleted your data')
        else:
            Speak('Connection failed')

    def MarksCalculate(self):

        scn = self.cn.get()
        sdc = self.dc.get()
        stl = self.tl.get()
        sjava = self.java.get()
        sce = self.ce.get()
        sos = self.oss.get()
        sminp = self.minp.get()
        smis = self.mis.get()
        g = ''

        total = (scn+sdc+stl+sjava+sce+sos+sminp+smis)
        avg = int(total/8)

        if avg > 90 and avg <= 100:
            g = 'A+'
        elif avg > 80 and avg <= 90:
            g = 'A'
        elif avg > 70 and avg <= 80:
            g = 'B+'
        elif avg > 60 and avg <= 70:
            g = 'B'
        elif avg > 50 and avg <= 60:
            g = 'C+'
        elif avg > 40 and avg <= 50:
            g = 'C'
        elif avg > 30 and avg <= 40:
            g = 'D+'
        elif avg > 20 and avg <= 30:
            g = 'D'
        elif avg > 10 and avg <= 20:
            g = 'E+'
        elif avg >= 0 and avg <= 10:
            g = 'E'
        # print(self.fname.get())
        # print(self.lname.get())
        # print(avg)
        # print(g)
        # print(self.semester.get())
        # print(self.sex.get())

        conn = mq.connect(host='localhost', user='root',
                          password='', database='dbsms')
        cur = conn.cursor()
        sql = ('insert into marksheet(Fullname,Sex,Semester,CN,OS,CE,DC,JAVA,AT,Minp,MIS,avg,grade,remarks) values(%s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s,%s,%s)')

        if(conn.is_connected()):
            if (self.sex.get() == 1):
                if(conn.is_connected() != 0):
                    remarks = [sos, sce, sdc, sminp, sjava, smis, scn, stl]
                    counts = 0
                    for x in remarks:
                        if x >= 32:
                            counts += 1
                        else:
                            pass
                    if counts == 8:
                        male = 'Male'
                        vals = [self.fname.get()+'  '+self.lname.get(), male, self.semester.get(),
                                scn, sos, sce, sdc, sjava, stl, sminp, smis, avg, g, 'passed']
                        cur.execute(sql, vals)
                        conn.commit()
                        Speak('Successfully data inserted')
                    else:
                        male = 'Male'
                        vals = [self.fname.get()+'  '+self.lname.get(), male, self.semester.get(),
                                scn, sos, sce, sdc, sjava, stl, sminp, smis, avg, g, 'failed']
                        cur.execute(sql, vals)
                        conn.commit()
                        Speak('Successfully data inserted')

                else:
                    Speak('Unsuccessfully data inserted ')
            elif (self.sex.get() == 0):
                if(conn.is_connected() != 0):
                    remarks = [sos, sce, sdc, sminp, sjava, smis, scn, stl]
                    counts = 0
                    for x in remarks:
                        if x >= 32:
                            counts += 1
                        else:
                            pass
                    if counts == 8:
                        male = 'Female'
                        vals = [self.fname.get()+'  '+self.lname.get(), male, self.semester.get(),
                                scn, sos, sce, sdc, sjava, stl, sminp, smis, avg, g, 'Passed']
                        cur.execute(sql, vals)
                        conn.commit()
                        Speak('Successfully data inserted')
                    else:
                        male = 'Female'
                        vals = [self.fname.get()+'  '+self.lname.get(), male, self.semester.get(),
                                scn, sos, sce, sdc, sjava, stl, sminp, smis, avg, g, 'Failed']
                        cur.execute(sql, vals)
                        conn.commit()
                        Speak('Successfully data inserted')

                else:
                    Speak('Unsuccessfully data inserted ')
        else:
            Speak('Connection failed please try again')

        # print(type(self.cn.get()))
        # print('operating s'+self.oss.get())
        # print('cyber'+self.ce.get())
        # print('mis'+self.mis.get())
        # print('miner'+self.minp.get())
        # print('java'+self.java.get())
        # print('dc'+self.dc.get())
        # print('tl'+self.tl.get())
        #total = (scn+sdc+stl+sjava+sce+sos+sminp+smis)
        # print(len(total))

    def Delete(self, wins):
        self.delvalue = IntVar()
        self.ids = Entry(wins, width=3, bd=0,
                         textvariable=self.delvalue, font=('arial', 12))
        self.ids.place(x=530, y=18)
        self.updates = Button(wins, text='D r o p',
                              width=15, relief=GROOVE, bg='lightgray', command=self.deletedata)
        self.updates.place(x=564, y=15)

    def Update(self, wins):
        self.comOption = ttk.Combobox(wins, width=15)
        self.comOption["state"] = "readonly"
        self.comOption["values"] = (
            'Fname', 'Sex', 'Semester', 'MIS', 'CN', 'AT', 'DC', 'OS', 'CE', 'JAVA')
        self.comOption.current(0)
        self.comOption.place(x=20, y=18)

        self.valuesss = Entry(wins, width=18, bd=0, font=('arial', 12))
        self.valuesss.place(x=140, y=18)
        self.id = Entry(wins, width=3, bd=0,
                        textvariable=self.id, font=('arial', 12))
        self.id.place(x=300, y=18)
        self.updates = Button(wins, text='U p d a t e',
                              width=20, relief=GROOVE, bg='lightgray', command=self.updatingValue)
        self.updates.place(x=335, y=15)

    def calculator(self, win):
        self.fname = StringVar()
        self.lname = StringVar()
        self.semester = StringVar()
        self.sex = IntVar()
        self.id = IntVar()

        # subjects variable declared
        self.cn = IntVar()
        self.minp = IntVar()
        self.tl = IntVar()
        self.java = IntVar()
        self.dc = IntVar()
        self.ce = IntVar()
        self.mis = IntVar()
        self.oss = IntVar()

        self.calc = Label(win, text='Marks  Calculator',
                          fg='gray', font=('Arial', 15, 'bold'), width=15)
        self.calc.place(x=82, y=12)

        #---------------------Labels and Enterybox
        self.fnamelb = Label(
            win, text='f i r s t     n a m e', font=('Arial', 10))
        self.fnamelb.place(x=20, y=70)
        self.fname = Entry(win, width=25)
        self.fname.place(x=20, y=100)

        self.lnamelb = Label(win, text='l a s t     n a m e')
        self.lnamelb.place(x=200, y=70)
        self.lname = Entry(win, width=25)
        self.lname.place(x=200, y=100)

        self.select = Label(win, text='Select Semester', font=('Arial', 10))
        self.select.place(x=17, y=130)
        self.com = ttk.Combobox(win, width=22, textvariable=self.semester)
        self.com["state"] = "readonly"
        self.com["values"] = ('SEM (I)', 'SEM (II)',
                              'SEM (III)', 'SEM (IV)', 'SEM (V)', 'SEM (VI)')
        self.com.current(0)
        self.com.place(x=20, y=158)

        self.malelb = Label(win, text='M a l e')
        self.malelb.place(x=220, y=135)
        self.male = Radiobutton(win, value=1, variable=self.sex)
        self.male.place(x=230, y=155)

        self.femalelb = Label(win, text='F e m a l e ')
        self.femalelb.place(x=280, y=135)
        self.female = Radiobutton(win, value=0, variable=self.sex)
        self.female.place(x=295, y=155)

        # -------------subjects marks entry box
        #---------------------Labels and Enterybox
        self.computerNetLB = Label(
            win, text='Computer  Network', font=('Arial', 10))
        self.computerNetLB.place(x=20, y=195)
        self.computerNet = Entry(win, width=25, textvariable=self.cn)
        self.computerNet.place(x=20, y=230)

        self.OSLB = Label(win, text='Operating System')
        self.OSLB.place(x=200, y=195)
        self.OS = Entry(win, width=25, textvariable=self.oss)
        self.OS.place(x=200, y=230)

        self.MinerPLB = Label(win, text='Miner Project', font=('Arial', 10))
        self.MinerPLB.place(x=20, y=270)
        self.minerP = Entry(win, width=25, textvariable=self.minp)
        self.minerP.place(x=20, y=300)

        self.DcLB = Label(win, text='Distributed Computing')
        self.DcLB.place(x=200, y=270)
        self.Dc = Entry(win, width=25, textvariable=self.dc)
        self.Dc.place(x=200, y=300)

        self.tlLb = Label(win, text='Applied Telecommun', font=('Arial', 10))
        self.tlLb.place(x=20, y=340)
        self.tll = Entry(win, width=25, textvariable=self.tl)
        self.tll.place(x=20, y=370)

        self.misLB = Label(win, text='Management Information S')
        self.misLB.place(x=200, y=340)
        self.miss = Entry(win, width=25, textvariable=self.mis)
        self.miss.place(x=200, y=370)

        self.ceLB = Label(win, text='Cyber Security', font=('Arial', 10))
        self.ceLB.place(x=20, y=400)
        self.ces = Entry(win, width=25, textvariable=self.ce)
        self.ces.place(x=20, y=430)

        self.javaLB = Label(win, text='Java Language')
        self.javaLB.place(x=200, y=400)
        self.javas = Entry(win, width=25, textvariable=self.java)
        self.javas.place(x=200, y=430)
        self.Clear = Button(win, text='C l e a r', font=(
            'Arial', 10, 'bold'), width=18, bg='lightgray', relief=GROOVE, command=self.clearfill)
        self.Clear.place(x=20, y=470)
        self.calculate = Button(win, text='C a l c u l a t e', font=(
            'Arial', 10, 'bold'), width=18, bg='gray', relief=GROOVE, fg='white', command=self.MarksCalculate)
        self.calculate.place(x=200, y=470)

    # table showing all the inserted data
    def show_dataTable(self, win):
        try:
            tree = ttk.Treeview(win, columns=(
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), show='headings', height=23)
            tree.place(x=376, y=55)
            tree.heading(1, text='S.N', anchor=W)
            tree.heading(2, text='Full  Name', anchor=W)
            tree.heading(3, text='Sex', anchor=W)
            tree.heading(4, text='Semester', anchor=W)
            tree.heading(5, text='A T', anchor=W)
            tree.heading(6, text='D C', anchor=W)
            tree.heading(7, text='O S', anchor=W)
            tree.heading(8, text='C N', anchor=W)
            tree.heading(9, text='C E', anchor=W)
            tree.heading(10, text='JAVA', anchor=W)
            tree.heading(11, text='Miner P', anchor=W)
            tree.heading(12, text='M I S', anchor=W)
            tree.heading(13, text='Percent %', anchor=W)
            tree.heading(14, text='Grade', anchor=W)
            tree.heading(15, text='Remarks', anchor=W)
            tree.column(1, width=30)
            tree.column(2, width=120)
            tree.column(3, width=50)
            tree.column(4, width=70)
            tree.column(5, width=50)
            tree.column(6, width=50)
            tree.column(7, width=50)
            tree.column(8, width=50)
            tree.column(9, width=50)
            tree.column(10, width=50)
            tree.column(11, width=60)
            tree.column(12, width=50)
            tree.column(13, width=64)
            tree.column(14, width=60)
            tree.column(15, width=65)
            conn = mq.connect(host='localhost', user='root',
                              password='', database='dbsms')
            cur = conn.cursor()
            if(conn.is_connected()):
                if(conn.is_connected() != 0):
                    sql = ("select * from marksheet")
                    cur.execute(sql)
                    for row in cur:
                        tree.insert(parent='', index=END,
                                    values=row, text='parent')
            else:
                Speak('connection failed')
        except:
            tree = ttk.Treeview(win, columns=(
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), show='headings', height=23)
            tree.place(x=376, y=55)
            tree.heading(1, text='S.N', anchor=W)
            tree.heading(2, text='Full  Name', anchor=W)
            tree.heading(3, text='Sex', anchor=W)
            tree.heading(4, text='Semester', anchor=W)
            tree.heading(5, text='A T', anchor=W)
            tree.heading(6, text='D C', anchor=W)
            tree.heading(7, text='O S', anchor=W)
            tree.heading(8, text='C N', anchor=W)
            tree.heading(9, text='C E', anchor=W)
            tree.heading(10, text='JAVA', anchor=W)
            tree.heading(11, text='Miner P', anchor=W)
            tree.heading(12, text='M I S', anchor=W)
            tree.heading(13, text='Percent %', anchor=W)
            tree.heading(14, text='Grade', anchor=W)
            tree.heading(15, text='Remarks', anchor=W)
            tree.column(1, width=30)
            tree.column(2, width=120)
            tree.column(3, width=50)
            tree.column(4, width=70)
            tree.column(5, width=50)
            tree.column(6, width=50)
            tree.column(7, width=50)
            tree.column(8, width=50)
            tree.column(9, width=50)
            tree.column(10, width=50)
            tree.column(11, width=60)
            tree.column(12, width=50)
            tree.column(13, width=64)
            tree.column(14, width=60)
            tree.column(15, width=65)

    # define marks calculator GUI

    def __init__(self, win):
        self.leftside = Frame(win, width=370)
        self.leftside.pack(side=LEFT, fill=Y)
        self.top = Frame(win, bg='lightgray', height=55)
        self.top.pack(side=TOP, fill=X)
        self.calculator(self.leftside)
        self.Update(self.top)
        self.Delete(self.top)
        self.show_dataTable(win)
        self.bottom = Frame(win, height=5, bg='orange')
        self.bottom.pack(side=BOTTOM, fill=X)
        footer = Label(self.leftside, width=20, height=2, text='@Copyright 2023',
                       font=('Helavatic', 7,), fg='#1f1f1f')
        footer.place(x=3, y=515)
        footer = Label(self.leftside, width=30, height=2, text='@developed by Chawbasanta 2023',
                       font=('Helavatic', 9,), fg='#1f1f1f')
        footer.place(x=160, y=516)


def main():
    win = Tk()
    win.geometry('1250x550')
    win.iconbitmap('images/img/ss.ico')
    win.config(bg='lightgray')
    win.title('_Marks Calculator')
    Marks(win)
    win.resizable(False, False)
    win.mainloop()


if __name__ == '__main__':
    main()
