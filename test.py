#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tkinter import *
from tkinter import messagebox


def closeallwindow():
    window.destroy()

def love1():
    btn2.pack_forget()
    label1 = Label(window, text="猫猫睁开了眼睛还想要摸摸", font=("华文行楷", 16), fg="black")
    label1.grid(row=0, column=0)
    label2 = Label(window, text="　　　　　　 ＿ ＿" +
                                "\n　　　　　／＞　　フ" +
                                "\n　　　　　|  　o　 o |" +
                                "\n　 　　　／` ミ＿3ノ" +
                                "\n　　 　 /　　　 　 |" +
                                "\n　　　 /　 ヽ　　 ﾉ" +
                                "\n　  __│　　|　|　|" +
                                "\n　／ __|　　 |　|　|" +
                                "\n　| (  ヽ＿ _ヽ_)__)" +
                                "\n　＼__つ", font=("等线", 14))
    # label2.grid(row=1, column=0, sticky=E)
    label2.grid(row=1, columnspan=2)
    btn3 = Button(window, text="摸摸", width=15, height=2, command=love)
    btn3.grid(row=3, column=0, sticky=W)


def love():
    label1 = Label(window, text="猫猫感到非常满意 再见(喵呜~)", font=("华文行楷", 16), fg="black")
    label1.grid(row=0, column=0)
    label2 = Label(window, text="　　　　　　 ＿ ＿" +
                                "\n　　　　　／＞　　フ" +
                                "\n　　　　　|  　^　 ^ |" +
                                "\n　 　　　／` ミ＿~ノ" +
                                "\n　　 　 /　　　 　 |" +
                                "\n　　　 /　 ヽ　　 ﾉ" +
                                "\n　  __│　　|　|　|" +
                                "\n　／ __|　　 |　|　|" +
                                "\n　| (  ヽ＿ _ヽ_)__)" +
                                "\n　＼__つ", font=("等线", 14))
    # label2.grid(row=1, column=0, sticky=E)
    label2.grid(row=1, columnspan=2)
    btn4 = Button(window, text="再见", width=15, height=2, command=closeallwindow)
    btn4.grid(row=3, column=0, sticky=W)

    btn5 = Button(window, text="下次再摸", width=15, height=2, command=closeallwindow)
    btn5.grid(row=3, column=1, sticky=E)


def noLove():
    no_love = Toplevel(window)
    no_love.geometry("300x100+610+260")
    no_love.title("喵喵喵")

    label = Label(no_love, text="再考虑考虑呗", font=("华文行楷", 25))
    label.pack()

    btn = Button( no_love, text="好吧", width=10, height=2, command=no_love.destroy)
    btn.pack()

    no_love.protocol("WM_DELETE_WINDOW", closeNoLove)


def closeNoLove():
    #  messagebox.showinfo("不喜欢我，你就关不掉")
    messagebox.showinfo(title="警告",message="不摸我，你就关不掉")
    noLove()


window =Tk()
window.title("猫猫")
window.geometry("420x300+590+230")
window.protocol("WM_DELETE_WINDOW",closeallwindow)

label1 =Label(window,text="你愿意摸摸这只猫咪吗？",font=("华文行楷",16),fg="black")
label1.grid(row=0, column=0)
label2 = Label(window, text="　　　　　　 ＿ ＿" +
"\n　　　　　／＞　　フ"+
"\n　　　　　|  　-　 - |" +
"\n　 　　　／` ミ＿꒳ノ"+
"\n　　 　 /　　　 　 |"+
"\n　　　 /　 ヽ　　 ﾉ"+
"\n　  __│　　|　|　|"+
"\n　／ __|　　 |　|　|"+
"\n　| (  ヽ＿ _ヽ_)__)"+
"\n　＼__つ", font=("等线", 14))
# label2.grid(row=1, column=0, sticky=E)
label2.grid(row=1, columnspan=2)

# photo = PhotoImage(file="cc.png")
# imageLable = Label(window, image=photo)
# imageLable.grid(row=2, columnspan=2)


btn1 = Button(window, text="摸摸", width=15, height=2, command=love1)
btn1.grid(row=3, column=0, sticky=W)

btn2 =Button(window,text="不愿意",width=15,height=2,command=noLove)
btn2.grid(row=3,column=1,sticky=E)
window.mainloop()