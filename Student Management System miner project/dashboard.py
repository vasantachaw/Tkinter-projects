import os
from tkinter import ttk
import datetime
#from typing_extensions import Self
# social links are defined here
import webbrowser
from tkinter import *
from matplotlib import pyplot as plt
import mysql.connector as mq
from PIL import Image, ImageTk


class Dashboard(object):
    def facebook(self):
        webbrowser.open('https://www.facebook.com/basantaChaw')

    def git(self):
        webbrowser.open('https://github.com/Chawbasanta')

    def twitter(self):
        webbrowser.open('https://twitter.com/Ibasanta69')

    def yt(self):
        webbrowser.open(
            'https://www.youtube.com/channel/UCF0bo_siMzdjxY_yMVrMypA')

    # def get_time(self, clock):
    #     import time
    #     self.clock = clock
    #     self.timevar = time.strftime("%I:%M:%S %p")
    #     self.clock.config(text=self.timevar)
    #     self.clock.after(200,self.get_time)
    # #Speak('hlo how are u darling')
    def datelb(self, win):
        import datetime
        print(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.r = datetime.datetime.now()
        self.res = self.r.strftime("  %B %d %Y , %a")

    def SexGraph(self, win):
        try:

            conn = mq.connect(host='localhost', user='root',
                              password='', database='dbsms')
            cur = conn.cursor()
            sql = 'select Sex,count(*) from marksheet where Sex=%s'
            val = ['Male']
            vals = ['Female']
            cur.execute(sql, val)
            self.ml = cur.fetchone()
            cur.execute(sql, vals)
            self.fm = cur.fetchone()
            plt.figure(figsize=(2, 5))
            x = ['Male', 'Female']
            y = [self.ml[1], self.fm[1]]
            colors = ['lightblue', 'pink']
            plt.bar(x, y, width=0.8, color=colors,
                    linestyle='dotted', lw=2, label='S E X')
            # plt.title()
            plt.legend()
            plt.savefig('images/graphs/sex.png', transparent=True)
        except:
            pass

    def Result(self, win):
        try:

            conn = mq.connect(host='localhost', user='root',
                              password='', database='dbsms')
            cur = conn.cursor()
            sql = 'select remarks,count(*) from marksheet where remarks=%s'
            p = ['passed']
            f = ['failed']
            cur.execute(sql, p)
            self.passed = cur.fetchone()
            cur.execute(sql, f)
            self.failed = cur.fetchone()
            plt.figure(figsize=(2, 5))
            x = ['Passed', 'Failed']
            y = [self.passed[1], self.failed[1]]
            colors = ['royalblue', 'tomato']
            plt.bar(x, y, width=0.8, color=colors,
                    linestyle='dotted', lw=2, label='RESULT')
            # plt.title()
            plt.legend()
            plt.savefig('images/graphs/result.png', transparent=True)
        except:
            pass

    def gradeGraph(self, win):
        try:

            conn = mq.connect(host='localhost', user='root',
                              password='', database='dbsms')
            cur = conn.cursor()
            sql = 'select Grade,count(*) from marksheet where Grade=%s'
            aPlush = ['A+']
            a = ['A']
            bPlush = ['B+']
            b = ['B']
            cPlush = ['C+']
            c = ['C']
            dPlush = ['D+']
            d = ['D']
            ePlush = ['E+']
            e = ['E']
            cur.execute(sql, aPlush)
            aPlusha = cur.fetchone()
            cur.execute(sql, bPlush)
            bPlusha = cur.fetchone()
            cur.execute(sql, cPlush)
            cPlusha = cur.fetchone()
            cur.execute(sql, dPlush)
            dPlusha = cur.fetchone()
            cur.execute(sql, ePlush)
            ePlusha = cur.fetchone()

            cur.execute(sql, a)
            aa = cur.fetchone()
            cur.execute(sql, b)
            bb = cur.fetchone()
            cur.execute(sql, c)
            cc = cur.fetchone()
            cur.execute(sql, d)
            dd = cur.fetchone()
            cur.execute(sql, e)
            ee = cur.fetchone()
            plt.figure(figsize=(8, 5))
            v = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'E+', 'E']
            x = [aPlusha[1], aa[1], bPlusha[1], bb[1], cPlusha[1],
                 cc[1], dPlusha[1], dd[1], ePlusha[1], ee[1]]

            # z=[33,55,44,67,88]
            colors = ['royalblue', 'pink', 'lightblue', 'thistle',
                      'orange', 'violet', 'lightgray', 'lightgreen']
            plt.ylabel('Grade ', fontsize=16)
            plt.bar(v, x, width=0.6, color=colors, linestyle='dotted',
                    lw=2, label='SEM III', alpha=0.6)
            # plt.title('RESULT',fontsize=16)
            plt.legend(loc=2)
            plt.savefig('images/graphs/grade.png', transparent=True)
        except:
            pass

    def Marking(self):
        self.mypath = 'mark.py'
        os.system('"%s"' % self.mypath)

    def logout(self):

        self.mypath = 'login.py'
        os.system('"%s"' % self.mypath)

    def ReadMode(self):
        self.mypath = 'ReadMode.py'
        os.system('"%s"' % self.mypath)

    def todolist(self):
        self.mypath = 'Todo.py'
        os.system('"%s"' % self.mypath)

    def showresult(self):
        self.mypath = 'showResult.py'
        os.system('"%s"' % self.mypath)

    def qrcodes(self):
        self.mypath = 'qrcodes.py'
        os.system('"%s"' % self.mypath)

    # here header deifined and menus bar

    def header(self, win):
        self.menus = Frame(self.win, height=45)
        self.menus.pack(side=TOP, fill=X)

        # menus part
        # logout buttom
        self.logout = Button(self.menus, text='Qr code', relief=GROOVE, fg='gray', font=(
            'Helavatic', 9, 'bold'), width=10, height=1, command=self.datelb).place(x=130, y=10)

        self.logout = Button(self.menus, text='LogOut', relief=GROOVE, fg='gray', font=(
            'Helavatic', 9, 'bold'), width=10, height=1, command=self.logout)
        self.logout.place(x=810, y=10)
        self.todo = Button(self.menus, text='Todo List', relief=GROOVE, fg='gray', font=(
            'Helavatic', 9, 'bold'), width=10, height=1, command=self.todolist)
        self.todo.place(x=210, y=10)

        # read button
        self.read = Button(self.menus, text='ReadMode', fg='gray', relief=GROOVE, font=(
            'Helavatic', 9, 'bold'), width=10, height=1, command=self.ReadMode)
        self.read.place(x=640, y=10)

        # show result
        self.showresult = Button(self.menus, text='show result', fg='gray', relief=GROOVE, font=(
            'Helavatic', 9, 'bold'), width=10, height=1, command=self.showresult)
        self.showresult.place(x=560, y=10)

        # calculate marks
        self.marks = Button(self.menus, text='Marks calculator', fg='gray', relief=GROOVE, font=(
            'Helavatic', 9, 'bold'), width=15, height=1, command=self.Marking)
        self.marks.place(x=400, y=10)

        # add data od students
        self.add = Button(self.menus, text='Fees', fg='gray', relief=GROOVE, font=(
            'Helavatic', 9, 'bold'), width=10, height=1)
        self.add.place(x=320, y=10)


# ----------------------------------------------------------------
#
#
#
# -----------------------------------------------------------------
    # graphs chart here functions defined

    def Graphs(self, win):

        # Bar diagramm graph
        self.barimg = Image.open('images/graphs/grade.png')
        self.barimg = self.barimg.resize((360, 200))
        self.barimage = ImageTk.PhotoImage(self.barimg)
        self.barlb = Label(self.win, image=self.barimage)
        self.barlb.place(x=180, y=50)
        self.result = Label(self.win, height=1, text='A+      A      B+      B      C+     C      D+      D      E+      E',
                            font=('Helavatic', 7))
        self.result.place(x=240, y=231)

# Pie chart
        self.pieimg = Image.open('images/graphs/pie.png')
        self.pieimg = self.pieimg.resize((230, 150))
        self.pieimage = ImageTk.PhotoImage(self.pieimg)
        self.pielb = Label(self.win, image=self.pieimage)
        self.pielb.place(x=540, y=70)
        self.sub = Label(self.win, height=1, text='Subjects',
                         font=('Helavatic', 7))
        self.sub.place(x=615, y=230)

# plot chart

        self.plotimg = Image.open('images/graphs/temp.png')
        self.plotimg = self.plotimg.resize((360, 200))
        self.plotimage = ImageTk.PhotoImage(self.plotimg)
        self.plotlb = Label(self.win, image=self.plotimage)
        self.plotlb.place(x=180, y=250)
# sex plot chart
        self.seximg = Image.open('images/graphs/sex.png')
        self.seximg = self.seximg.resize((100, 200))
        self.seximage = ImageTk.PhotoImage(self.seximg)
        self.sexlb = Label(self.win, image=self.seximage)
        self.sexlb.place(x=800, y=50)
        self.gender = Label(self.win, height=1, text='Male      Female',
                            font=('Helavatic', 7))
        self.gender.place(x=820, y=231)
# ---------------------------------------------------

        self.lineimg = Image.open('images/graphs/result.png')
        self.lineimg = self.lineimg.resize((100, 200))
        self.lineimage = ImageTk.PhotoImage(self.lineimg)
        self.linelb = Label(self.win, image=self.lineimage)
        self.linelb.place(x=930, y=50)
        self.work = Label(self.win, height=1, text=' Passed    Failed',
                          font=('Helavatic', 7))
        self.work.place(x=941, y=231)
        # self.line = Label(self.win, height=1, text='Male      Female',
        #                     font=('Helavatic', 7))
        # self.line.place(x=790, y=230)


# --------------------------------------

        # --------------------------------------------
        self.workimg = Image.open('images/graphs/working.png')
        self.workimg = self.workimg.resize((300, 200))
        self.workimage = ImageTk.PhotoImage(self.workimg)
        self.worklb = Label(self.win, image=self.workimage)
        self.worklb.place(x=550, y=250)

        # ---------------------------------------------
        self.skillimg = Image.open('images/graphs/skiil.png')
        self.skillimg = self.skillimg.resize((230, 150))
        self.skillimage = ImageTk.PhotoImage(self.skillimg)
        self.skilllb = Label(self.win, image=self.skillimage)
        self.skilllb.place(x=850, y=280)
        self.skill = Label(self.win, height=1, text='Working Progress',
                           font=('Helavatic', 7))
        self.skill.place(x=640, y=430)
# ----------------------------------------------------------------
#
# here socila link method are define linke facebook ,instagram,youtube\
# github and witter etc can you also follow me with this links and you get free my own projects codes of
# Stuident managememnt SYstem and ideas
#
# -----------------------------------------------------------------

    def SocialLinks(self, win):
        self.facebookimg = Image.open('images/socialIcons/fb.png')
        self.facebookimg = self.facebookimg.resize((30, 30))
        self.facebookimgp = ImageTk.PhotoImage(self.facebookimg)
        self.facebookbtn = Button(
            self.leftSide, image=self.facebookimgp, bd=0, command=self.facebook)
        self.facebookbtn.place(x=10, y=460)

        # -------------------Twitter------------------
        self.twitterimg = Image.open('images/socialIcons/tw.png')
        self.twitterimg = self.twitterimg.resize((28, 28))
        self.twitterimgp = ImageTk.PhotoImage(self.twitterimg)
        self.twitterbtn = Button(self.leftSide, image=self.twitterimgp,
                                 bd=0, command=self.twitter)
        self.twitterbtn.place(x=50, y=460)

        # ----------------------Github------------------------------
        self.gitimg = Image.open('images/socialIcons/git.png')
        self.gitimg = self.gitimg.resize((30, 30))
        self.gitimgp = ImageTk.PhotoImage(self.gitimg)
        self.gitbtn = Button(
            self.leftSide, image=self.gitimgp, bd=0, command=self.git)
        self.gitbtn.place(x=90, y=460)

        # -----------------------Youtube----------------------
        self.ytimg = Image.open('images/socialIcons/yt.png')
        self.ytimg = self.ytimg.resize((30, 30))
        self.ytimgp = ImageTk.PhotoImage(self.ytimg)
        self.ytbtn = Button(self.leftSide, image=self.ytimgp,
                            bd=0, command=self.yt)
        self.ytbtn.place(x=135, y=460)

# -----------------------------------------------------------------------
# _______________________________________________________________________
# )))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\

    def Body(self, win):
        r = datetime.datetime.now().strftime("%Y-%m-%d")
        self.topbottom = Frame(self.win, bg='lightgray', height=70)
        self.topbottom.pack(side=BOTTOM, fill=X)
        # ---------------------------------------------------------
        self.semvalue = StringVar()
        self.sem = Label(self.topbottom, text='S E M : ( V )',
                         bg='lightgray', font=('Helavatic', 9))
        self.sem.place(x=60, y=10)
        self.college = Label(self.topbottom, text='T R A D E  :  Computer  Engineering',
                             bg='lightgray', font=('Helavatic', 9, 'bold'))
        self.college.place(x=60, y=40)
        # Self.tasktable=ttk.Treeview(self.topbottom,columns=(1,2,3,4,5))

        self.about = Image.open('images/graphs/qrcode.png')
        self.about = self.about.resize((70, 70))
        self.abouts = ImageTk.PhotoImage(self.about)
        self.aboutlb = Label(self.topbottom, image=self.abouts)
        self.aboutlb.place(x=845, y=0)
        try:

            self.tree = ttk.Treeview(self.topbottom, columns=(
                1, 2, 3), show='headings', height=1)
            self.tree.place(x=300, y=14)
            self.tree.heading(1, text='Male', anchor=W)
            self.tree.heading(2, text='Female', anchor=W)
            self.tree.heading(3, text='Total', anchor=W)
            self.tree.column(1, width=40)
            self.tree.column(2, width=40)
            self.tree.column(3, width=43)
            self.tree.insert(parent='', index=END, values=[
                [self.ml[1]], [self.fm[1]], [self.ml[1]+self.fm[1]]])
        except:
            self.tree = ttk.Treeview(self.topbottom, columns=(
                1, 2, 3), show='headings', height=1)
            self.tree.place(x=300, y=14)
            self.tree.heading(1, text='Male', anchor=W)
            self.tree.heading(2, text='Female', anchor=W)
            self.tree.heading(3, text='Total', anchor=W)
            self.tree.column(1, width=40)
            self.tree.column(2, width=40)
            self.tree.column(3, width=43)
            self.tree.insert(parent='', index=END, values=[
                ['0'], ['0'], ['0']])
        try:

            self.trees = ttk.Treeview(self.topbottom, columns=(
                1, 2, 3), show='headings', height=1)
            self.trees.place(x=450, y=14)
            self.trees.heading(1, text='Paased', anchor=W)
            self.trees.heading(2, text='Failed', anchor=W)
            self.trees.heading(3, text='Total', anchor=W)
            self.trees.column(1, width=45)
            self.trees.column(2, width=45)
            self.trees.column(3, width=48)
            self.trees.insert(parent='', index=END, values=[
                [self.passed[1]], [self.failed[1]], [self.passed[1]+self.failed[1]]])
        except:
            self.trees = ttk.Treeview(self.topbottom, columns=(
                1, 2, 3), show='headings', height=1)
            self.trees.place(x=450, y=14)
            self.trees.heading(1, text='Passed', anchor=W)
            self.trees.heading(2, text='Failed', anchor=W)
            self.trees.heading(3, text='Total', anchor=W)
            self.trees.column(1, width=45)
            self.trees.column(2, width=45)
            self.trees.column(3, width=48)
            self.trees.insert(parent='', index=END, values=[
                ['0'], ['0'], ['0']])
        self.datelabel = Label(win, text=self.res,font=('arial',13,'bold'),bg='lightgrey',fg='grey').place(x=800, y=490)

    def __init__(self, win):
        self.win = win
        # self.adminImage = Image.open('img/tt.png')
        # self.adminImage = self.adminImage.resize((150, 150))
        # self.adminimg = ImageTk.PhotoImage(self.adminImage)

        self.mine = Image.open('images/img/ib.png')
        self.mine = self.mine.resize((152, 150))
        self.mineimg = ImageTk.PhotoImage(self.mine)

        self.leftSide = Frame(self.win, bg='whitesmoke', width=180)
        self.leftSide.pack(side=LEFT, fill=Y)
        # self.adminimglb = Label(
        #     self.leftSide, image=self.adminimg,).place(x=13, y=50)
        self.bottom = Frame(self.win, bg='#FF6F00', height=5)
        self.minelb = Label(
            self.leftSide, image=self.mineimg,).place(x=10, y=50)
        self.name = Label(self.win, text='Specialist', fg='gray', font=(
            'Helavatic', 10, 'bold')).place(x=10, y=185)
        self.name = Label(self.win, text='Name : Basanta Chaw', fg='gray', font=(
            'Helavatic', 9, 'bold')).place(x=10, y=210)
        self.name = Label(self.win, text='Trade : Computer Engineer', fg='gray', font=(
            'Helavatic', 9, 'bold')).place(x=10, y=230)
        self.name = Label(self.win, text='Lives In : Kathmandu,Nepal', font=(
            'Helavatic', 9, 'bold'), fg='gray').place(x=10, y=250)

        self.bottom.pack(side=BOTTOM, fill=X)

        # menus functions
        self.header(win)

        self.SexGraph(win)
        self.Result(win)
        self.gradeGraph(win)
        # soacila links functions \
        self.SocialLinks(win)
        self.datelb(win)
        # Graphs chart of alll data after analysis
        self.Graphs(win)

        # clock Part
        self.clock = Label(self.leftSide, width=15, height=1, text='STudent  M S',
                           font=('verdana', 13, 'bold'), fg='gray', bg='#f8c870')
        self.clock.place(x=5, y=10)

        self.qrcodeimg = Image.open('images/graphs/qrcode.png')
        self.qrcodeimg = self.qrcodeimg.resize((45, 45))
        self.qrimage = ImageTk.PhotoImage(self.qrcodeimg)
        self.qrimagelb = Label(self.leftSide, image=self.qrimage)
        self.qrimagelb.place(x=125, y=495)

        # ---------------------------------------------

        self.footer = Label(self.leftSide, width=15, height=1, text='@Copyright 2023',
                            font=('Helavatic', 9), fg='#1f1f1f', bg='#f0b548')
        self.footer.place(x=10, y=510)

        # body functions here
        self.Body(win)


def main_win():
    win = Tk()
    win.title('_Dashboard')
    win.geometry('1100x550')
    win.iconbitmap('images/img/ss.ico')
    # win.config(bg='lightgreen')
    Dashboard(win)

    win.resizable(False, False)
    win.mainloop()


if __name__ == '__main__':
    main_win()
