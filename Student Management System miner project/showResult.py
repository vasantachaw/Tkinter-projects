
from cProfile import label
from tkinter import*
from tkinter import ttk
from matplotlib.pyplot import text
import mysql.connector as mq


class ShowResult(object):
    def TableResult(self, win):
        try:

            self.tree = ttk.Treeview(win, columns=(
                1, 2, 3, 4, 5), show='headings', height=8)
            self.tree.place(x=24, y=10)
            self.tree.heading(1, text='S.N', anchor=W)
            self.tree.heading(2, text='Full Name', anchor=W)
            self.tree.heading(3, text='Semester', anchor=W)
            self.tree.heading(4, text='Remarks', anchor=W)
            self.tree.heading(5, text='Trade')
            self.tree.column(1, width=50)
            self.tree.column(2, width=130)
            self.tree.column(3, width=70)
            self.tree.column(4, width=70)
            self.tree.column(5, width=130)
            conn = mq.connect(host='localhost', user='root',
                              password='', database='dbsms')
            cur = conn.cursor()
            sql = 'select id,Fullname,Semester,remarks from marksheet'
            cur.execute(sql)
            for x in cur:
                self.tree.insert(parent='', index=END,
                                 values=[x[0], x[1], x[2], x[3], 'computer Engeenring'], text='parent')
        except:
            self.tree = ttk.Treeview(win, columns=(
                1, 2, 3, 4, 5), show='headings', height=8)
            self.tree.place(x=24, y=10)
            self.tree.heading(1, text='S.N', anchor=W)
            self.tree.heading(2, text='Full Name', anchor=W)
            self.tree.heading(3, text='Semester', anchor=W)
            self.tree.heading(4, text='Remarks', anchor=W)
            self.tree.heading(5, text='Trade')
            self.tree.column(1, width=50)
            self.tree.column(2, width=130)
            self.tree.column(3, width=70)
            self.tree.column(4, width=70)
            self.tree.column(5, width=130)

    def __init__(self, win):

        self.TableResult(win)
        self.lb = Label(win, text='Result   Published', font=(
            'arial', 12, 'bold')).place(x=170, y=206)
        self.bottom = Frame(win, bg='orange', height=8).pack(
            side=BOTTOM, fill=X)


def main():
    win = Tk()
    win.title("_ShowResult")
    win.iconbitmap("images/img/ss.ico")
    win.geometry("500x250")
    ShowResult(win)
    win.mainloop()


if __name__ == '__main__':
    main()
