from datetime import datetime
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


class TodolList(object):
    def droptodolist(self):
        conn = mq.connect(host='localhost', user='root',
                          password='', database='dbsms')
        cur = conn.cursor()
        if(conn.is_connected()):
            if(conn.is_connected() != 0):
                sql = ('delete from todolist where id={0}').format(
                    self.deleteid.get())
                cur.execute(sql)
                conn.commit()
                Speak('successfully deleted your data')
            else:
                Speak('Unsuccessfully deleted your data')
        else:
            Speak('Connection failed')

    def todoMysql(self):
        conn = mq.connect(host='localhost', user='root',
                          password='', database='dbsms')
        cur = conn.cursor()
        sql = ('insert into todolist(subject,task,day,dates)values(%s,%s,%s,%s)')
        if(self.days.get() == 'Wednesday (OFF Day)'):
            if(conn.is_connected()):
                if(conn.is_connected() != 0):
                    vals = ['---------Wed------------', '----------Wed-----------',
                            '---------OFF Day--------', datetime.now().strftime("%Y-%m-%d")]
                    cur.execute(sql, vals)
                    conn.commit()
                    Speak('successfully deleted your data')
                else:
                    Speak('Unsuccessfully deleted your data')
            else:
                Speak('Connection failed')
        else:
            if(conn.is_connected()):
                if(conn.is_connected() != 0):
                    vals = [self.subjects.get(), self.tasks.get(
                    ), self.days.get(), datetime.now().strftime("%Y-%m-%d")]
                    cur.execute(sql, vals)
                    conn.commit()
                    Speak('successfully deleted your data')
                else:
                    Speak('Unsuccessfully deleted your data')
            else:
                Speak('Connection failed')

    def bottoms(self, win):
        self.days = StringVar()
        self.subjects = StringVar()

        # days select options
        self.day = ttk.Combobox(win, width=15, textvariable=self.days)
        self.day["state"] = "readonly"
        self.day["values"] = ('Sunday', 'Monday', 'Tuesday',
                              'Wednesday (OFF Day)', 'Thursday', 'Friday', 'Saturday')
        self.day.current(0)
        self.day.place(x=10, y=340)

        # subjects select options
        self.subject = ttk.Combobox(win, width=20, textvariable=self.subjects)
        self.subject["state"] = "readonly"
        self.subject["values"] = ('Management Information System', 'Computer Network', 'Applied Telecommunication',
                                  'Operating System', 'Distributed System', 'Cyber Security and ethics', 'Java language', 'Miner Project')
        self.subject.current(0)
        self.subject.place(x=130, y=340)

        self.adds = Button(win, text='A D D', relief=GROOVE,
                           width=8, command=self.todoMysql).place(x=480, y=338)
        self.deleteds = Button(win, text='D r o p', relief=GROOVE,
                               width=14, command=self.droptodolist).place(x=620, y=338)

    def __init__(self, win):
        try:
            self.win = win
            self.todo = Label(win, text='T o d o   L i s t',
                              font=('Arial', 20, 'bold'), fg='gray',)
            self.todo.place(x=290, y=5)
            self.tree = ttk.Treeview(win, columns=(
                1, 2, 3, 4, 5), show='headings', height=12)
            self.tree.place(x=10, y=50)
            self.tasks = StringVar()
            self.deleteid = IntVar()
            self.tree.heading(1, text='S  .  N', anchor=W)
            self.tree.heading(2, text='S  U  B  J  E  C  T  S ', anchor=W)
            self.tree.heading(3, text='T  A  S  K', anchor=W)
            self.tree.heading(4, text='D  A  Y ', anchor=W)
            self.tree.heading(5, text='D  A  T  E', anchor=W)
            self.tree.column(1, width=50)
            self.tree.column(2, width=200)
            self.tree.column(3, width=180)
            self.tree.column(4, width=150)
            self.tree.column(5, width=150)
            # menus botoms are here kept
            self.bottoms(win)
            self.task = Entry(win, width=20, textvariable=self.tasks, font=(
                'arial', 12)).place(x=280, y=340)
            self.deleted = Entry(win, width=3, textvariable=self.deleteid, font=(
                'arial', 12)).place(x=580, y=340)
            # --------------------------------
            self.bottom = Frame(win, height=10, bg='orange').pack(
                side=BOTTOM, fill=X)
            self.copyright = Label(
                self.bottom, text='Copyright 2023').place(x=63, y=380)
            self.copyright = Label(
                self.bottom, text='Developed by Chaw basanta').place(x=594, y=380)
            conn = mq.connect(host='localhost', user='root',
                              password='', database='dbsms')
            cur = conn.cursor()
            if(conn.is_connected()):
                if(conn.is_connected() != 0):
                    sql = ("select * from todolist")
                    cur.execute(sql)
                    for row in cur:
                        self.tree.insert(parent='', index=END,
                                         values=row, text='parent')
            else:
                Speak('connection failed')
        except:
            self.win = win
            self.todo = Label(win, text='T o d o   L i s t',
                              font=('Arial', 20, 'bold'), fg='gray',)
            self.todo.place(x=290, y=5)
            self.tree = ttk.Treeview(win, columns=(
                1, 2, 3, 4, 5), show='headings', height=12)
            self.tree.place(x=10, y=50)
            self.tasks = StringVar()
            self.deleteid = IntVar()
            self.tree.heading(1, text='S  .  N', anchor=W)
            self.tree.heading(2, text='S  U  B  J  E  C  T  S ', anchor=W)
            self.tree.heading(3, text='T  A  S  K', anchor=W)
            self.tree.heading(4, text='D  A  Y ', anchor=W)
            self.tree.heading(5, text='D  A  T  E', anchor=W)
            self.tree.column(1, width=50)
            self.tree.column(2, width=200)
            self.tree.column(3, width=180)
            self.tree.column(4, width=150)
            self.tree.column(5, width=150)
            # menus botoms are here kept
            self.bottoms(win)
            self.task = Entry(win, width=20, textvariable=self.tasks, font=(
                'arial', 12)).place(x=280, y=340)
            self.deleted = Entry(win, width=3, textvariable=self.deleteid, font=(
                'arial', 12)).place(x=580, y=340)
            # --------------------------------
            self.bottom = Frame(win, height=20, bg='orange').pack(
                side=BOTTOM, fill=X)
            self.copyright = Label(
                self.bottom, text='Copyright 2023').place(x=63, y=380)
            self.copyright = Label(
                self.bottom, text='Developed by Chaw basanta').place(x=594, y=380)


def main():
    win = Tk()
    win.title('_Todo List')
    win.iconbitmap('images/img/ss.ico')
    win.geometry('750x400')
    win.resizable(False, False)
    TodolList(win)
    win.mainloop()


if __name__ == '__main__':
    main()
