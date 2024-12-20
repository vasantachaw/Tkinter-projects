import mysql.connector as mq



fn='Basanta'
ln='chaw'
email='chaudharybasanta69@gmail.com'
address='Kathmandu'
contact=9808046983
pas='chaw'
conpass='chaw'
sex='male'
sql=sql=('insert into register(fname,lname,email,sex,pass,confirmpass,address,contact) values ("{0}","{1}","{2}","{3}","{4}","{5}","{6}")'.format(fn,ln,email,sex,pas,conpass,address,contact))
            
conn=mq.connect(host='localhost',user='root',password='',database='sms')
cur=conn.cursor()
if conn.is_connected():
    cur.execute(sql)
    conn.commit()
    print('ok')
else:
    print('no')
    cur.close()
    conn.close()
