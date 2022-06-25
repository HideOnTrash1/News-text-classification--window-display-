import pickle
import tkinter
from tkinter import Label, Text, END, Tk, Button, Menu
import tkinter.messagebox
import pymysql
import tkinter as tk
tfid_model_file='E:\python代码\整合\output\model.pkl'
with open(tfid_model_file, 'rb') as infile:
    tfid_predict= pickle.load(infile)
dbconn = pymysql.connect(
    host="localhost",
    database="test",
    user="root",
    password="123456",
    port=3306,
    charset='utf8'
)
cursor = dbconn.cursor()
root=Tk()
root.title("文本分类")
#顶级菜单
menubar=Menu(root)
root.config(menu = menubar)

sw = root.winfo_screenwidth()
#得到屏幕宽度
sh = root.winfo_screenheight()
#得到屏幕高度
ww = 500
wh = 300
x = (sw-ww) / 2
y = (sh-wh) / 2-50
root.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
# root.iconbitmap('tb.ico')
lb2=Label(root,text="输入内容")
lb2.place(relx=0, rely=0.03)
txt = Text(root,font=("宋体",10))
txt.place(rely=0.45, relheight=0.5,relwidth=1)
inp1 = Text(root, height=10, width=65,font=("宋体",10))
inp1.place(relx=0, rely=0.1, relwidth=1, relheight=0.2)
lb3=Label(root,text="最近五天的新闻")
lb3.place(relx=0, rely=0.3)
newsmenu = tk.Menu(menubar,tearoff = False)

def run1():

    a = inp1.get('0.0',(END))
    y = tfid_predict['lr'].predict(tfid_predict['tfidf'].transform([a]))
    result = tkinter.messagebox.askokcancel(title='标题~', message=y)

    # txt.delete("0.0",END)
    # a = inp1.get('0.0',(END))
    # y = tfid_predict['lr'].predict(tfid_predict['tfidf'].transform([a]))
    # txt.insert(END, y)   # 追加显示运算结果
# def button1(event):
def run2():
    txt.delete("0.0", END)
    sqlcmd = "select 内容 from 新闻 where 标签 ='财经' and DATEDIFF(now(),时间) <= 5 order by rand() limit 1"
    cursor.execute(sqlcmd)
    rr = cursor.fetchall()
    txt.insert(END,rr)
def run3():
    txt.delete("0.0", END)
    sqlcmd = "select 内容 from 新闻 where 标签 ='军事' and DATEDIFF(now(),时间) <= 5 order by rand() limit 1"
    cursor.execute(sqlcmd)
    rr = cursor.fetchall()
    txt.insert(END, rr)
def run4():
    txt.delete("0.0", END)
    sqlcmd = "select 内容 from 新闻 where 标签 ='游戏' and DATEDIFF(now(),时间) <= 5 order by rand() limit 1"
    cursor.execute(sqlcmd)
    rr = cursor.fetchall()
    txt.insert(END, rr)
def run5():
    txt.delete("0.0", END)
    sqlcmd = "select 内容 from 新闻 where 标签 ='房产' and DATEDIFF(now(),时间) <= 5 order by rand() limit 1"
    cursor.execute(sqlcmd)
    rr = cursor.fetchall()
    txt.insert(END, rr)
def run6():
    txt.delete("0.0", END)
    sqlcmd = "select 内容 from 新闻 where 标签 ='娱乐' and DATEDIFF(now(),时间) <= 5 order by rand() limit 1"
    cursor.execute(sqlcmd)
    rr = cursor.fetchall()
    txt.insert(END, rr)
def run7():
    txt.delete("0.0", END)
    sqlcmd = "select 内容 from 新闻 where 标签 ='汽车' and DATEDIFF(now(),时间) <= 5 order by rand() limit 1"
    cursor.execute(sqlcmd)
    rr = cursor.fetchall()
    txt.insert(END, rr)

def run8():
    txt.delete("0.0", END)
    sqlcmd = "select 内容 from 新闻 where 标签 ='体育' and DATEDIFF(now(),时间) <= 5 order by rand() limit 1"
    cursor.execute(sqlcmd)
    rr = cursor.fetchall()
    txt.insert(END, rr)
def run9():
    a = inp1.get('0.0', (END))
    y = tfid_predict['lr'].predict(tfid_predict['tfidf'].transform([a]))
    result = tkinter.messagebox.askokcancel(title='是否保存', message=y[0])
    if(result == 1):
        sql_insert = "INSERT INTO 新闻(内容,标签) values(%s,%s)"
        row = cursor.execute(sql_insert, (a.replace('\n', '').replace('\r', ''), y[0]))
        dbconn.commit()
        inp1.delete()

#下拉菜单新闻
newsmenu.add_command(label = "财经",command= run2)
newsmenu.add_command(label = "军事",command= run3)
newsmenu.add_command(label = "游戏",command= run4)
newsmenu.add_command(label = "房产",command= run5)
newsmenu.add_command(label = "娱乐",command= run6)
newsmenu.add_command(label = "汽车",command= run7)
newsmenu.add_command(label = "体育",command= run8)

menubar.add_cascade(label = "新闻",menu = newsmenu)
menubar.add_command(label="分析",command=run1)
menubar.add_command(label="保存",command=run8)

# button1(1)
root.mainloop()
