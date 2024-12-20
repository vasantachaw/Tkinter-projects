# from matplotlib import pyplot as plt
# import mysql.connector as mq
# conn=mq.connect(host='localhost',user='root',password='',database='dbsms')
# cur=conn.cursor()
# sql='select Sex,count(*) from marksheet where Sex=%s'
# val=['Male']
# vals=['Female']
# cur.execute(sql,val)
# ml=cur.fetchone()
# cur.execute(sql,vals)
# fm=cur.fetchone()
# plt.figure(figsize=(2,5))
# x=[ml[1],fm[1]]
# y=[15,5]
# colors=['lightblue','pink']
# plt.bar(x,y,width=0.8,color=colors,linestyle='dotted',lw=2,label='HIGH')
# #plt.title()
# plt.legend()
# #plt.savefig('sex.png',dpi=1200)
# plt.show()




# p=[44,33,54,43,33,33,33,31]
# pp=0
# for x in p:
#     if x>=32:
#         pp+=1

# print(pp)
# if pp==8:
#     print('pass')
# else:
#     print('failed')
def datelb():
    import datetime
    print(datetime.datetime.now().strftime("%Y-%B-%d"))
datelb()