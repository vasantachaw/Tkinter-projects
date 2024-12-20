
import mysql.connector as mq
import datetime
import pyttsx3 as pt
'''
MySQL is one of the most popular database management systems (DBMSs) on the market today. 
we have used the Mysql in python for backend server for data store int db .it gives many
 functions to  data manage,data organaized step by step
and insert ,delete ,create and update etc


'''
# the program is coded by Chawbasanta


'''
pyttsx3 is a text-to-speech conversion library in Python.
Unlike alternative libraries, it works offline
'''


def Speak(audio):
    engine = pt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()


def WishMe():  # This method is make for wishing me when we open the program

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak('Goood Morning have a you nice today ')
    elif hour >= 12 and hour < 18:
        Speak('Good Afternoon')
    elif hour >= 18 and hour < 20:
        Speak('Good Evening')
    else:
        Speak('Goood night ')

# Student_management_system_database class


class DB_sms:
    # create new database needed by user
    def NEw_CreateDatabase(self):
        try:
            # make the connection
            conn = mq.connect(host='localhost', user='root', password='')
            Speak('Enter want you create database name')
            db_name = str(input('\t\t\t\t\t\tEnter want you database name : '))
            cur = conn.cursor()
            sql = 'create database {0}'.format(db_name)
            if(conn.is_connected()):  # check the connection is True or False
                if(conn.is_connected() != 0):
                    cur.execute(sql)
                    sp = 'successfully created your {0} database'.format(
                        db_name)
                    Speak(sp)
                else:
                    sp = 'Unsuccessfully created your {0} database'.format(
                        db_name)
                    Speak(sp)

            else:
                Speak('Unuccessfully connection')

            cur.close()
            conn.close()
        except:
            Speak('Unuccessfully connection please try again')
            pass

# use database after created by user in mysql with help of python
    def Use_database(self):
        try:
            Speak('Enter want you use database name')
            self.db_use = str(
                input('\t\t\t\t\t\tEnter want you use database name : '))
            conn = mq.connect(host='localhost', user='root', password='')
            cur = conn.cursor()
            sql = 'use {0}'.format(self.db_use)
            if(conn.is_connected()):
                if(conn.is_connected() != 0):
                    cur.execute(sql)
                    Speak('Successfully used '+self.db_use+' database')
                else:
                    Speak('Unsuccessfully used  '+self.db_use+' database')
            cur.close()
            conn.close()
        except:
            Speak('Unuccessfully connection please try again')
            pass


# create new table after used database by user
    # create table for register data of student

    def registertable(self):

        Speak('enter want you create table name')
        table_name = str(input('\t\t\t\t\t\tenter want you table name :'))
        conn = mq.connect(host='localhost', user='root',
                          password='', database=self.db_use)
        cur = conn.cursor()
        sql1 = ('''
            create table {0} (
            fname varchar(50) not null,
            lname varchar(50) not null,
            email varchar(50) not null,
            sex varchar(10) not null,
            passwords varchar(50) not null,
            conf_passwords varchar(50) not null,
            address varchar(70) not null,
            contact int(20) not null
        )
        ''').format(table_name)
        if(conn.is_connected()):
            if(conn.is_connected() != 0):
                cur.execute(sql1)
                conn.commit()
                Speak('Successfully created  '+table_name + 'table')
            else:
                Speak('unuccessfully created  '+table_name + 'table')
        else:
            Speak('Unuccessfully connection please try again')
            pass
        cur.close()  # close the connection of databas
        conn.close()

    # marksheet table create for kept student marks result and grades in the table

    def Marks_table(self):

        Speak('enter want you create table name')
        table_name = str(input('\t\t\t\t\t\tenter want you table name :'))
        conn = mq.connect(host='localhost', user='root',
                          password='', database=self.db_use)
        cur = conn.cursor()
        sql1 = ('''
            create table {0} (
            id INTEGER PRIMARY KEY AUTO_INCREMENT ,
            Fullname varchar(50) not null,
            Sex varchar(10) not null,
            Semester varchar(50) not null,
            CN int(10) not null,
            OS int(10) not null,
            CE int(10) not null,
            DC int(10) not null,
            JAVA int(10) not null,
            AT int (10) not null,
            Minp int(10) not null,
            MIS int(10) not null,
            avg int(10) not null,
            grade varchar(10) not null,
            remarks varchar(20) not null
        )
        ''').format(table_name)
        if(conn.is_connected()):
            if(conn.is_connected() != 0):
                cur.execute(sql1)
                conn.commit()
                Speak('Successfully created  '+table_name + 'table')
            else:
                Speak('unuccessfully created  '+table_name + 'table')
        else:
            Speak('Unuccessfully connection please try again')
            pass
        cur.close()  # close the connection of databas
        conn.close()


# create the table of Todo list daily activities of school day of students

    def todolist(self):

        Speak('enter want you create table name')
        todolistname = str(input('\t\t\t\t\t\tenter want you table name :'))
        conn = mq.connect(host='localhost', user='root',
                          password='', database=self.db_use)
        cur = conn.cursor()
        sql1 = ('''
                create table {0} (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                subject varchar(50) not null,
                task varchar(50) not null,
                day varchar(30) not null,
                dates date
            )
            ''').format(todolistname)
        if(conn.is_connected()):
            if(conn.is_connected() != 0):
                cur.execute(sql1)
                conn.commit()
                Speak('Successfully created  '+todolistname + 'table')
            else:
                Speak('unuccessfully created  '+todolistname + 'table')
        else:
            Speak('Unuccessfully connection please try again')

        cur.close()  # close the connection of databas
        conn.close()


# Drop the databases


    def drop_database(self):
        try:
            Speak('Enter want you drop database name')
            drop_db = str(
                input('\t\t\t\t\t\tEnter want you drop database name : '))
            conn = mq.connect(
                host='localhost', user='root', password='', database=drop_db)
            cur = conn.cursor()
            sql = 'drop database {0}'.format(drop_db)
            if(conn.is_connected()):
                if(conn.is_connected() != 0):
                    cur.execute(sql)
                    Speak('Successfully droped '+drop_db+' database')
                else:
                    Speak('Unsuccessfully used  '+drop_db+' database')
            cur.close()
            conn.close()
        except:
            Speak('Unuccessfully connection please try again')
            pass


# drop the table


    def drop_table(self):

        Speak('Enter want you drop table name')
        drop_table = str(
            input('\t\t\t\t\t\tEnter want you drop table name : '))
        conn = mq.connect(
            host='localhost', user='root', password='', database=self.db_use)
        cur = conn.cursor()
        sql = 'drop table {0}'.format(drop_table)

        if(conn.is_connected()):
            if(conn.is_connected() != 0):
                cur.execute(sql)
                Speak('Successfully droped '+drop_table+' table')
            else:
                Speak('Unsuccessfully used  '+drop_table+' table')
        else:
            Speak('Unuccessfully connection please try again')
            pass
        cur.close()
        conn.close()


# show  the database


    def show_databases(self):

        Speak(' can you   show the  databases')

        conn = mq.connect(host='localhost', user='root', password='')
        cur = conn.cursor()
        sql = 'show databases;'
        if(conn.is_connected()):
            if(conn.is_connected() != 0):
                cur.execute(sql)
                Speak('Successfully databases here available')
                for databases in cur:
                    print('\t\t\t\t\t\t', databases)
            else:
                Speak('unsuccessfully databases are not available here')
        else:
            Speak('Unsuccessfully connection')
        cur.close()
        conn.close()

    def show_tables(self):

        Speak('can you show the tables please enter your database name')
        showTable = str(input('\t\t\t\t\t\tEnter your database Name : '))
        conn = mq.connect(host='localhost', user='root',
                          password='', database=showTable)
        myquery = 'show tables'
        mycur = conn.cursor()
        if conn.is_connected():
            if(conn.is_connected() != 0):
                mycur.execute(myquery)
                Speak('Successfully tables here available')
                for var in mycur:
                    print('\t\t\t\t\t\t', var)
            else:
                Speak('unsuccessfully show tables !')
        else:
            Speak('Unsuccessfully connection')
        mycur.close()
        conn.close()


# WishMe()  # ,alert me every time

db = DB_sms()
# WishMe()
print('\n\n\n')
user = str(input('\t\t\t\t\t\t\tUser Name : '))
password = str(input('\t\t\t\t\t\t\tUser Pass : '))
if user == 'admin' and password == '123':

    while True:
        print()
        print('\t\t\t\t--------------------- ! ! DATABASE Of SMS!!---------------------')
        print()
        print('\t\t\t\t\t\t  [1]   Create Database      ')
        print('\t\t\t\t\t\t  [2]   Use Database         ')
        print('\t\t\t\t\t\t  [3]   Create Register Table')
        print('\t\t\t\t\t\t  [4]   Create Marksheet Table')
        print('\t\t\t\t\t\t  [5]   Create Todo List Table')
        print('\t\t\t\t\t\t  [6]   Drop Database        ')
        print('\t\t\t\t\t\t  [7]   Drop Table           ')
        print('\t\t\t\t\t\t  [8]   Show Databases       ')
        print('\t\t\t\t\t\t  [9]   Show Tables          ')
        num = int(input('\t\t\t\t\t\t [10]   Do you want exit  : '))
        print()
        if num == 1:
            db.NEw_CreateDatabase()
        elif num == 2:
            db.Use_database()
        elif num == 3:
            db.registertable()
        elif num == 4:
            db.Marks_table()
        elif num == 5:
            db.todolist()
        elif num == 6:
            db.drop_database()
        elif num == 7:
            db.drop_table()
        elif num == 8:
            db.show_databases()
        elif num == 9:
            db.show_tables()
        elif num == 10:
            break
        else:
            Speak('You have entered invalid number please try again')

else:
    Speak('Invalid password and user name please try again')
