from re import I
import re
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from sqlite3 import Error
import datetime
from setuptools import Command

def create_window():
    main = Tk()
    # Import all image into Program
    
    main.title("BoardGame Cafe")
    main.geometry("1100x700")
    main.resizable(False, False)
    main.config(bg = "#f8f4f2" )
    return main
    
def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('db/boardgame403.db')
    cursor = conn.cursor()

def out_Frame(a):
    a.destroy()

def out_Frame2(a):
    a.destroy()
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", bd=0, font="Tahoma 12 ",fieldbackground = "#ffc9ab",background = "ffc9ab",foreground = "black")
    style.configure("Treeview.Heading", font=(None, 15),background="#d87847")
    style.map('Treeview',background = [('selected','#d87847')])
    
def jumpto(a,b):
    a.destroy()
    b

def login_window():
    global user_entry
    global pwd_entry
    login_frame = Frame(window,height=700,width=1100)
    login_frame.place(x=0,y=0)

    # Create Labellogin
    Label(login_frame,image=bglogin).place(x=-2,y=-2)
    Label(login_frame,text="ชื่อผู้ใช้",font="Tahoma 27",bg="#f5cdb5",fg="#d4292e").place(x=649,y=147,relwidth=0.358)
    Label(login_frame,text="รหัสผ่าน",font="Tahoma 27",bg="#f5cdb5",fg="#d4292e").place(x=649,y=307,relwidth=0.358)

    # Create Entry
    user_entry = Entry(login_frame,bg="#ffffff",font="Tahoma 17",bd=0,justify=CENTER, textvariable=user_login)
    user_entry.place(x=683,y=230,relheight=0.06,relwidth=0.305)
    pwd_entry = Entry(login_frame,bg="#ffffff",show='*',font="Tahoma 17",bd=0,justify=CENTER, textvariable=password_login)
    pwd_entry.place(x=683,y=385,relheight=0.06,relwidth=0.305)
    
    # Create Button
    Button(login_frame,text='เข้าสู่ระบบ',bg="#e91a20",fg="#fae4e5",font="Tahoma 28",activebackground="#e91a20",height=1,width=11,bd=0,command=login_Employer).place(x=740,y=487)


def login_Employer():
    global resultO
    if  user_login.get() == "" :
        messagebox.showwarning("แจ้งเตือน","กรุณากรอกชื่อผู้ใช้!")
        user_entry.focus_force()
    else :
        sql = "select * from Employee where username=?"
        cursor.execute(sql,[user_login.get()])
        resultO = cursor.fetchall()
        if resultO :
            if password_login.get() == "" :
                messagebox.showwarning("แจ้งเตือน","กรุณากรอกรหัสผ่าน!")
                pwd_entry.focus_force()
            else :
                sql = "select * from Employee where username=? AND password=? "
                cursor.execute(sql,[user_login.get(),password_login.get()])
                resultO = cursor.fetchall()
                if resultO:
                    messagebox.showinfo("ระบบ","เข้าสู่ระบบสำเร็จ")
                    if  resultO[0][4] == "owner" :
                        adminmenu_window()
                        user_entry.delete(0, END)
                        pwd_entry.delete(0, END)
                        user_entry.focus_force()
                    else :
                        usermenu_window()
                        user_entry.delete(0, END)
                        pwd_entry.delete(0, END)
                        user_entry.focus_force()
                else :
                    messagebox.showwarning("แจ้งเตือน","ชื่อผู้ใช้ หรือ รหัสผ่านไม่ถูกต้อง")
                    pwd_entry.focus_force()
        else :
            messagebox.showwarning("แจ้งเตือน","ชื่อผู้ใช้ หรือ รหัสผ่านไม่ถูกต้อง")

def usermenu_window():

    user_frame = Frame(window,height=700,width=1100)
    user_frame.place(x=0,y=0)

        # Create Labellogin
    Label(user_frame,image=bgstorefront).place(x=-2,y=-2)
    
        # Create Button
    Button(user_frame,image=iconrent,text='การเช่า',bg="#ffffff",font="Tahoma 27",activebackground="#ffffff",activeforeground="#ff0000",compound=TOP,height=320,width=300,bd=0,command=tables_window).place(x=142,y=205)
    Button(user_frame,image=iconsell,text='การขาย',command=Store_Food,bg="#ffffff",font="Tahoma 27",activebackground="#ffffff",activeforeground="#ff0000",compound=TOP,height=320,width=310,bd=0).place(x=660,y=205)
    Button(user_frame,image=iconback,bg="#ece1db",activebackground="#ece1db",height=65,width=65,bd=0,command=logout).place(x=28,y=612)

def logout():
    confirm_yesno = messagebox.askquestion(title='แจ้งเตือน',message="คุณต้องการออกจากระบบ")
    if confirm_yesno == "yes" :
        login_window()

def adminmenu_window():
    login_frame = Frame(window,height=700,width=1100)
    login_frame.place(x=0,y=0)  

    # Create Labellogin
    Label(login_frame,image=bgadminmenu).place(x=-2,y=-2)

    # Create Button
    Button(login_frame,image=iconstore,text='ระบบหน้าร้าน',bg="#ffffff",font="Tahoma 27",command=usermenu_admin_window,activebackground="#ffffff",activeforeground="#ff0000",compound=TOP,height=320,width=300,bd=0).place(x=142,y=205)
    Button(login_frame,image=iconoffice,text='ระบบหลังร้าน',bg="#ffffff",font="Tahoma 27",command=back_office_system,activebackground="#ffffff",activeforeground="#ff0000",compound=TOP,height=320,width=310,bd=0).place(x=660,y=205)
    Button(login_frame,image=iconback,bg="#ece1db",activebackground="#ece1db",height=65,width=65,bd=0,command=logout).place(x=28,y=612)


def usermenu_admin_window():

    user_frame = Frame(window,height=700,width=1100)
    user_frame.place(x=0,y=0)

        # Create Labellogin
    Label(user_frame,image=bgstorefront).place(x=-2,y=-2)

        # Create Button
    Button(user_frame,image=iconrent,text='การเช่า',bg="#ffffff",font="Tahoma 27",activebackground="#ffffff",activeforeground="#ff0000",compound=TOP,height=320,width=300,bd=0,command=tables_window).place(x=142,y=205)
    Button(user_frame,image=iconsell,text='การขาย',command=Store_Food,bg="#ffffff",font="Tahoma 27",activebackground="#ffffff",activeforeground="#ff0000",compound=TOP,height=320,width=310,bd=0).place(x=660,y=205)
    Button(user_frame,image=iconback,bg="#ece1db",activebackground="#ece1db",height=65,width=65,bd=0,command=lambda:jumpto(user_frame,adminmenu_window())).place(x=28,y=612)

def back_office_system():

    back_office_frame = Frame(window,height=700,width=1100)
    back_office_frame.place(x=0,y=0)

    # Create Labellogin
    Label(back_office_frame,image=bgbackendmenu).place(x=-2,y=-2)

    # Create Button
    Button(back_office_frame,text='รายงานสรุปรายได้',bg="#ffffff",font="Tahoma 12",command=Report_Income_Boardgame,activebackground="#ffffff",activeforeground="#ff0000",compound=TOP,height=3,width=24,bd=0).place(x=184,y=200)
    Button(back_office_frame,text='รายงานสรุปบอร์ดเกม',bg="#ffffff",font="Tahoma 12",command=Report_Store_Boardgame,activebackground="#ffffff",activeforeground="#ff0000",compound=TOP,height=3,width=24,bd=0).place(x=184,y=360)
    Button(back_office_frame,text='รายงานสรุปรายได้เฉลี่ย',bg="#ffffff",command=Report_amount_Boardgame,font="Tahoma 12",activebackground="#ffffff",activeforeground="#ff0000",compound=TOP,height=3,width=24,bd=0).place(x=184,y=512)
    Button(back_office_frame,text='การลงทะเบียนผู้ใช้',bg="#ffffff",font="Tahoma 12",activebackground="#ffffff",command=user_window,activeforeground="#ff0000",compound=TOP,height=3,width=24,bd=0).place(x=698,y=200)
    Button(back_office_frame,text='การลงทะเบียนสมัครสมาชิก',bg="#ffffff",font="Tahoma 12",activebackground="#ffffff",command=member_window,activeforeground="#ff0000",compound=TOP,height=3,width=24,bd=0).place(x=698,y=310)
    Button(back_office_frame,text='การลงทะเบียนบอร์ดเกม',bg="#ffffff",font="Tahoma 12",activebackground="#ffffff",command=boardgame_registation,activeforeground="#ff0000",compound=TOP,height=3,width=24,bd=0).place(x=699,y=422)
    Button(back_office_frame,text='การลงทะเบียนสินค้า',bg="#ffffff",font="Tahoma 12",command=product_window,activebackground="#ffffff",activeforeground="#ff0000",compound=TOP,height=3,width=24,bd=0).place(x=699,y=530)
    Button(back_office_frame,image=iconback,bg="#ece1db",activebackground="#ece1db",height=65,width=65,bd=0,command=lambda:jumpto(back_office_frame,adminmenu_window())).place(x=28,y=617)

def add_data():
    # Access Database   
    cursor.execute("SELECT * FROM Boardgame")
    result = cursor.fetchall()

    # Add data from Database to list
    for i,data in enumerate(result):
        IDstocklst.append(data[0])
        namestock_lst.append(data[1])
        playamt_lst.append(int(data[2]))
        saleamt_lst.append(int(data[3]))
        takeprice_lst.append(int(data[4]))
        saleprice_lst.append(int(data[5]))

def user_window():
    global cursor,conn,mytree_userr,search
    user_frame = Frame(window,height=700,width=1100)
    user_frame.place(x=0,y=0)

    def treeviewclick(event) :
        global   values     
        values = mytree_userr.item(mytree_userr.focus(),'values')
        conn = sqlite3.connect('db/boardgame403.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM Employee"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result = cursor.fetchall()
        edit_employ_window()
        for i,data in enumerate(result):
            if data[0] == values[0]:
                lo=0
                if data[4] == "staff":
                    lo=1
                name_entry.insert(0,data[0])   
                surname_entry.insert(0,data[1])
                nickname_entry.insert(0,data[2])
                telephone_entry.insert(0,data[3])
                national_entry.insert(0,data[7])
                rank_Combo.current(lo)
                id_entry.insert(0,data[5])
        
    def searchm():
        # Reset Medical Stock Display
        mytree_userr.delete(*mytree_userr.get_children())
        sql = "SELECT * FROM Employee"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result_member = cursor.fetchall()
        
        for i, data in enumerate(result_member):   
            if (search.get().lower() in data[0].lower() or search.get().lower() in data[1].lower() or search.get().lower() in data[2].lower() or search.get().lower() in data[3].lower()  ):
                mytree_userr.insert('', 'end', values=(data[0],data[1], data[2], data[3]))

    def removem() :
        yn = messagebox.askquestion(title='แจ้งเตือน',message="คุณต้องการลบหรือไม่")
        if yn == "yes" :
            deleterow = mytree_userr.selection()
            values = mytree_userr.item(mytree_userr.focus(),'values')
            mytree_userr.delete(deleterow)
            sql = "DELETE FROM Employee WHERE em_fname=?"
            cursor.execute(sql,[values[0]])
            conn.commit()
            messagebox.showinfo("ระบบ","การลบสำเร็จ")

    def eedit():
        if not name_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not surname_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not nickname_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif len(telephone_entry.get())!=10:
            if len(telephone_entry.get())<10:
                messagebox.showinfo(title='ระบบ', message='กรุณากรอกหมายเลขโทรศัพท์ให้ครบ 10 หลัก')
            else:
                messagebox.showinfo(title='ระบบ', message='หมายเลขโทรศัพท์เกินมากกว่า 10 หลัก')

        elif len(national_entry.get())!=13:
            if len(telephone_entry.get())<10:
                messagebox.showinfo(title='ระบบ', message='กรุณากรอกหมายเลขประจำตัวประชาชนให้ครบ 13 หลัก')
            else:
                messagebox.showinfo(title='ระบบ', message='หมายเลขประจำตัวประชาชนเกินมากกว่า 13 หลัก')

        elif not rank_Combo.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not id_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not password_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not confirm_password_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')
            
        else:
            if password_entry.get() == confirm_password_entry.get():
                messagebox.showinfo('ระบบ','รหัสผ่านของคุณเปลี่ยนเรียบร้อยแล้ว')
                mytree_userr.item('',text='',values=(name_entry.get(),surname_entry.get(),nickname_entry.get(),telephone_entry.get(),national_entry.get(),rank_Combo.get(),id_entry.get(),password_entry.get()))
                sql = '''
                    update Employee
                    set em_fname = ?, em_lname = ?, em_nname = ?, em_tel = ?, id = ?, position = ?, username = ?, password = ?
                    where em_fname = ?

                '''
                cursor.execute(sql,[name_entry.get(),surname_entry.get(),nickname_entry.get(),telephone_entry.get(),national_entry.get(),rank_Combo.get(),id_entry.get(),password_entry.get(),values[0]])
                conn.commit()
                messagebox.showinfo("ระบบ","ลงทะเบียนสำเร็จ")
                edit_employ_frame.destroy()
                user_frame.destroy()
                user_window()
                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview", bd=0, font="Tahoma 12 ",fieldbackground = "#ffc9ab",background = "ffc9ab",foreground = "black")
                style.configure("Treeview.Heading", font=(None, 15),background="#d87847")
                style.map('Treeview',background = [('selected','#d87847')])

            else :
                messagebox.showinfo(title='ระบบ', message='รหัสผ่านไม่ตรงกับรหัสผ่านที่ยืนยัน')

                password_entry.delete(0,END)
                confirm_password_entry.delete(0,END)

    def addm() :
        if not name_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not surname_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not nickname_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif len(telephone_entry.get())!=10:
            if len(telephone_entry.get())<10:
                messagebox.showinfo(title='ระบบ', message='กรุณากรอกหมายเลขโทรศัพท์ให้ครบ 10 หลัก')
            else:
                messagebox.showinfo(title='ระบบ', message='หมายเลขโทรศัพท์เกินมากกว่า 10 หลัก')

        elif len(national_entry.get())!=13:
            if len(telephone_entry.get())<10:
                messagebox.showinfo(title='ระบบ', message='กรุณากรอกหมายเลขประจำตัวประชาชนให้ครบ 13 หลัก')
            else:
                messagebox.showinfo(title='ระบบ', message='หมายเลขประจำตัวประชาชนเกินมากกว่า 13 หลัก')

        elif not rank_Combo.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not id_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not password_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not confirm_password_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')
            
        else:
            if password_entry.get() == confirm_password_entry.get():
                messagebox.showinfo('ระบบ','รหัสผ่านของคุณเปลี่ยนเรียบร้อยแล้ว')
                mytree_userr.insert('',index='end',values=(name_entry.get(),surname_entry.get(),nickname_entry.get(),telephone_entry.get(),national_entry.get(),rank_Combo.get(),id_entry.get(),password_entry.get()))
                curr = conn.cursor()
                curr.execute("INSERT INTO Employee (em_fname,em_lname,em_nname,em_tel,id,position,username,password) VALUES (?,?,?,?,?,?,?,?)",(name_entry.get(),surname_entry.get(),nickname_entry.get(),telephone_entry.get(),national_entry.get(),rank_Combo.get(),id_entry.get(),password_entry.get()))
                conn.commit()
                messagebox.showinfo("ระบบ","ลงทะเบียนสำเร็จ")
                add_employ_frame.destroy()


                style = ttk.Style()
                style.theme_use("default")
                style.configure("Treeview", bd=0, font="Tahoma 12 ",fieldbackground = "#ffc9ab",background = "ffc9ab",foreground = "black")
                style.configure("Treeview.Heading", font=(None, 15),background="#d87847")
                style.map('Treeview',background = [('selected','#d87847')])

            else :
                messagebox.showinfo(title='ระบบ', message='รหัสผ่านไม่ตรงกับรหัสผ่านที่ยืนยัน')

                password_entry.delete(0,END)
                confirm_password_entry.delete(0,END)   

    def add_employ_window():
        global name_entry,surname_entry,nickname_entry,telephone_entry,national_entry,rank_Combo,id_entry,password_entry,confirm_password_entry,add_employ_frame
        add_employ_frame = Frame(window,height=700,width=1100)
        add_employ_frame.place(x=0,y=0)
        
        # Create Labellogin
        Label(add_employ_frame,image=bgaddemploy).place(x=-2,y=-2)

        # Create Entry
        name_entry = Entry(add_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        name_entry.place(x=291,y=143,relheight=0.05,relwidth=0.230)
        surname_entry = Entry(add_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        surname_entry.place(x=291,y=234,relheight=0.05,relwidth=0.230)
        nickname_entry = Entry(add_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        nickname_entry.place(x=291,y=317,relheight=0.05,relwidth=0.230)
        telephone_entry = Entry(add_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        telephone_entry.place(x=291,y=400,relheight=0.05,relwidth=0.230)
        national_entry = Entry(add_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        national_entry.place(x=291,y=485,relheight=0.05,relwidth=0.230)
        id_entry = Entry(add_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        id_entry.place(x=832,y=234,relheight=0.05,relwidth=0.230)
        password_entry = Entry(add_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        password_entry.place(x=832,y=317,relheight=0.05,relwidth=0.230)
        confirm_password_entry = Entry(add_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        confirm_password_entry.place(x=832,y=400,relheight=0.05,relwidth=0.230)
        
        # Define the style for combobox widget
        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground= "#e8986c",state='readonly')
        
        rank_Combo = ttk.Combobox(add_employ_frame, values=datelst,font="Tahoma 17",)
        rank_Combo.place(x=831,y=143,relheight=0.05,relwidth=0.231)

        Button(add_employ_frame,image=iconback,bg="#ece1db",activebackground="#ece1db",command=lambda:out_Frame2(add_employ_frame),height=65,width=65,bd=0).place(x=28,y=612)
        Button(add_employ_frame,image=iconadd,bg="#ece1db",activebackground="#ece1db",command=addm,height=72,width=187,bd=0).place(x=868,y=612)
        
    def edit_employ_window():
        global name_entry,surname_entry,nickname_entry,telephone_entry,national_entry,rank_Combo,id_entry,password_entry,confirm_password_entry,edit_employ_frame
        edit_employ_frame = Frame(window,height=700,width=1100)
        edit_employ_frame.place(x=0,y=0)
        
        # Create Labellogin
        Label(edit_employ_frame,image=bgeditemploy).place(x=-2,y=-2)
        # Create Entry
        name_entry = Entry(edit_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        name_entry.place(x=291,y=143,relheight=0.05,relwidth=0.230)
        surname_entry = Entry(edit_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        surname_entry.place(x=291,y=234,relheight=0.05,relwidth=0.230)
        nickname_entry = Entry(edit_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        nickname_entry.place(x=291,y=317,relheight=0.05,relwidth=0.230)
        telephone_entry = Entry(edit_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        telephone_entry.place(x=291,y=400,relheight=0.05,relwidth=0.230)
        national_entry = Entry(edit_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        national_entry.place(x=291,y=485,relheight=0.05,relwidth=0.230)
        id_entry = Entry(edit_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        id_entry.place(x=832,y=234,relheight=0.05,relwidth=0.230)
        password_entry = Entry(edit_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        password_entry.place(x=832,y=317,relheight=0.05,relwidth=0.230)
        confirm_password_entry = Entry(edit_employ_frame,bg="#e8986c",font="Tahoma 17",bd=0,justify=CENTER)
        confirm_password_entry.place(x=832,y=400,relheight=0.05,relwidth=0.230)
        
        # Define the style for combobox widget
        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground= "#e8986c",state='readonly')
        
        rank_Combo = ttk.Combobox(edit_employ_frame, values=datelst,font="Tahoma 17",)
        rank_Combo.place(x=831,y=143,relheight=0.05,relwidth=0.231)

        Button(edit_employ_frame,image=iconback,bg="#ece1db",activebackground="#ece1db",command=lambda:out_Frame2(edit_employ_frame),height=65,width=65,bd=0).place(x=28,y=612)
        Button(edit_employ_frame,image=iconedit,bg="#ece1db",activebackground="#ece1db",command=eedit,height=72,width=187,bd=0).place(x=868,y=612)

    # Create Labellogin
    Label(user_frame,image=bguserregist).place(x=-2,y=-2)
    Label(user_frame,text="การลงทะเบียนผู้ใช้",font="Tahoma 20",bg="#ece1db").place(x=360,y=56)

    #Treeview
    treeframe_user = Frame(user_frame,height=390,width=740,bg="black")
    treeframe_user.place(x=325,y=130)
    treebar = Scrollbar(treeframe_user)
    treebar.pack(side=RIGHT,fill=Y)
    mytree_userr = ttk.Treeview(treeframe_user,columns=("name","surnname","nickname","phone"),height=16,yscrollcommand=treebar.set)
    mytree_userr.pack()
    #สี
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", bd=0, font="Tahoma 12 ",fieldbackground = "#ffc9ab",background = "ffc9ab",foreground = "black")
    style.configure("Treeview.Heading", font=(None, 15),background="#d87847")
    style.map('Treeview',background = [('selected','#d87847')])
        
    treebar.config(command=mytree_userr.yview)
    #create headings
    mytree_userr.heading("#0",text="",anchor=W)
    mytree_userr.heading("name",text="ชื่อ",anchor=CENTER)
    mytree_userr.heading("surnname",text="นามสกุล",anchor=CENTER)
    mytree_userr.heading("nickname",text="ชื่อเล่น",anchor=CENTER)
    mytree_userr.heading("phone",text="เบอร์โทรศัพท์",anchor=CENTER)
    #Format our columns
    mytree_userr.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    mytree_userr.column("name",anchor=W,width=200)
    mytree_userr.column("surnname",anchor=W,width=200)
    mytree_userr.column("nickname",anchor=W,width=170)
    mytree_userr.column("phone",anchor=W,width=170)

    mytree_userr.delete(*mytree_userr.get_children()) #delete old data from treeview
    conn = sqlite3.connect('db/boardgame403.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM Employee"
    cursor.execute(sql)# ORDER BY firstname ASC")
    result = cursor.fetchall()
    for i,data in enumerate(result):
        mytree_userr.insert('', 'end', values=(data[0],data[1], data[2], data[3]))


    mytree_userr.bind('<Double-1>',treeviewclick)

    Button(user_frame,text='การลงทะเบียนผู้ใช้',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=73)
    Button(user_frame,text='การลงทะเบียนสมัครสมาชิก',bg="#ffffff",font="Tahoma 12",command=lambda:jumpto(user_frame,member_window()),activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=190)
    Button(user_frame,text='การลงทะเบียนบอร์ดเกม',bg="#ffffff",font="Tahoma 12",command=lambda:jumpto(user_frame,boardgame_registation()),activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=308)
    Button(user_frame,text='การลงทะเบียนสินค้า',bg="#ffffff",font="Tahoma 12",command=lambda:jumpto(user_frame,product_window()),activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=425)
    Button(user_frame,text='ย้อนกลับ',bg="#ffffff",font="Tahoma 20",activebackground="#fff7f3",command=lambda:out_Frame(user_frame),activeforeground="#fff7f3",compound=TOP,bd=0).place(x=34,y=543,relheight=0.099,relwidth=0.202)
    Button(user_frame,text='ลบ',bg="#ffffff",font="Tahoma 20",activebackground="#fff7f3",command=removem,activeforeground="red",compound=TOP,bd=0).place(x=457,y=543,relheight=0.08,relwidth=0.170)
    Button(user_frame,text='เพิ่ม',bg="#ffffff",font="Tahoma 20",activebackground="#fff7f3",command=add_employ_window,activeforeground="red",compound=TOP,bd=0).place(x=776,y=543,relheight=0.080,relwidth=0.170)
    Button(user_frame,image=iconserch,activebackground="#fff7f3",activeforeground="#fff7f3",command=searchm,compound=TOP,bd=0).place(x=1030,y=54)
    search = Entry(user_frame,bg="#f09968",font="Tahoma 17",bd=0,justify=CENTER)
    search.place(x=810,y=56,relheight=0.069,relwidth=0.200)

    
def member_window():
    global search_member,result_member
    member_frame = Frame(window,height=700,width=1100)
    member_frame.place(x=0,y=0)
    
    def treeviewclick(event) :
            global   values
            # Delete Exist Information in Entry
            name_entry.delete(0,END)
            sname_entry.delete(0,END)
            nname_entry.delete(0,END)
            phone_entry.delete(0,END)

            values = mytree_member.item(mytree_member.focus(),'values')

        
            # Insert Select Information into Entry
            name_entry.insert(0,values[0])   
            sname_entry.insert(0,values[1])
            nname_entry.insert(0,values[2])
            phone_entry.insert(0,values[3])
            
    def searchm():

        # Reset Medical Stock Display
        mytree_member.delete(*mytree_member.get_children())
        sql = "SELECT * FROM Member"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result_member = cursor.fetchall()

        for i, data in enumerate(result_member):
            n=data[0]
            if (search_member.get().lower() in n.lower() or search_member.get().lower() in data[1].lower() or search_member.get().lower() in data[2].lower() or search_member.get().lower() in data[3].lower() or search_member.get().lower() in data[4]):
                mytree_member.insert('', 'end', values=(data[0],data[1], data[2], data[3], data[4],data[5]))

    def addm() :
        if not name_entry.get():
            messagebox.showinfo(title='', message='กรุณากรอกทั้งหมด')

        elif not sname_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not nname_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not phone_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif len(phone_entry.get())!=10:
            
            if len(phone_entry.get())<10:
                messagebox.showinfo(title='ระบบ', message='กรุณากรอกหมายเลขโทรศัพท์ให้ครบ 10 หลัก')
            else:
                messagebox.showinfo(title='ระบบ', message='กรอกหมายเลขโทรศัพท์เกินมากกว่า 10 หลัก')
        else:
            now = datetime.datetime.now()
            date = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
            
            exp= str(now.day)+"/"+str(now.month)+"/"+str(now.year+1)

            mytree_member.insert('',index='end',values=(name_entry.get(),sname_entry.get(),nname_entry.get(),phone_entry.get(),date,exp))
            curr = conn.cursor()
            curr.execute("INSERT INTO Member (mb_fname,mb_lname,mb_nname,mb_tel,app_date,exp_date) VALUES (?,?,?,?,?,?)",(name_entry.get(),sname_entry.get(),nname_entry.get(),phone_entry.get(),date,exp))
            conn.commit()
            messagebox.showinfo("ระบบ","ลงทะเบียนสำเร็จ")

            

            name_entry.delete(0,END)
            sname_entry.delete(0,END)
            nname_entry.delete(0,END)
            phone_entry.delete(0,END)
        
    def updatem():
        if not name_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not sname_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not nname_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not phone_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif len(phone_entry.get())!=10:
            
            if len(phone_entry.get())<10:
                messagebox.showinfo(title='ระบบ', message='กรุณากรอกหมายเลขโทรศัพท์ให้ครบ 10 หลัก')
            else:
                messagebox.showinfo(title='ระบบ', message='กรอกหมายเลขโทรศัพท์เกินมากกว่า 10 หลัก')
     
        else :
            selected =mytree_member.focus()
            mytree_member.item(selected,text="",values=(name_entry.get(),sname_entry.get(),nname_entry.get(),phone_entry.get(),values[4],values[5]))
            sql = '''
                update Member
                set mb_fname=?,mb_lname=?,mb_nname=?,mb_tel=?
                where mb_fname=? 

            '''
            cursor.execute(sql,[name_entry.get(),sname_entry.get(),nname_entry.get(),phone_entry.get(),values[0]])
            conn.commit()



            name_entry.delete(0,END)
            sname_entry.delete(0,END)
            nname_entry.delete(0,END)
            phone_entry.delete(0,END)

    def removem() :
        
        yn = messagebox.askquestion(title='แจ้งเตือน',message="คุณต้องการลบหรือไม่"+name_entry.get())
        if yn == "yes"  :
            deleterow = mytree_member.selection()
            values = mytree_member.item(mytree_member.focus(),'values')
            mytree_member.delete(deleterow)
            sql = "DELETE FROM Member WHERE mb_fname=?"
            cursor.execute(sql,[values[0]])
            conn.commit()
            messagebox.showinfo("ระบบ","ลบ "+name_entry.get()+"สำเร็จ")

            name_entry.delete(0,END)
            sname_entry.delete(0,END)
            nname_entry.delete(0,END)
            phone_entry.delete(0,END)

    def clear_entry():
        name_entry.delete(0,END)
        sname_entry.delete(0,END)
        nname_entry.delete(0,END)
        phone_entry.delete(0,END)

     # Create Labellogin
    Label(member_frame,image=bgmemberregist).place(x=-2,y=-2)
    Label(member_frame,text="ทะเบียนสมาชิก",font="Tahoma 20",bg="#ece1db").place(x=360,y=56)
    Label(member_frame,text="ค้นหา :",font="Tahoma 18",bg="#ece1db").place(x=720,y=58)

    #Treeview
    treeframe = Frame(member_frame,height=390,width=740,bg="black")
    treeframe.place(x=315,y=340)
    treebar = Scrollbar(treeframe)
    treebar.pack(side=RIGHT,fill=Y)
    mytree_member = ttk.Treeview(treeframe,columns=("name","surnname","nickname","phone","appdate","expdate"),height=14,yscrollcommand=treebar.set)
    mytree_member.pack()
    #สี
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", bd=0, font="Tahoma 11 ",fieldbackground = "#ffc9ab",background = "ffc9ab",foreground = "black")
    style.configure("Treeview.Heading", font=(None, 12),background="#d87847")
    style.map('Treeview',background = [('selected','#d87847')])
    
    treebar.config(command=mytree_member.yview)
    #create headings
    mytree_member.heading("#0",text="",anchor=W)
    mytree_member.heading("name",text="ชื่อ",anchor=CENTER)
    mytree_member.heading("surnname",text="นามสกุล",anchor=CENTER)
    mytree_member.heading("nickname",text="ชื่อเล่น",anchor=CENTER)
    mytree_member.heading("phone",text="เบอร์โทร",anchor=CENTER)
    mytree_member.heading("appdate",text="วันที่สมัคร",anchor=CENTER)
    mytree_member.heading("expdate",text="วันที่หมดอายุ",anchor=CENTER)
    #Format our columns
    mytree_member.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    mytree_member.column("name",anchor=W,width=170)
    mytree_member.column("surnname",anchor=W,width=170)
    mytree_member.column("nickname",anchor=W,width=100)
    mytree_member.column("phone",anchor=W,width=100)
    mytree_member.column("appdate",anchor=CENTER,width=100)
    mytree_member.column("expdate",anchor=CENTER,width=100)

    mytree_member.delete(*mytree_member.get_children()) #delete old data from treeview
    conn = sqlite3.connect('db/boardgame403.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM Member"
    cursor.execute(sql)# ORDER BY firstname ASC")
    result_member = cursor.fetchall()
    for i,data in enumerate(result_member):
        mytree_member.insert('', 'end', values=(data[0],data[1], data[2], data[3], data[4], data[5]))

    search_member = Entry(member_frame,bg="#f09968",font="Tahoma 13",bd=0,justify=CENTER)
    search_member.place(x=810,y=60,relheight=0.048,relwidth=0.200)


    Button(member_frame,text='ทะเบียนผู้ใช้',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",command=lambda:jumpto(member_frame,user_window()),activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=73)
    Button(member_frame,text='ทะเบียนสมาชิก',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=190)
    Button(member_frame,text='ทะเบียบอร์ดเกม',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",command=lambda:jumpto(member_frame,boardgame_registation()),activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=308)
    Button(member_frame,text='ทะเบียนสินค้า',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",command=lambda:jumpto(member_frame,product_window()),activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=425)
    Button(member_frame,text='ย้อนกลับ',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",command=lambda:out_Frame(member_frame),activeforeground="#fff7f3",compound=TOP,bd=0).place(x=34,y=543,relheight=0.099,relwidth=0.202)
    Button(member_frame,text='ลบข้อมูล',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="red",compound=TOP,bd=0,command=removem).place(x=339,y=223,relheight=0.060,relwidth=0.128)
    Button(member_frame,text='เพิ่มข้อมูล',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="red",compound=TOP,bd=0,command=addm).place(x=528,y=223,relheight=0.060,relwidth=0.128)
    Button(member_frame,text='แก้ไขข้อมูล',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="red",compound=TOP,bd=0,command=updatem).place(x=717,y=223,relheight=0.060,relwidth=0.128)
    Button(member_frame,text="ยกเลิกข้อมูลที่กรอก",bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="red",compound=TOP,bd=0,command=clear_entry).place(x=906,y=223,relheight=0.060,relwidth=0.128)
    Button(member_frame,image=iconserch,activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,bd=0,command=searchm).place(x=1030,y=60,relheight=0.048,relwidth=0.030)
    mytree_member.bind('<Double-1>',treeviewclick)

    Label(member_frame,text="____________________________________________________________",font="Tahoma 18",bg="#ece1db").place(x=300,y=100)
    Label(member_frame,text="ชื่อ :",font="Tahoma 13",bg="#ece1db").place(x=310,y=150)
    Label(member_frame,text="นามสกุล :",font="Tahoma 13",bg="#ece1db").place(x=495,y=150)
    Label(member_frame,text="ชื่อเล่น :",font="Tahoma 13",bg="#ece1db").place(x=718,y=150)
    Label(member_frame,text="เบอร์โทรศัพท์ :",font="Tahoma 13",bg="#ece1db").place(x=844,y=150)
    Label(member_frame,text="____________________________________________________________",font="Tahoma 18",bg="#ece1db").place(x=300,y=270)

    name_entry = Entry(member_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    name_entry.place(x=350,y=151,relheight=0.04,relwidth=0.130)
    sname_entry = Entry(member_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    sname_entry.place(x=573,y=151,relheight=0.04,relwidth=0.130)
    nname_entry = Entry(member_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    nname_entry.place(x=784,y=151,relheight=0.04,relwidth=0.050)
    phone_entry = Entry(member_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    phone_entry.place(x=958,y=151,relheight=0.04,relwidth=0.100)

def boardgame_registation():
    global conn,cursor,mytree_board,search,name_entry,pyamt_entry,saleamt_entry,tprice_entry,sprice_entry,search_stock,result_board
    bg_reg_frame = Frame(window,height=700,width=1100)
    bg_reg_frame.place(x=0,y=0)
    def treeviewclick(event) :
        global values
        # Delete Exist Information in Entry
        name_entry.delete(0,END)
        pyamt_entry.delete(0,END)
        saleamt_entry.delete(0,END)
        tprice_entry.delete(0,END)
        sprice_entry.delete(0,END)

        values = mytree_board.item(mytree_board.focus(),'values')

        
        # Insert Select Information into Entry
        name_entry.insert(0,values[0])   
        pyamt_entry.insert(0,values[1])
        saleamt_entry.insert(0,values[2])
        tprice_entry.insert(0,values[3])
        sprice_entry.insert(0,values[4])

    def search():
        # Reset Medical Stock Display
        mytree_board.delete(*mytree_board.get_children())
        
        for i, data in enumerate(result_board):
            n=data[1]
            if (search_member.get().lower() in n.lower()):
                mytree_board.insert('', 'end', values=(data[1],data[2], data[3], data[4], data[5]))
       

    def add() :
        if not name_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not pyamt_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not saleamt_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not tprice_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not sprice_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        else:   
            mytree_board.insert('',index='end',values=(name_entry.get(),pyamt_entry.get(),saleamt_entry.get(),tprice_entry.get(),sprice_entry.get()))
            curr = conn.cursor()
            curr.execute("INSERT INTO Boardgame (bgame_name,play_amt,sale_amt,take_price,sale_price) VALUES (?,?,?,?,?)",(name_entry.get(),pyamt_entry.get(),saleamt_entry.get(),tprice_entry.get(),sprice_entry.get()))
            conn.commit()
            messagebox.showinfo("ระบบ","ลงทะเบียนสำเร็จ")

        name_entry.delete(0,END)
        pyamt_entry.delete(0,END)
        saleamt_entry.delete(0,END)
        tprice_entry.delete(0,END)
        sprice_entry.delete(0,END)

    def update():
       
        if not name_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not pyamt_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not saleamt_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not tprice_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not sprice_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')
        
        else :
            selected = mytree_board.focus()
            mytree_board.item(selected,text="",values=(name_entry.get(),pyamt_entry.get(),saleamt_entry.get(),tprice_entry.get(),sprice_entry.get()))
            sql = '''
                update Boardgame
                set bgame_name=? , play_amt=?  , sale_amt=? , take_price=?, sale_price=?
                where bgame_name=?

            '''
            cursor.execute(sql,[name_entry.get(),pyamt_entry.get(),saleamt_entry.get(),tprice_entry.get(),sprice_entry.get(),values[0]])
            conn.commit()
            name_entry.delete(0,END)
            pyamt_entry.delete(0,END)
            saleamt_entry.delete(0,END)
            tprice_entry.delete(0,END)
            sprice_entry.delete(0,END)

    def remove() :
        yn = messagebox.askquestion(title='แจ้งเตือน',message="คุณต้องการลบหรือไม่"+name_entry.get())
        if yn == "yes"  :
            deleterow = mytree_board.selection()
            values = mytree_board.item(mytree_board.focus(),'values')
            mytree_board.delete(deleterow)
            sql = "DELETE FROM Boardgame WHERE bgame_name=?"
            cursor.execute(sql,[values[0]])
            conn.commit()
            messagebox.showinfo("ระบบ","ลบ "+name_entry.get()+"สำเร็จ")
            clear()

    def clear():
        name_entry.delete(0,END)
        pyamt_entry.delete(0,END)
        saleamt_entry.delete(0,END)
        tprice_entry.delete(0,END)
        sprice_entry.delete(0,END)
     # Create Labellogin
    Label(bg_reg_frame,image=bgboardst).place(x=-2,y=-2)
    Label(bg_reg_frame,text="ทะเบียนบอร์ดเกม",font="Tahoma 20",bg="#ece1db").place(x=360,y=56)
    Label(bg_reg_frame,text="ค้นหา :",font="Tahoma 18",bg="#ece1db").place(x=720,y=58)

    #Treeview
    treeframe = Frame(bg_reg_frame,height=390,width=740,bg="black")
    treeframe.place(x=325,y=340)
    treebar = Scrollbar(treeframe)
    treebar.pack(side=RIGHT,fill=Y)
    mytree_board = ttk.Treeview(treeframe,columns=("name","pyamt","saleamt","tprice","sprice"),height=14,yscrollcommand=treebar.set)
    mytree_board.pack()
    #สี
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", bd=0, font="Tahoma 12 ",fieldbackground = "#ffc9ab",background = "ffc9ab",foreground = "black")
    style.configure("Treeview.Heading", font=(None, 12),background="#d87847")
    style.map('Treeview',background = [('selected','#d87847')])
    
    treebar.config(command=mytree_board.yview)
    #create headings
    mytree_board.heading("#0",text="",anchor=W)
    mytree_board.heading("name",text="ชื่อบอร์ดเกม",anchor=CENTER)
    mytree_board.heading("pyamt",text="จำนวนการเล่น ",anchor=CENTER)
    mytree_board.heading("saleamt",text="จำนวนการขาย ",anchor=CENTER)
    mytree_board.heading("tprice",text="ราคาที่ซื้อ",anchor=CENTER)
    mytree_board.heading("sprice",text="ราคาที่ขาย",anchor=CENTER)
    #Format our columns
    mytree_board.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    mytree_board.column("name",anchor=W,width=275)
    mytree_board.column("pyamt",anchor=CENTER,width=120)
    mytree_board.column("saleamt",anchor=CENTER,width=120)
    mytree_board.column("tprice",anchor=CENTER,width=110)
    mytree_board.column("sprice",anchor=CENTER,width=110)

    mytree_board.delete(*mytree_board.get_children()) #delete old data from treeview
    conn = sqlite3.connect('db/boardgame403.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM Boardgame"
    cursor.execute(sql)# ORDER BY firstname ASC")
    result_board = cursor.fetchall()
    for i,data in enumerate(result_board):
        mytree_board.insert('', 'end', values=(data[1],data[2], data[3], data[4], data[5]))

    Button(bg_reg_frame,text='ทะเบียนผู้ใช่',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",command=lambda:jumpto(bg_reg_frame,user_window()),activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=73)
    Button(bg_reg_frame,text='ทะเบียนสมาชิก',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",command=lambda:jumpto(bg_reg_frame,member_window()),activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=190)
    Button(bg_reg_frame,text='ทะเบียนบอร์ดเกม',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=308)
    Button(bg_reg_frame,text='ทะเบียนสินค้า',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",command=lambda:jumpto(bg_reg_frame,product_window()),activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=425)
    Button(bg_reg_frame,text='ย้อนกลับ',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",command=lambda:out_Frame(bg_reg_frame),activeforeground="#fff7f3",compound=TOP,bd=0).place(x=34,y=543,relheight=0.099,relwidth=0.202)
    Button(bg_reg_frame,text='ลบข้อมูล',bg="#ffffff",font="Tahoma 12",command=remove,activebackground="#fff7f3",activeforeground="red",compound=TOP,bd=0).place(x=339,y=223,relheight=0.060,relwidth=0.128)
    Button(bg_reg_frame,text='เพิ่มข้อมูล',bg="#ffffff",font="Tahoma 12",command=add,activebackground="#fff7f3",activeforeground="red",compound=TOP,bd=0).place(x=528,y=223,relheight=0.060,relwidth=0.128)
    Button(bg_reg_frame,text='แก้ไขข้อมูล',bg="#ffffff",font="Tahoma 12",command=update,activebackground="#fff7f3",activeforeground="red",compound=TOP,bd=0).place(x=717,y=223,relheight=0.060,relwidth=0.128)
    Button(bg_reg_frame,text="ยกเลิกข้อมูลที่กรอก",bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="red",compound=TOP,bd=0,command=clear).place(x=906,y=223,relheight=0.060,relwidth=0.128)
    Button(bg_reg_frame,image=iconserch,activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,bd=0,command=search).place(x=1030,y=60,relheight=0.048,relwidth=0.030)

    Label(bg_reg_frame,text="____________________________________________________________",font="Tahoma 18",bg="#ece1db").place(x=300,y=100)
    Label(bg_reg_frame,text="ชื่อบอร์ดเกม :",font="Tahoma 13",bg="#ece1db").place(x=330,y=155)
    Label(bg_reg_frame,text="จำนวนการเล่น :",font="Tahoma 13",bg="#ece1db").place(x=637,y=141)
    Label(bg_reg_frame,text="จำนวนการขาย :",font="Tahoma 13",bg="#ece1db").place(x=635,y=170)
    Label(bg_reg_frame,text=" ราคาที่ซื้อ :",font="Tahoma 13",bg="#ece1db").place(x=851,y=141)
    Label(bg_reg_frame,text="ราคาที่ขาย :",font="Tahoma 13",bg="#ece1db").place(x=850,y=170)
    Label(bg_reg_frame,text="____________________________________________________________",font="Tahoma 18",bg="#ece1db").place(x=300,y=270)

    search_member = Entry(bg_reg_frame,bg="#f09968",font="Tahoma 13",bd=0,justify=CENTER)
    search_member.place(x=810,y=60,relheight=0.048,relwidth=0.200)

    name_entry = Entry(bg_reg_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    name_entry.place(x=435,y=157,relheight=0.04,relwidth=0.150)
    pyamt_entry = Entry(bg_reg_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    pyamt_entry.place(x=755,y=142,relheight=0.04,relwidth=0.050)
    saleamt_entry = Entry(bg_reg_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    saleamt_entry.place(x=755,y=171,relheight=0.04,relwidth=0.050)
    tprice_entry = Entry(bg_reg_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    tprice_entry.place(x=945,y=142,relheight=0.04,relwidth=0.050)
    sprice_entry = Entry(bg_reg_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    sprice_entry.place(x=945,y=171,relheight=0.04,relwidth=0.050)

    mytree_board.bind('<Double-1>',treeviewclick)

def product_window():
    pro_frame = Frame(window,height=700,width=1100)
    pro_frame.place(x=0,y=0)
    
     # Create Labellogin
    Label(pro_frame,image=bgproductrg).place(x=-2,y=-2)
    Label(pro_frame,text="ทะเบียนสินค้า",font="Tahoma 20",bg="#ece1db").place(x=360,y=56)
    Label(pro_frame,text="ค้นหา :",font="Tahoma 18",bg="#ece1db").place(x=720,y=58)

    def treeviewclick(event) :
            global   values
            # Delete Exist Information in Entry
            name_entry.delete(0,END)
            pyamt_entry.delete(0,END)
            saleamt_entry.delete(0,END)
            tprice_entry.delete(0,END)

            values = mytree_pro.item(mytree_pro.focus(),'values')

        
            # Insert Select Information into Entry
            
            name_entry.insert(0,values[0])   
            pyamt_entry.insert(0,values[1])
            saleamt_entry.insert(0,values[2])
            tprice_entry.insert(0,values[3])

    def searchp():

            # Reset Medical Stock Display
            mytree_pro.delete(*mytree_pro.get_children())
            sql = "SELECT * FROM Product"
            cursor.execute(sql)# ORDER BY firstname ASC")
            result_member = cursor.fetchall()

            for i, data in enumerate(result_member):

                if (search_pro.get().lower() in data[1].lower() ):
                    mytree_pro.insert('', 'end', values=(data[1],data[2], data[3], data[4]))

    def addp() :
        if not name_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not pyamt_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not saleamt_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not tprice_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        else:
            mytree_pro.insert('',index='end',values=(name_entry.get(),pyamt_entry.get(),saleamt_entry.get(),tprice_entry.get()))
            curr = conn.cursor()
            curr.execute("INSERT INTO Product (proname,proprice,proleft,type) VALUES (?,?,?,?)",(name_entry.get(),pyamt_entry.get(),saleamt_entry.get(),tprice_entry.get()))
            conn.commit()
            messagebox.showinfo("ระบบ","ลงทะเบียนสำเร็จ")

            

            name_entry.delete(0,END)
            pyamt_entry.delete(0,END)
            saleamt_entry.delete(0,END)
            tprice_entry.delete(0,END)


    def updatep():
        if not name_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not pyamt_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not saleamt_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')

        elif not tprice_entry.get():
            messagebox.showinfo(title='ระบบ', message='กรุณากรอกทั้งหมด')
        elif saleamt_entry.get().isdigit()==False:
                messagebox.showinfo(title='ระบบ', message='กรุณากรอกราคา')
        
        else :
            
            selected =mytree_pro.focus()
            mytree_pro.item(selected,text="",values=(name_entry.get(),pyamt_entry.get(),saleamt_entry.get(),tprice_entry.get()))
            sql = '''
                update Product
                set proname=?,proprice=?,proleft=?,type=?
                where proname=? 

            '''
            cursor.execute(sql,[name_entry.get(),pyamt_entry.get(),saleamt_entry.get(),tprice_entry.get(),values[0]])
            conn.commit()


            name_entry.delete(0,END)
            pyamt_entry.delete(0,END)
            saleamt_entry.delete(0,END)
            tprice_entry.delete(0,END)

    def removem() :
        values =mytree_pro.item(mytree_pro.focus(),'values')
        yn = messagebox.askquestion(title='แจ้งเตือน',message="คุณต้องการลบหรือไม่"+values[0])
        if yn == "yes"  :
            deleterow = mytree_pro.selection()
            mytree_pro.delete(deleterow)
            sql = "DELETE FROM Product WHERE proname=?"
            cursor.execute(sql,[values[0]])
            conn.commit()
            messagebox.showinfo("ระบบ","ลบ "+values[0]+" สำเร็จ")

            name_entry.delete(0,END)
            pyamt_entry.delete(0,END)
            saleamt_entry.delete(0,END)
            tprice_entry.delete(0,END)


    def clearn():
        name_entry.delete(0,END)
        pyamt_entry.delete(0,END)
        saleamt_entry.delete(0,END)
        tprice_entry.delete(0,END)

    #Treeview
    treeframe_pro = Frame(pro_frame,height=390,width=740,bg="black")
    treeframe_pro.place(x=315,y=340)
    treebar = Scrollbar(treeframe_pro)
    treebar.pack(side=RIGHT,fill=Y)
    mytree_pro = ttk.Treeview(treeframe_pro,columns=("name","price","proleft","type"),height=14,yscrollcommand=treebar.set)
    mytree_pro.pack()
    #สี
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", bd=0, font="Tahoma 12 ",fieldbackground = "#ffc9ab",background = "ffc9ab",foreground = "black")
    style.configure("Treeview.Heading", font=(None, 13),background="#d87847")
    style.map('Treeview',background = [('selected','#d87847')])
    
    treebar.config(command=mytree_pro.yview)
    #create headings
    mytree_pro.heading("#0",text="",anchor=W)
    mytree_pro.heading("name",text="ชื่อสินค้า",anchor=CENTER)
    mytree_pro.heading("price",text="ราคาสินค้า ",anchor=CENTER)
    mytree_pro.heading("proleft",text="จำนวนสินค้า ",anchor=CENTER)
    mytree_pro.heading("type",text="ชนิดสินค้า",anchor=CENTER)
    
    #Format our columns
    mytree_pro.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    mytree_pro.column("name",anchor=W,width=300)
    mytree_pro.column("price",anchor=CENTER,width=170)
    mytree_pro.column("proleft",anchor=CENTER,width=135)
    mytree_pro.column("type",anchor=CENTER,width=135)
    

    mytree_pro.delete(*mytree_pro.get_children()) #delete old data from treeview
    conn = sqlite3.connect('db/boardgame403.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM Product"
    cursor.execute(sql)# ORDER BY firstname ASC")
    result = cursor.fetchall()
    for i,data in enumerate(result):
        mytree_pro.insert('', 'end', values=(data[1],data[2], data[3], data[4]))




    Button(pro_frame,text='ทะเบียนผู้ใช้',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",command=lambda:jumpto(pro_frame,user_window()),activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=73)
    Button(pro_frame,text='ทะเบียนสมาชิก',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",command=lambda:jumpto(pro_frame,member_window()),activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=190)
    Button(pro_frame,text='ทะเบียนบอร์ดเกม',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",command=lambda:jumpto(pro_frame,boardgame_registation()),activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=308)
    Button(pro_frame,text='ทะเบียนสินค้า',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=425)
    Button(pro_frame,text='ย้อนกลับ',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",command=lambda:out_Frame(pro_frame),activeforeground="#fff7f3",compound=TOP,bd=0).place(x=34,y=543,relheight=0.099,relwidth=0.202)
    Button(pro_frame,text='ลบข้อมูล',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="red",compound=TOP,bd=0,command=removem).place(x=339,y=223,relheight=0.060,relwidth=0.128)
    Button(pro_frame,text='เพิ่มข้อมูล',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="red",compound=TOP,bd=0,command=addp).place(x=528,y=223,relheight=0.060,relwidth=0.128)
    Button(pro_frame,text='แก้ไขข้อมูล',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="red",compound=TOP,bd=0,command=updatep).place(x=717,y=223,relheight=0.060,relwidth=0.128)
    Button(pro_frame,text="ยกเลิกข้อมูลที่กรอก",bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="red",compound=TOP,bd=0,command=clearn).place(x=906,y=223,relheight=0.060,relwidth=0.128)
    Button(pro_frame,image=iconserch,activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,bd=0,command= searchp).place(x=1030,y=60,relheight=0.048,relwidth=0.030)
    mytree_pro.bind('<Double-1>',treeviewclick)
    
    search_pro = Entry(pro_frame,bg="#f09968",font="Tahoma 13",bd=0,justify=CENTER)
    search_pro.place(x=810,y=60,relheight=0.048,relwidth=0.200)

    Label(pro_frame,text="____________________________________________________________",font="Tahoma 18",bg="#ece1db").place(x=300,y=100)
    Label(pro_frame,text="ชื่อสินค้า :",font="Tahoma 13",bg="#ece1db").place(x=310,y=150)
    Label(pro_frame,text="ราคาสินค้า :",font="Tahoma 13",bg="#ece1db").place(x=535,y=150)
    Label(pro_frame,text="จำนวนสินค้า :",font="Tahoma 13",bg="#ece1db").place(x=718,y=150)
    Label(pro_frame,text="ประเภทสินค้า :",font="Tahoma 13",bg="#ece1db").place(x=880,y=150)
    Label(pro_frame,text="____________________________________________________________",font="Tahoma 18",bg="#ece1db").place(x=300,y=270)

    name_entry = Entry(pro_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    name_entry.place(x=390,y=151,relheight=0.04,relwidth=0.130)
    pyamt_entry = Entry(pro_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    pyamt_entry.place(x=625,y=151,relheight=0.04,relwidth=0.080)
    saleamt_entry = Entry(pro_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    saleamt_entry.place(x=820,y=151,relheight=0.04,relwidth=0.050)
    tprice_entry = Entry(pro_frame,bg="#e8986c",font="Tahoma 13",bd=2,justify=CENTER)
    tprice_entry.place(x=995,y=151,relheight=0.04,relwidth=0.030)
    
def backtomenu():
    if resultO:
        if  resultO[0][4] == "owner" :
            usermenu_admin_window()
            user_entry.delete(0, END)
            pwd_entry.delete(0, END)
            user_entry.focus_force()
        else :
            usermenu_window()
            user_entry.delete(0, END)
            pwd_entry.delete(0, END)
            user_entry.focus_force()

def Store_Food():
    global conn,cursor,mytree,search,name_entry,pyamt_entry,saleamt_entry,tprice_entry,sprice_entry,search_stock
    bg_food_frame = Frame(window,height=700,width=1100)
    bg_food_frame.place(x=0,y=0)

    def back():
        bg_food_frame.destroy()
    def food1_window(values) :
        global food1_frame
        food1_frame = Frame(window,height=700,width=1100)
        food1_frame.place(x=0,y=0)
        global amout_tables,list_name,amout_name,boardgame1_frame
        conn = sqlite3.connect('db/boardgame403.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM Product"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result_board = cursor.fetchall()
        list_amout = []
        list_tables = []
        list_name = []

        def done():
            print()
            if amout_combo.get()=="" :
                messagebox.showwarning("แจ้งเตือน","กรุณาเลือกจำนวนสินค้า")
            elif amout_tables.get() == "":
                messagebox.showwarning("แจ้งเตือน","กรุณาเลือกโต๊ะของลูกค้า")
            elif amout_name.get() == "":
                messagebox.showwarning("แจ้งเตือน","กรุณาเลือกลูกค้า")
            else:
                def updateprice():
                    sql="select other_c ,m_check  from Player where name = ? and ta=?  "
                    cursor.execute(sql,[amout_name.get(),amout_tables.get()])
                    result = cursor.fetchone()
                    price = (int(amout_combo.get())*(data[2]))
                    print(result[1])
                    if result[1]==1:
                        price = price - (price*0.1)
                    new =result[0]+price
                    sql = '''
                        update Player
                        set other_c=?
                        where name = ? and ta=?

                    '''
                    cursor.execute(sql,[new,amout_name.get(),amout_tables.get()])
                    conn.commit()


                sql="select proleft from Product where proname = ?"
                cursor.execute(sql,[values[0]])
                result = cursor.fetchone()
                r =  ''.join(str(x) for x in result)
                new = int(r)- int(amout_combo.get())
                sql = '''
                    update Product
                    set proleft=?
                    where proname=?

                '''
                cursor.execute(sql,[new,values[0]])
                conn.commit()
                updateprice()
                food1_frame.destroy()



        def combo_bgame_select(e) :
            global list_name,amout_name
            list_name = []
            
            #ดึงราคาเกมที่เลือก
            conn = sqlite3.connect('db/boardgame403.db')
            cursor = conn.cursor()
            sql = "SELECT * FROM Player"
            cursor.execute(sql)# ORDER BY firstname ASC")
            name_combo = cursor.fetchall()
            
            for i,data in enumerate(name_combo):
                if data[0] == amout_tables.get():
                    
                    print(data[2])
                    if data[2] :
                         list_name.append(data[2])
            amout_name = ttk.Combobox(food1_frame,values=list_name,font="Tahoma 18")
            amout_name.place(x=560,y=477,relheight=0.064,relwidth=0.218)


        for i,data in enumerate(result_board):
            if data[1] == values[0]:
                for n in range(data[3]+1) : 
                    list_amout.append(n)
        
        
        sql = "SELECT * FROM Player"
        cursor.execute(sql)# ORDER BY firstname ASC")
        ta_combo = cursor.fetchall()
        for i,dat in enumerate(ta_combo):
            if dat[2] is not None and dat[0] not in list_tables and dat[2] != "":
                list_tables.append(dat[0])

        Label(food1_frame,image=bgfood1).place(x=-2,y=-2)
        Label(food1_frame,text=values[0],font="Tahoma 18",bg="#ece1db").place(x=555,y=123)
        Label(food1_frame,text=values[1],font="Tahoma 18",bg="#ece1db").place(x=555,y=193)
        note_entry = Entry(food1_frame,font="Tahoma 18",bd=0,justify=CENTER)
        note_entry.place(x=560,y=338,relheight=0.063,relwidth=0.215)
        amout_combo = ttk.Combobox(food1_frame,values=list_amout,font="Tahoma 18")
        amout_combo.place(x=560,y=262,relheight=0.064,relwidth=0.218)
        amout_tables = ttk.Combobox(food1_frame,values=list_tables,font="Tahoma 18")
        amout_tables.bind("<<ComboboxSelected>>", combo_bgame_select)
        amout_tables.place(x=560,y=410,relheight=0.064,relwidth=0.218)
        amout_name = ttk.Combobox(food1_frame,values=list_name,font="Tahoma 18")
        amout_name.place(x=560,y=477,relheight=0.064,relwidth=0.218)
        Button(food1_frame,bg="#FF7878",text="ตกลง",font="Tahoma 20",width=8,height=1,command=done).place(x=490,y=550)
        Button(food1_frame,bg="#ece1db",image=exitimg,font="Tahoma 20",bd=0,activebackground="#ece1db",command=lambda:food1_frame.destroy()).place(x=1030,y=15)

    def member(values):
        def c_member(values):
            sql="select mb_nname from Member where mb_tel = ?"
            cursor.execute(sql,[player_entry.get()])
            result = cursor.fetchall()
            print(result)
            if len(result)>0:
                    food2_window(values,1)
                    addn_frame.destroy()  
            else :
                    messagebox.showinfo('ระบบ','ขออภัยหมายเลขโทรศัพท์ไม่ถูกต้อง') 
        
        addn_frame = Frame(window,height=200,width=200)
        addn_frame.config(bg="#f8f4f2")
        addn_frame.place(x=500,y=250)
        Label(addn_frame,text="กรุณากรอกหมายเลขโทรศัพท์",font="Tahoma 18",bg="#f8f4f2").grid(row=0,columnspan=2,pady=2)
        player_entry = Entry(addn_frame,font="Tahoma 18",bd=0,justify=CENTER)
        player_entry.grid(row=1,columnspan=2)
        Button(addn_frame,text="ยืนยัน",font="Tahoma 18",bd=1,command=lambda:c_member(values)).grid(row=2,column=0,pady=2)
        Button(addn_frame,text="ยกเลิก",font="Tahoma 18",bd=1,command=lambda:addn_frame.destroy()).grid(row=2,column=1,pady=2,padx=5)

    def treeviewclick(event) :
    
        values = mytree.item(mytree.focus(),'values')
        sql="select proleft from Product where proname = ?"
        cursor.execute(sql,[values[0]])
        result = cursor.fetchone()
        r =  ''.join(str(x) for x in result)
        if  int(r)<=0:
            messagebox.showinfo('ระบบ','ขออภัย ตอนนี้สินค้าหมด')
        
        else:
            m=messagebox.askquestion ('ระบบ','คุณต้องการชำระสินค้าเลยหรือไม่')
            if m== 'yes':
                m=messagebox.askquestion ('ระบบ','คุณเป็นสมาชิกหรือไม่')
                if m== 'yes':
                    member(values)
                else:
                    food2_window(values,0)
            else:
                food1_window(values)
    
    def searchm():

        # Reset Medical Stock Display
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM Product"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result_member = cursor.fetchall()

        for i, data in enumerate(result_member):
            if (search_stock.get().lower() in data[1].lower() ):
                if data[4].lower() == "f":
                    mytree.insert('', 'end', values=(data[1],str(data[2])+" B                           " ))

    def food2_window(values,m_type) :
        food2_frame = Frame(window,height=700,width=1100)
        food2_frame.place(x=0,y=0)
        total=StringVar()
        p=StringVar()
        list_amout = []

        conn = sqlite3.connect('db/boardgame403.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM Product"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result_pro = cursor.fetchall()
        
        for i,data in enumerate(result_pro):
            if data[1] == values[0]:
                for n in range(data[3]+1) : 
                    list_amout.append(n)
       #####
        def done():
            if amout_combo.get()!="":
                def addreportincome():
                    te="sell  "+values[0]
                    now = datetime.datetime.now()
                    date = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
                    cursor.execute("INSERT INTO Reportincome (name,price,date) VALUES (?,?,?)",(te,price,date))
                    conn.commit()
                    #
                    avg=price/int(amout_combo.get())
                    sql = "INSERT INTO Reportavg (total_avg,num_avg,avg,date) VALUES (?,?,?,?)"
                    cursor.execute(sql,[price,amout_combo.get(),avg,date])
                    conn.commit()


                sql="select proleft from Product where proname = ?"
                cursor.execute(sql,[values[0]])
                result = cursor.fetchone()
                r =  ''.join(str(x) for x in result)
                new = int(r)- int(amout_combo.get())
                sql = '''
                    update Product
                    set proleft=?
                    where proname=?

                '''
                cursor.execute(sql,[new,values[0]])
                conn.commit()
                addreportincome()
                food2_frame.destroy()
            else:
                messagebox.showwarning("แจ้งเตือน","กรุณาเลือกจำนวนสินค้า")
            

        def charge():
            sum=int(pay_entry.get())-int(price)
            p.set(str(sum)+" B")


        def combo_bgame_select(e) :
            global price
            price=0
            for i,data in enumerate(result_pro):
                if data[1] == values[0]:
                    if m_type==0 :
                        price=int(data[2])*int(amout_combo.get())
                        total.set( str(price)+" B")
                    else:
                        price=int(data[2])*int(amout_combo.get())
                        price = price - (price*0.1)
                        total.set( str(price)+" B")

        Label(food2_frame,image=bgfood2).place(x=-2,y=-2)
        Label(food2_frame,text=values[0],font="Tahoma 18",bg="#ece1db").place(x=570,y=92)
        Label(food2_frame,text=values[1],font="Tahoma 18",bg="#ece1db").place(x=570,y=162)
        Label(food2_frame,textvariable=total,font="Tahoma 18",bg="white").place(x=570,y=382,relheight=0.064,relwidth=0.216)
        Label(food2_frame,textvariable=p,font="Tahoma 18",bg="white").place(x=570,y=519,relheight=0.064,relwidth=0.216)
        
        amout_combo = ttk.Combobox(food2_frame,values=list_amout,font="Tahoma 18")
        amout_combo.bind("<<ComboboxSelected>>", combo_bgame_select)
        amout_combo.place(x=570,y=234,relheight=0.064,relwidth=0.216)
        
        note_entry = Entry(food2_frame,font="Tahoma 18",bd=0,justify=CENTER)
        note_entry.place(x=570,y=310,relheight=0.062,relwidth=0.215)
        pay_entry = Entry(food2_frame,font="Tahoma 18",bd=0,justify=CENTER)
        pay_entry.place(x=570,y=449,relheight=0.062,relwidth=0.215)
        Button(food2_frame,bg="#FABCBC",text="ยอดสุทธิ",font="Tahoma 20",width=8,height=1,command=charge).place(x=490,y=580)
        Button(food2_frame,bg="#FABCBC",text="ยืนยัน",font="Tahoma 20",width=8,height=1,command=done).place(x=40,y=600)
        Button(food2_frame,bg="#ece1db",image=exitimg,font="Tahoma 20",bd=0,command=lambda:food2_frame.destroy(),activebackground="#ece1db").place(x=1030,y=15)


     # Create Labellogin
    Label(bg_food_frame,image=backg_Food).place(x=-2,y=-2)
    Button(bg_food_frame,text='ย้อนกลับ',bg="#fc7a33",font="Tahoma 20",activebackground="#fc7a33",activeforeground="#fff7f3",compound=TOP,bd=0,command=back).place(x=325,y=565,relheight=0.099,relwidth=0.202)
    Button(bg_food_frame,image=food_icon,compound=TOP,height=185,width=240,bd=0,activebackground="#f86819").place(x=21,y=20)
    Button(bg_food_frame,image=drink_icon,compound=TOP,height=185,width=240,bd=0,command=lambda:jumpto(bg_food_frame,Store_Drink()),activebackground="#f86819").place(x=21,y=255)
    Button(bg_food_frame,image=boardgame_icon,compound=TOP,height=185,width=240,bd=0,command=lambda:jumpto(bg_food_frame,Store_Boardgame()),activebackground="#f86819").place(x=21,y=489)
    Button(bg_food_frame,image=iconserch,activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,bd=0,command=searchm).place(x=1030,y=54)
    Label(bg_food_frame,text="เมนูอาหาร",font="Tahoma 20",bg="#ece1db").place(x=360,y=56)

    #Treeview
    treeframe = Frame(bg_food_frame,height=390,width=740,bg="black")
    treeframe.place(x=325,y=130)
    treebar = Scrollbar(treeframe)
    treebar.pack(side=RIGHT,fill=Y)
    mytree = ttk.Treeview(treeframe,columns=("name","price"),height=16,yscrollcommand=treebar.set)
    mytree.pack()
    #สี
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", bd=0, font="Tahoma 15 ",height=30,fieldbackground = "#ffc9ab",background = "ffc9ab",foreground = "black")
    style.configure("Treeview.Heading", font=(None, 20),background="#d87847")
    style.map('Treeview',background = [('selected','#d87847')])
    
    treebar.config(command=mytree.yview)
    #create headings
    mytree.heading("#0",text="",anchor=W)
    mytree.heading("name",text="ชื่อ",anchor=CENTER)
    mytree.heading("price",text="ราคา ",anchor=CENTER)
    
    #Format our columns
    mytree.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    mytree.column("name",anchor=W,width=370)
    mytree.column("price",anchor=E,width=370)


    mytree.delete(*mytree.get_children()) #delete old data from treeview
    conn = sqlite3.connect('db/boardgame403.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM Product"
    cursor.execute(sql)# ORDER BY firstname ASC")
    result = cursor.fetchall()
    for i,data in enumerate(result):
        if data[4].lower() == "f":
            mytree.insert('', 'end', values=(data[1],str(data[2])+" B                           " ))

    

    mytree.bind('<Double-1>',treeviewclick)
    search_stock = Entry(bg_food_frame,bg="#f09968",font="Tahoma 17",bd=0,justify=CENTER)
    search_stock.place(x=812,y=56,relheight=0.069,relwidth=0.200)
    

# 
def Store_Drink():
    global conn,cursor,mytree,search,name_entry,pyamt_entry,saleamt_entry,tprice_entry,sprice_entry,search_stock
    bg_drink_frame = Frame(window,height=700,width=1100)
    bg_drink_frame.place(x=0,y=0)
    
    def back():
        bg_drink_frame.destroy()

    def drinks1_window(values) :
        global drinks1_frame
        drinks1_frame = Frame(window,height=700,width=1100)
        drinks1_frame.place(x=0,y=0)
        global amout_tables,list_name,amout_name,boardgame1_frame
        conn = sqlite3.connect('db/boardgame403.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM Product"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result_board = cursor.fetchall()
        list_amout = []
        list_tables = []
        list_name = []

        def done():
            if amout_combo.get()=="" :
                messagebox.showwarning("แจ้งเตือน","กรุณาเลือกจำนวนสินค้า")
            elif amout_tables.get() == "":
                messagebox.showwarning("แจ้งเตือน","กรุณาเลือกโต๊ะของลูกค้า")
            elif amout_name.get() == "":
                messagebox.showwarning("แจ้งเตือน","กรุณาเลือกลูกค้า")
            else:
                def updateprice():
                    sql="select proprice from Product where proname = ?"
                    cursor.execute(sql,[values[0]])
                    result = cursor.fetchone()
                    r =  ''.join(str(x) for x in result)
                    sql="select other_c ,m_check  from Player where name = ? and ta=?  "
                    cursor.execute(sql,[amout_name.get(),amout_tables.get()])
                    result = cursor.fetchone()
                    price = (int(amout_combo.get())*int(r))
                    print(result[1])
                    if result[1]==1:
                        price = price - (price*0.1)
                    new =result[0]+price
                    sql = '''
                        update Player
                        set other_c=?
                        where name = ? and ta=?

                    '''
                    cursor.execute(sql,[new,amout_name.get(),amout_tables.get()])
                    conn.commit()

                sql="select proleft from Product where proname = ?"
                cursor.execute(sql,[values[0]])
                result = cursor.fetchone()
                r =  ''.join(str(x) for x in result)
                new = int(r)- int(amout_combo.get())
                sql = '''
                    update Product
                    set proleft=?
                    where proname=?

                '''
                cursor.execute(sql,[new,values[0]])
                conn.commit()
                updateprice()
                drinks1_frame.destroy()


        def combo_bgame_select(e) :
            global list_name,amout_name
            list_name = []
            
            #ดึงราคาเกมที่เลือก
            conn = sqlite3.connect('db/boardgame403.db')
            cursor = conn.cursor()
            sql = "SELECT * FROM Player"
            cursor.execute(sql)# ORDER BY firstname ASC")
            name_combo = cursor.fetchall()
            
            for i,data in enumerate(name_combo):
                if data[0] == amout_tables.get():
                    
                    print(data[2])
                    if data[2] :
                         list_name.append(data[2])
            amout_name = ttk.Combobox(drinks1_frame,values=list_name,font="Tahoma 18")
            amout_name.place(x=570,y=487,relheight=0.064,relwidth=0.218)
        

        for i,data in enumerate(result_board):
            if data[1] == values[0]:
                for n in range(data[3]+1) : 
                    list_amout.append(n)
        
        
        
        sql = "SELECT * FROM Player"
        cursor.execute(sql)# ORDER BY firstname ASC")
        ta_combo = cursor.fetchall()
        for i,dat in enumerate(ta_combo):
            if dat[2] is not None and dat[0] not in list_tables and dat[2] != "":
                list_tables.append(dat[0])

        Label(drinks1_frame,image=bgdrinks1).place(x=-2,y=-2)
        Label(drinks1_frame,text=values[0],font="Tahoma 18",bg="#ece1db").place(x=577,y=132)
        Label(drinks1_frame,text=values[1],font="Tahoma 18",bg="#ece1db").place(x=577,y=202)
        note_entry = Entry(drinks1_frame,font="Tahoma 18",bd=1,justify=CENTER)
        note_entry.place(x=570,y=348,relheight=0.064,relwidth=0.215)
        amout_combo = ttk.Combobox(drinks1_frame,values=list_amout,font="Tahoma 18")
        amout_combo.place(x=570,y=273,relheight=0.064,relwidth=0.218)
        amout_tables = ttk.Combobox(drinks1_frame,values=list_tables,font="Tahoma 18")
        amout_tables.bind("<<ComboboxSelected>>", combo_bgame_select)
        amout_tables.place(x=570,y=420,relheight=0.064,relwidth=0.218)
        amout_name = ttk.Combobox(drinks1_frame,values=list_name,font="Tahoma 18")
        amout_name.place(x=570,y=487,relheight=0.064,relwidth=0.218)
        Button(drinks1_frame,bg="#FF7878",text="ยืนยัน",font="Tahoma 20",width=8,height=1,command=done).place(x=500,y=560)
        Button(drinks1_frame,bg="#ece1db",image=exitimg,command=lambda:drinks1_frame.destroy(),font="Tahoma 20",bd=0,activebackground="#ece1db").place(x=1030,y=15)
        
    def member(values):
        def c_member(values):
            sql="select mb_nname from Member where mb_tel = ?"
            cursor.execute(sql,[player_entry.get()])
            result = cursor.fetchall()
            print(result)
            if len(result)>0:
                    drinks2_window(values,1)
                    addn_frame.destroy()  
            else :
                    messagebox.showinfo('ระบบ','ขออภัยหมายเลขโทรศัพท์ไม่ถูกต้อง') 
        
        addn_frame = Frame(window,height=200,width=200)
        addn_frame.config(bg="#f8f4f2")
        addn_frame.place(x=500,y=250)
        Label(addn_frame,text="กรุณากรอกชื่อ",font="Tahoma 18",bg="#f8f4f2").grid(row=0,columnspan=2,pady=2)
        player_entry = Entry(addn_frame,font="Tahoma 18",bd=0,justify=CENTER)
        player_entry.grid(row=1,columnspan=2)
        Button(addn_frame,text="ยืนยัน",font="Tahoma 18",bd=1,command=lambda:c_member(values)).grid(row=2,column=0,pady=2)
        Button(addn_frame,text="ยกเลิก",font="Tahoma 18",bd=1,command=lambda:addn_frame.destroy()).grid(row=2,column=1,pady=2,padx=5)


    def treeviewclick(event) :
    
        values = mytree.item(mytree.focus(),'values')
        sql="select proleft from Product where proname = ?"
        cursor.execute(sql,[values[0]])
        result = cursor.fetchone()
        r =  ''.join(str(x) for x in result)
        if  int(r)<=0:
            messagebox.showinfo('ระบบ','ขออภัย ตอนนี้สินค้าหมด')
        
        else:
            m=messagebox.askquestion ('ระบบ','คุณต้องการจ่ายสินค้าเลยหรือไม่')
            if m== 'yes':
                    m=messagebox.askquestion ('ระบบ','คุณเป็นสมาชิกหรือไม่')
                    if m== 'yes':
                        member(values)
                    else:
                         drinks2_window(values,0)
            else:
                drinks1_window(values)

    def searchm():

        # Reset Medical Stock Display
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM Product"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result_member = cursor.fetchall()

        for i, data in enumerate(result_member):
            if (search_stock.get().lower() in data[1].lower() ):
                if data[4].lower() == "d":
                    mytree.insert('', 'end', values=(data[1],str(data[2])+" B                           " ))

    def drinks2_window(values,m_type) :
        drinks2_frame = Frame(window,height=700,width=1100)
        drinks2_frame.place(x=0,y=0)
        total=StringVar()
        p=StringVar()
        list_amout = []


        conn = sqlite3.connect('db/boardgame403.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM Product"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result_board = cursor.fetchall()

        for i,data in enumerate(result_board):
            if data[1] == values[0]:
                for n in range(data[3]+1) : 
                    list_amout.append(n)
                
        def done():
            if amout_combo.get()!="":
                def addreportincome():
                    te="sell  "+values[0]
                    now = datetime.datetime.now()
                    date = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
                    cursor.execute("INSERT INTO Reportincome (name,price,date) VALUES (?,?,?)",(te,price,date))
                    conn.commit()

                    avg=price/int(amout_combo.get())
                    sql = "INSERT INTO Reportavg (total_avg,num_avg,avg,date) VALUES (?,?,?,?)"
                    cursor.execute(sql,[price,amout_combo.get(),avg,date])
                    conn.commit()


                sql="select proleft from Product where proname = ?"
                cursor.execute(sql,[values[0]])
                result = cursor.fetchone()
                r =  ''.join(str(x) for x in result)
                new = int(r)- int(amout_combo.get())
                sql = '''
                    update Product
                    set proleft=?
                    where proname=?

                '''
                cursor.execute(sql,[new,values[0]])
                conn.commit()
                addreportincome()
                drinks2_frame.destroy()
            else:
                messagebox.showwarning("แจ้งเตือน","กรุณาเลือกจำนวนสินค้า")

        def charge():
            sum=int(pay_entry.get())-int(price)
            p.set(str(sum)+" B")


        def combo_bgame_select(e) :
            global price
            price=0
            for i,data in enumerate(result_board):
                if data[1] == values[0]: 
                    if m_type==0 :
                        price=int(data[2])*int(amout_combo.get())
                        total.set( str(price)+" B")
                    else:
                        price=int(data[2])*int(amout_combo.get())
                        price = price - (price*0.1)
                        total.set( str(price)+" B")

        Label(drinks2_frame,image=bgdrinks2).place(x=-2,y=-2)
        Label(drinks2_frame,text=values[0],font="Tahoma 18",bg="#ece1db").place(x=570,y=92)
        Label(drinks2_frame,text=values[1],font="Tahoma 18",bg="#ece1db").place(x=570,y=162)
        Label(drinks2_frame,textvariable=total,font="Tahoma 18",bg="white").place(x=570,y=382,relheight=0.064,relwidth=0.216)
        Label(drinks2_frame,textvariable=p,font="Tahoma 18",bg="white").place(x=570,y=519,relheight=0.064,relwidth=0.216)
        
        
        amout_combo = ttk.Combobox(drinks2_frame,values=list_amout,font="Tahoma 18")
        amout_combo.bind("<<ComboboxSelected>>", combo_bgame_select)
        amout_combo.place(x=570,y=234,relheight=0.064,relwidth=0.216)
        note_entry = Entry(drinks2_frame,font="Tahoma 18",bd=0,justify=CENTER)
        note_entry.place(x=570,y=310,relheight=0.062,relwidth=0.215)
        pay_entry = Entry(drinks2_frame,font="Tahoma 18",bd=0,justify=CENTER)
        pay_entry.place(x=570,y=449,relheight=0.062,relwidth=0.215)
        Button(drinks2_frame,bg="#FF7878",text="ยอดสุทธิ",font="Tahoma 20",width=8,height=1,command=charge).place(x=490,y=580)
        Button(drinks2_frame,bg="#FF7878",text="ตกลง",font="Tahoma 20",width=8,height=1,command=done).place(x=40,y=600)
        Button(drinks2_frame,bg="#ece1db",image=exitimg,command=lambda:drinks2_frame.destroy(),font="Tahoma 20",bd=0,activebackground="#ece1db").place(x=1030,y=15)
        
     # Create Labellogin
    Label(bg_drink_frame,image=backg_Drink,activebackground="#f86819").place(x=-2,y=-2)
    Button(bg_drink_frame,text='ย้อนกลับ',bg="#fc7a33",font="Tahoma 20",activebackground="#fc7a33",activeforeground="#fff7f3",compound=TOP,bd=0,command=back).place(x=325,y=565,relheight=0.099,relwidth=0.202)
    Button(bg_drink_frame,image=food_icon,compound=TOP,height=185,width=240,bd=0,command=lambda:jumpto(bg_drink_frame,Store_Food()),activebackground="#f86819").place(x=21,y=20)
    Button(bg_drink_frame,image=drink_icon,compound=TOP,height=185,width=240,bd=0,activebackground="#f86819").place(x=21,y=255)
    Button(bg_drink_frame,image=boardgame_icon,compound=TOP,height=185,width=240,bd=0,command=lambda:jumpto(bg_drink_frame,Store_Boardgame())).place(x=21,y=491)
    Button(bg_drink_frame,image=iconserch,activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,bd=0,command=searchm).place(x=1030,y=54)
    Label(bg_drink_frame,text="เมนูเครื่องดื่ม",font="Tahoma 20",bg="#ece1db").place(x=360,y=56)

    #Treeview
    treeframe = Frame(bg_drink_frame,height=390,width=740,bg="black")
    treeframe.place(x=325,y=130)
    treebar = Scrollbar(treeframe)
    treebar.pack(side=RIGHT,fill=Y)
    mytree = ttk.Treeview(treeframe,columns=("name","price"),height=16,yscrollcommand=treebar.set)
    mytree.pack()
    #สี
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", bd=0, font="Tahoma 15 ",height=30,fieldbackground = "#ffc9ab",background = "ffc9ab",foreground = "black")
    style.configure("Treeview.Heading", font=(None, 20),background="#d87847")
    style.map('Treeview',background = [('selected','#d87847')])
    
    treebar.config(command=mytree.yview)
    #create headings
    mytree.heading("#0",text="",anchor=W)
    mytree.heading("name",text="ชื่อ",anchor=CENTER)
    mytree.heading("price",text="ราคา",anchor=CENTER)
    
    #Format our columns
    mytree.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    mytree.column("name",anchor=W,width=370)
    mytree.column("price",anchor=E,width=370)


    mytree.delete(*mytree.get_children()) #delete old data from treeview
    conn = sqlite3.connect('db/boardgame403.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM Product"
    cursor.execute(sql)# ORDER BY firstname ASC")
    result = cursor.fetchall()
    for i,data in enumerate(result):
        if data[4].lower() == "d":
            mytree.insert('', 'end', values=(data[1],str(data[2])+" B                           " ))

    
    search_stock = Entry(bg_drink_frame,bg="#f09968",font="Tahoma 17",bd=0,justify=CENTER)
    search_stock.place(x=812,y=56,relheight=0.069,relwidth=0.200)
    mytree.bind('<Double-1>',treeviewclick)
    
# 
def Store_Boardgame():


    global conn,cursor,mytree,search,name_entry,pyamt_entry,saleamt_entry,tprice_entry,sprice_entry,search_stock
    bg_boardgame_frame = Frame(window,height=700,width=1100)
    bg_boardgame_frame.place(x=0,y=0)

    
    def back():
        bg_boardgame_frame.destroy()        

    def boardgame1_window(values) :
        global amout_tables,list_name,amout_name,boardgame1_frame
        conn = sqlite3.connect('db/boardgame403.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM Boardgame"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result_board = cursor.fetchall()
        list_amout = []
        list_tables = []
        list_name = []

        def combo_bgame_select(e) :
            global list_name,amout_name
            list_name = []
            
            #ดึงราคาเกมที่เลือก
            conn = sqlite3.connect('db/boardgame403.db')
            cursor = conn.cursor()
            sql = "SELECT * FROM Player"
            cursor.execute(sql)# ORDER BY firstname ASC")
            name_combo = cursor.fetchall()
            
            for i,data in enumerate(name_combo):
                if data[0] == amout_tables.get():
                    
                    print(data[2])
                    if data[2] :
                         list_name.append(data[2])
            amout_name = ttk.Combobox(boardgame1_frame,values=list_name,font="Tahoma 18")
            amout_name.place(x=540,y=467,relheight=0.064,relwidth=0.216)

        def done():
            if amout_combo.get()=="" :
                messagebox.showwarning("แจ้งเตือน","กรุณาเลือกจำนวนสินค้า")
            elif amout_tables.get() == "":
                messagebox.showwarning("แจ้งเตือน","กรุณาเลือกโต๊ะของลูกค้า")
            elif amout_name.get() == "":
                messagebox.showwarning("แจ้งเตือน","กรุณาเลือกลูกค้า")
            else:
                def updateprice():
                    sql="select other_c ,m_check from Player where name = ? and ta=?  "
                    cursor.execute(sql,[amout_name.get(),amout_tables.get()])
                    result = cursor.fetchone()
                    for i,data in enumerate(result_board):
                        if data[1] == values[0]:
                            price=(int(amout_combo.get())*int(data[5]))
                            if result[1]==1:
                                price = price - (price*0.1)
                            new = result[0] + price
                    sql = '''
                        update Player
                        set other_c=?
                        where name = ? and ta=?

                    '''
                    cursor.execute(sql,[new,amout_name.get(),amout_tables.get()])
                    conn.commit()
                sql="select sale_amt from Boardgame where bgame_name = ?"
                cursor.execute(sql,[values[0]])
                result = cursor.fetchone()
                r =  ''.join(str(x) for x in result)
                new = int(r)- int(amout_combo.get())
                sql = """
                        update Boardgame
                        set sale_amt=?
                        where bgame_name=?
                    """
                cursor.execute(sql,[new,values[0]])
                conn.commit()
                updateprice()
                boardgame1_frame.destroy()
    

        for i,data in enumerate(result_board):
            if data[1] == values[0]:
                for n in range(data[3]+1) : 
                    list_amout.append(n)
        
        
        sql = "SELECT * FROM Player"
        cursor.execute(sql)# ORDER BY firstname ASC")
        ta_combo = cursor.fetchall()
        for i,dat in enumerate(ta_combo):
            if dat[2] is not None and dat[0] not in list_tables and dat[2] != "":
                list_tables.append(dat[0])

        boardgame1_frame = Frame(window,height=700,width=1100)
        boardgame1_frame.place(x=0,y=0)
    
        
        Label(boardgame1_frame,image=bggame1).place(x=-2,y=-2)
        Label(boardgame1_frame,text=values[0],font="Tahoma 18",bg="#ece1db").place(x=540,y=184)
        Label(boardgame1_frame,text=values[1],font="Tahoma 18",bg="#ece1db").place(x=540,y=254)
        amout_combo = ttk.Combobox(boardgame1_frame,values=list_amout,font="Tahoma 18")
        
        amout_combo.place(x=540,y=319,relheight=0.064,relwidth=0.216)
        amout_tables = ttk.Combobox(boardgame1_frame,values=list_tables,font="Tahoma 18")
        amout_tables.bind("<<ComboboxSelected>>", combo_bgame_select)
        amout_tables.place(x=540,y=394,relheight=0.064,relwidth=0.216)
        amout_name = ttk.Combobox(boardgame1_frame,values=list_name,font="Tahoma 18")
        amout_name.place(x=540,y=467,relheight=0.064,relwidth=0.216)
        Button(boardgame1_frame,bg="#5CDDE1",text="ตกลง",font="Tahoma 20",width=8,height=1,command=done).place(x=470,y=540)
        Button(boardgame1_frame,bg="#ece1db",image=exitimg,command=lambda:boardgame1_frame.destroy(),font="Tahoma 20",bd=0,activebackground="#ece1db").place(x=1030,y=15)

    def member(values):
        def c_member(values):
            sql="select mb_nname from Member where mb_tel = ?"
            cursor.execute(sql,[player_entry.get()])
            result = cursor.fetchall()
            print(result)
            if len(result)>0:
                    boardgame2_window(values,1)
                    addn_frame.destroy()  
            else :
                    messagebox.showinfo('ระบบ','ขออภัยหมายเลขโทรศัพท์ไม่ถูกต้อง') 
        
        addn_frame = Frame(window,height=200,width=200)
        addn_frame.config(bg="#f8f4f2")
        addn_frame.place(x=500,y=250)
        Label(addn_frame,text="กรุณากรอกชื่อ",font="Tahoma 18",bg="#f8f4f2").grid(row=0,columnspan=2,pady=2)
        player_entry = Entry(addn_frame,font="Tahoma 18",bd=0,justify=CENTER)
        player_entry.grid(row=1,columnspan=2)
        Button(addn_frame,text="ยืนยัน",font="Tahoma 18",bd=1,command=lambda:c_member(values)).grid(row=2,column=0,pady=2)
        Button(addn_frame,text="ยกเลิก",font="Tahoma 18",bd=1,command=lambda:addn_frame.destroy()).grid(row=2,column=1,pady=2,padx=5)


    def treeviewclick(event) :
    
        values = mytree.item(mytree.focus(),'values')
        sql="select sale_amt from Boardgame where bgame_name = ?"
        cursor.execute(sql,[values[0]])
        result = cursor.fetchone()
        r =  ''.join(str(x) for x in result)
        print(r)
        if  int(r)<=0:
            messagebox.showinfo('ระบบ','ขออภัย ตอนนี้สินค้าหมด')
        
        else:
            m=messagebox.askquestion ('ระบบ','คุณต้องการจ่ายสินค้าเลยหรือไม่')
            if m== 'yes':
                m=messagebox.askquestion ('ระบบ','คุณเป็นสมาชิกหรือไม่')
                if m== 'yes':
                    member(values)
                else:
                    boardgame2_window(values,0)
            else:
                boardgame1_window(values)
            

    def searchm():

        # Reset Medical Stock Display
        mytree.delete(*mytree.get_children())
        sql = "SELECT * FROM Boardgame"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result_member = cursor.fetchall()

        for i, data in enumerate(result_member):
            if (search_stock.get().lower() in data[1].lower() ):
                mytree.insert('', 'end', values=(data[1], str(data[5])+" B                          "))   

        # Insert Select Information into Entry     
    def boardgame2_window(values,m_type) :
        boardgame2_frame = Frame(window,height=700,width=1100)
        boardgame2_frame.place(x=0,y=0)
        total=StringVar()
        p=StringVar()
        list_amout = []
        
        def charge():
            sum=int(pay_entry.get())-int(price)
            p.set(str(sum)+" B")


        def combo_bgame_select(e) :
            global price
            price=0
            for i,data in enumerate(result_board):
                if data[1] == values[0]: 
                    price=int(data[5])*int(amout_combo.get())
                    if m_type == 1:
                        price=price - (price*0.1)
                    
                    total.set( str(price)+" B")

        def done():
            if amout_combo.get()!="":
                def addreportincome():
                    te="sell  "+values[0]
                    now = datetime.datetime.now()
                    date = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
                    cursor.execute("INSERT INTO Reportincome (name,price,date) VALUES (?,?,?)",(te,price,date))
                    conn.commit()



                sql="select sale_amt from Boardgame where bgame_name = ?"
                cursor.execute(sql,[values[0]])
                result = cursor.fetchone()
                r =  ''.join(str(x) for x in result)
                new = int(r)- int(amout_combo.get())
                sql = """
                        update Boardgame
                        set sale_amt=?
                        where bgame_name=?
                    """
                cursor.execute(sql,[new,values[0]])
                conn.commit()
                addreportincome()
                boardgame2_frame.destroy()
            else:
                messagebox.showwarning("แจ้งเตือน","กรุณาเลือกจำนวนสินค้า")
            

        conn = sqlite3.connect('db/boardgame403.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM Boardgame"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result_board = cursor.fetchall()

        for i,data in enumerate(result_board):
            if data[1] == values[0]:
                for n in range(data[3]+1) : 
                    list_amout.append(n)
        


        Label(boardgame2_frame,image=bggame2).place(x=-2,y=-2)
        Label(boardgame2_frame,text=values[0],font="Tahoma 18",bg="#ece1db").place(x=550,y=113)
        Label(boardgame2_frame,text=values[1],font="Tahoma 18",bg="#ece1db").place(x=550,y=183)
        Label(boardgame2_frame,textvariable=total,font="Tahoma 20",bg="white").place(x=550,y=334,relheight=0.064,relwidth=0.216)
        Label(boardgame2_frame,textvariable=p,font="Tahoma 20",bg="white").place(x=550,y=473,relheight=0.064,relwidth=0.216)
        
        amout_combo = ttk.Combobox(boardgame2_frame,values=list_amout,font="Tahoma 18")
        amout_combo.bind("<<ComboboxSelected>>", combo_bgame_select)
        amout_combo.place(x=550,y=259,relheight=0.064,relwidth=0.216)
        pay_entry = Entry(boardgame2_frame,font="Tahoma 18",bd=0,justify=CENTER)
        pay_entry.place(x=550,y=407,relheight=0.062,relwidth=0.215)
        Button(boardgame2_frame,bg="#5CDDE1",text="ยอดสุทธิ",font="Tahoma 20",width=8,height=1,command=charge).place(x=470,y=550)
        Button(boardgame2_frame,bg="#5CDDE1",text="ตกลง",font="Tahoma 20",width=8,height=1,command=done).place(x=40,y=600)
        Button(boardgame2_frame,bg="#ece1db",image=exitimg,font="Tahoma 20",command=lambda:boardgame2_frame.destroy(),bd=0,activebackground="#ece1db").place(x=1030,y=15)

        
    Label(bg_boardgame_frame,image=backg_Boardgame,activebackground="#f86819").place(x=-2,y=-2)
    Button(bg_boardgame_frame,text='ย้อนกลับ',bg="#fc7a33",font="Tahoma 20",activebackground="#fc7a33",activeforeground="#fff7f3",compound=TOP,bd=0,command=back).place(x=325,y=565,relheight=0.099,relwidth=0.202)
    Button(bg_boardgame_frame,image=food_icon,compound=TOP,height=185,width=240,bd=0,command=lambda:jumpto(bg_boardgame_frame,Store_Food()),activebackground="#f86819").place(x=21,y=20)
    Button(bg_boardgame_frame,image=drink_icon,compound=TOP,height=185,width=240,bd=0,command=lambda:jumpto(bg_boardgame_frame,Store_Drink()),activebackground="#f86819").place(x=21,y=255)
    Button(bg_boardgame_frame,image=boardgame_icon,compound=TOP,height=185,width=240,bd=0).place(x=21,y=489)
    Button(bg_boardgame_frame,image=iconserch,activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,bd=0,command=searchm).place(x=1030,y=54)


     # Create Labellogi
    Label(bg_boardgame_frame,text="เมนูบอร์ดเกม",font="Tahoma 20",bg="#ece1db").place(x=360,y=56)

    #Treeview
    treeframe = Frame(bg_boardgame_frame,height=390,width=740,bg="black")
    treeframe.place(x=325,y=130)
    treebar = Scrollbar(treeframe)
    treebar.pack(side=RIGHT,fill=Y)
    mytree = ttk.Treeview(treeframe,columns=("name","price"),height=16,yscrollcommand=treebar.set)
    mytree.pack()
    #สี
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", bd=0, font="Tahoma 15 ",fieldbackground = "#ffc9ab",background = "ffc9ab",foreground = "black")
    style.configure("Treeview.Heading", font=(None, 20),background="#d87847")
    style.map('Treeview',background = [('selected','#d87847')])
    
    treebar.config(command=mytree.yview)
    #create headings
    mytree.heading("#0",text="",anchor=W)
    mytree.heading("name",text="ชื่อ",anchor=CENTER)
    mytree.heading("price",text="ราคา",anchor=CENTER)
    #Format our columns
    mytree.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    mytree.column("name",anchor=W,width=370)
    mytree.column("price",anchor=E,width=370)

    mytree.delete(*mytree.get_children()) #delete old data from treeview
    conn = sqlite3.connect('db/boardgame403.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM Boardgame"
    cursor.execute(sql)# ORDER BY firstname ASC")
    result = cursor.fetchall()
    for i,data in enumerate(result):
        mytree.insert('', 'end', values=(data[1], str(data[5])+" B                          "))

    search_stock = Entry(bg_boardgame_frame,bg="#f09968",font="Tahoma 17",bd=0,justify=CENTER)
    search_stock.place(x=812,y=56,relheight=0.069,relwidth=0.200)
    mytree.bind('<Double-1>',treeviewclick)
     


def Report_Income_Boardgame():
    global conn,cursor,mytree,dayCombo

    def serchmonth(a):
        global dayCombo
        dayCombo.destroy()
        datelstday = ["ทุกวัน"]
        month31=['มกราคม', 'มีนาคม','พฤษภาคม','กรกฎาคม', 'สิงหาคม', 'ตุลาคม','ธันวาคม']
        if monthCombo.get() in month31:
            for i in range(1,32):
                datelstday.append(i)
        elif monthCombo.get() == 'กุมภาพันธ์':
            y=int(yearCombo.get())-543
            if (y%400 == 0 or y%4 ==0 and y%100 != 0) :
                for i in range(1,30):
                    datelstday.append(i)
            else:
                for i in range(1,29):
                    datelstday.append(i)
        elif monthCombo.get() == "ทุกเดือน":
            datelstday = []
        else:
            for i in range(1,31):
                datelstday.append(i)
        dayCombo = ttk.Combobox(bg_report_income_frame, values=datelstday,font="Tahoma 17", justify='center',state='readonly')
        dayCombo.set("ทุกวัน")
        dayCombo.place(x=468,y=120,relheight=0.06,relwidth=0.10)

    def done():
        total=0
        mytree.delete(*mytree.get_children()) #delete old data from treeview
        conn = sqlite3.connect('db/boardgame403.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM Reportincome"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result = cursor.fetchall()
        for i,data in enumerate(result):
            new_date=data[3].split('/')
            if monthCombo.get() == "ทุกเดือน":
                if int(new_date[2]) == (int(yearCombo.get())-543):
                   total = total + data[2]
                   year = int(new_date[2])+543
                   pyear=new_date[0]+"/"+new_date[1]+"/"+str(year)
                   mytree.insert('', 'end', values=(data[1],data[2],pyear))
            else:
                if dayCombo.get() == "ทุกวัน":
                    x= datelstmonth.index(monthCombo.get())
                    if int(new_date[2]) == (int(yearCombo.get())-543) and x == int(new_date[1]):
                        total = total + data[2]
                        year = int(new_date[2])+543
                        pyear=new_date[0]+"/"+new_date[1]+"/"+str(year)
                        mytree.insert('', 'end', values=(data[1],data[2],pyear))
                else:
                    x= datelstmonth.index(monthCombo.get())
                    if int(new_date[2]) == (int(yearCombo.get())-543) and (x == int(new_date[1] )) and (int(new_date[0])==int(dayCombo.get())):
                        total = total + data[2]
                        year = int(new_date[2])+543
                        pyear=new_date[0]+"/"+new_date[1]+"/"+str(year)
                        mytree.insert('', 'end', values=(data[1],data[2],pyear))
        Label(bg_report_income_frame,text=total,font="Tahoma 18",bg="white").place(x=780,y=585,relheight=0.075,relwidth=0.150)

    bg_report_income_frame = Frame(window,height=700,width=1100)
    bg_report_income_frame.place(x=0,y=0)
    
     # Create Labellogin
    Label(bg_report_income_frame,image=backg_report_income).place(x=-2,y=-2)
    Label(bg_report_income_frame,text="รายงานสรุปรายได้",font="Tahoma 20",bg="#ece1db").place(x=595,y=56,)
    #Treeview
    treeframe = Frame(bg_report_income_frame,height=390,width=740,bg="black")
    treeframe.place(x=450,y=190)
    treebar = Scrollbar(treeframe)
    treebar.pack(side=RIGHT,fill=Y)
    mytree = ttk.Treeview(treeframe,columns=("name","pricee","amountt"),height=16,yscrollcommand=treebar.set)
    mytree.pack()
    #สี
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", bd=0, font="Tahoma 12 ",fieldbackground = "#ffc9ab",background = "ffc9ab",foreground = "black")
    style.configure("Treeview.Heading", font=(None, 15),background="#d87847")
    style.map('Treeview',background = [('selected','#d87847')])
    
    treebar.config(command=mytree.yview)
    #create headings
    mytree.heading("#0",text="",anchor=W)
    mytree.heading("name",text="ชื่อ ",anchor=CENTER)
    mytree.heading("pricee",text="ราคา ",anchor=CENTER)
    mytree.heading("amountt",text="วัน/เดือน/ปี ",anchor=CENTER)

    #Format our columns
    mytree.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    mytree.column("name",anchor=W,width=300)
    mytree.column("pricee",anchor=CENTER,width=80)
    mytree.column("amountt",anchor=CENTER,width=100)


    Button(bg_report_income_frame,text='รายงานสรุปรายได้',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=115)
    Button(bg_report_income_frame,text='รายงานสรุปบอร์ดเกม',bg="#ffffff",font="Tahoma 12",command=lambda:jumpto(bg_report_income_frame,Report_Store_Boardgame()),activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=253)
    Button(bg_report_income_frame,text='รายงานสรุปรายได้เฉลี่ย',bg="#ffffff",font="Tahoma 12",command=lambda:jumpto(bg_report_income_frame,Report_amount_Boardgame()),activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=398)
    Button(bg_report_income_frame,text='ย้อนกลับ',bg="#ffffff",font="Tahoma 20",activebackground="#fff7f3",command=lambda:out_Frame(bg_report_income_frame),activeforeground="#fff7f3",compound=TOP,bd=0).place(x=34,y=543,relheight=0.099,relwidth=0.202)
    Button(bg_report_income_frame,text='ตกลง',bg="#ffffff",font="Tahoma 20",activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,bd=0,command=done).place(x=450,y=585,relheight=0.075,relwidth=0.150)
    Label(bg_report_income_frame,text="ยอดสุทธิ",font="Tahoma 18",bg="#ece1db").place(x=780,y=540,relwidth=0.150)
    


    dayCombo = ttk.Combobox(bg_report_income_frame, values=datelstday,font="Tahoma 17", justify='center',state='readonly')
    dayCombo.set('ทุกวัน')
    dayCombo.place(x=468,y=120,relheight=0.06,relwidth=0.10)

    monthCombo = ttk.Combobox(bg_report_income_frame, values=datelstmonth,font="Tahoma 17", justify='center',state='readonly')
    monthCombo.set('ทุกเดือน')
    monthCombo.bind("<<ComboboxSelected>>",serchmonth)
    monthCombo.place(x=576,y=120,relheight=0.06,relwidth=0.200)

    yearCombo = ttk.Combobox(bg_report_income_frame, values=datelstyear,font="Tahoma 17", justify='center',state='readonly')
    yearCombo.set('2565')
    yearCombo.bind("<<ComboboxSelected>>",serchmonth)
    yearCombo.place(x=795,y=120,relheight=0.06,relwidth=0.120)
    done()



def Report_Store_Boardgame():
    global conn,cursor,mytree,dayCombo
    
    def serchmonth(a):
        global dayCombo
        dayCombo.destroy()
        datelstday = ["ทุกวัน"]
        month31=['มกราคม', 'มีนาคม','พฤษภาคม','กรกฎาคม', 'สิงหาคม', 'ตุลาคม','ธันวาคม']
        if monthCombo.get() in month31:
            for i in range(1,32):
                datelstday.append(i)
        elif monthCombo.get() == 'กุมภาพันธ์':
            y=int(yearCombo.get())-543
            if (y%400 == 0 or y%4 ==0 and y%100 != 0) :
                for i in range(1,30):
                    datelstday.append(i)
            else:
                for i in range(1,29):
                    datelstday.append(i)
        elif monthCombo.get() == "ทุกเดือน":
            datelstday = []
        else:
            for i in range(1,31):
                datelstday.append(i)
        dayCombo = ttk.Combobox(bg_report_store_frame, values=datelstday,font="Tahoma 17", justify='center',state='readonly')
        dayCombo.set("ทุกวัน")
        dayCombo.place(x=468,y=120,relheight=0.06,relwidth=0.10)



    def done():
        def __init__(self, name,at):
            self.name = name
            self.at = at
        mytree.delete(*mytree.get_children()) #delete old data from treeview
        conn = sqlite3.connect('db/boardgame403.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM Reportplay ORDER BY used DESC"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result = cursor.fetchall()
        if monthCombo.get() == "ทุกเดือน":
            n=[]
            amt=[]
            all=[]
            for i,data in enumerate(result):
                new_date=data[3].split('/')
                if int(new_date[2]) == (int(yearCombo.get())-543):
                    if data[1]  not in n:
                        print(0)
                        n.append(data[1])
                        amt.append(data[2])
                    elif data[1] in n:
                        print(1)
                        x=n.index(data[1])
                        a=amt[x]
                        sum = int(data[2])+int(a)
                        del amt[x]
                        amt.insert(x,sum)
            for i in range(len(n)):
                all.append((n[i],amt[i]))
            print(n)
            print(amt)
            all=sorted(all,key=lambda __init__:__init__[1])
            print(all)
            for i in range (len(all)):
                a=all.pop()
                mytree.insert('', 'end', values=(a[0],a[1]))
        
        else:
            if dayCombo.get() == "ทุกวัน":
                n=[]
                amt=[]
                all=[]
                for i,data in enumerate(result):
                    new_date=data[3].split('/')
                    x= datelstmonth.index(monthCombo.get())
                    if int(new_date[2]) == (int(yearCombo.get())-543) and x == int(new_date[1]):
                        if data[1]  not in n:
                            print(0)
                            n.append(data[1])
                            amt.append(data[2])
                        elif data[1] in n:
                            print(1)
                            x=n.index(data[1])
                            a=amt[x]
                            sum = int(data[2])+int(a)
                            del amt[x]
                            amt.insert(x,sum)
                for i in range(len(n)):
                    all.append((n[i],amt[i]))
                print(n)
                print(amt)
                all=sorted(all,key=lambda __init__:__init__[1])
                print(all)
                for i in range (len(all)):
                    a=all.pop()
                    mytree.insert('', 'end', values=(a[0],a[1]))


            else :
                for i,data in enumerate(result):
                    new_date=data[3].split('/')
                    x= datelstmonth.index(monthCombo.get())
                    if int(new_date[2]) == (int(yearCombo.get())-543) and (x == int(new_date[1] )) and (int(new_date[0])==int(dayCombo.get())):
                        mytree.insert('', 'end', values=(data[1],data[2]))
            

    bg_report_store_frame = Frame(window,height=700,width=1100)
    bg_report_store_frame.place(x=0,y=0)
    
     # Create Labellogin
    Label(bg_report_store_frame,image=backg_report_Store).place(x=-2,y=-2)
    Label(bg_report_store_frame,text="รายงานสรุปบอร์ดเกม",font="Tahoma 20",bg="#ece1db").place(x=575,y=56)

    #Treeview
    treeframe = Frame(bg_report_store_frame,height=390,width=740,bg="black")
    treeframe.place(x=490,y=190)
    treebar = Scrollbar(treeframe)
    treebar.pack(side=RIGHT,fill=Y)
    mytree = ttk.Treeview(treeframe,columns=("name","amountt"),height=16,yscrollcommand=treebar.set)
    mytree.pack()
    #สี
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", bd=0, font="Tahoma 12 ",fieldbackground = "#ffc9ab",background = "ffc9ab",foreground = "black")
    style.configure("Treeview.Heading", font=(None, 15),background="#d87847")
    style.map('Treeview',background = [('selected','#d87847')])
    
    treebar.config(command=mytree.yview)
    #create headings
    mytree.heading("#0",text="",anchor=W)
    mytree.heading("name",text="ชื่อ",anchor=CENTER)
    mytree.heading("amountt",text="จำนวน ",anchor=CENTER)

    #Format our columns
    mytree.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    mytree.column("name",anchor=W,width=300)
    mytree.column("amountt",anchor=CENTER,width=100)

   


    Button(bg_report_store_frame,text='รายงานสรุปรายได้',bg="#ffffff",font="Tahoma 12",command=lambda:jumpto(bg_report_store_frame,Report_Income_Boardgame()),activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=115)
    Button(bg_report_store_frame,text='รายงานสรุปบอร์ดเกม',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=253)
    Button(bg_report_store_frame,text='รายงานสรุปรายได้เฉลี่ย',bg="#ffffff",font="Tahoma 12",command=lambda:jumpto(bg_report_store_frame,Report_amount_Boardgame()),activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=398)
    Button(bg_report_store_frame,text='ย้อนกลับ',bg="#ffffff",font="Tahoma 20",activebackground="#fff7f3",command=lambda:out_Frame(bg_report_store_frame),activeforeground="#fff7f3",compound=TOP,bd=0).place(x=34,y=543,relheight=0.099,relwidth=0.202)
    Button(bg_report_store_frame,text='ตกลง',bg="#ffffff",font="Tahoma 20",activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,bd=0,command=done).place(x=620,y=585,relheight=0.075,relwidth=0.150)




    dayCombo = ttk.Combobox(bg_report_store_frame, values=datelstday,font="Tahoma 17", justify='center',state='readonly')
    dayCombo.set('ทุกวัน')
    dayCombo.place(x=468,y=120,relheight=0.06,relwidth=0.10)

    monthCombo = ttk.Combobox(bg_report_store_frame, values=datelstmonth,font="Tahoma 17", justify='center',state='readonly')
    monthCombo.set('ทุกเดือน')
    monthCombo.bind("<<ComboboxSelected>>",serchmonth)
    monthCombo.place(x=576,y=120,relheight=0.06,relwidth=0.200)

    yearCombo = ttk.Combobox(bg_report_store_frame, values=datelstyear,font="Tahoma 17", justify='center',state='readonly')
    yearCombo.set('2565')
    yearCombo.bind("<<ComboboxSelected>>",serchmonth)
    yearCombo.place(x=795,y=120,relheight=0.06,relwidth=0.120)
    done()

def Report_amount_Boardgame():
    global conn,cursor,mytree,dayCombo

    allprice = StringVar()
    custo = StringVar()
    av = StringVar()

    def serchmonth(a):
        global dayCombo
        dayCombo.destroy()
        datelstday = ["ทุกวัน"]
        month31=['มกราคม', 'มีนาคม','พฤษภาคม','กรกฎาคม', 'สิงหาคม', 'ตุลาคม','ธันวาคม']
        if monthCombo.get() in month31:
            for i in range(1,32):
                datelstday.append(i)
        elif monthCombo.get() == 'กุมภาพันธ์':
            y=int(yearCombo.get())-543
            if (y%400 == 0 or y%4 ==0 and y%100 != 0) :
                for i in range(1,30):
                    datelstday.append(i)
            else:
                for i in range(1,29):
                    datelstday.append(i)
        elif monthCombo.get() == "ทุกเดือน":
            datelstday = []
        else:
            for i in range(1,31):
                datelstday.append(i)
        dayCombo = ttk.Combobox(bg_report_amount_frame, values=datelstday,font="Tahoma 17", justify='center',state='readonly')
        dayCombo.set("ทุกวัน")
        dayCombo.place(x=468,y=215,relheight=0.06,relwidth=0.10)
    
    def done():
        t=0
        c=0
        aa=0
        conn = sqlite3.connect('db/boardgame403.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM Reportavg"
        cursor.execute(sql)# ORDER BY firstname ASC")
        result = cursor.fetchall()
        for i,data in enumerate(result):
            new_date=data[4].split('/')
            if monthCombo.get() == "ทุกเดือน":
                if int(new_date[2]) == (int(yearCombo.get())-543):
                   t = t + data[1]
                   c = c + data[2]
            else:
                if dayCombo.get() == "ทุกวัน":
                    x= datelstmonth.index(monthCombo.get())
                    if int(new_date[2]) == (int(yearCombo.get())-543) and x == int(new_date[1]):
                        t = t + data[1]
                        c = c + data[2]
                else:
                    x= datelstmonth.index(monthCombo.get())
                    if int(new_date[2]) == (int(yearCombo.get())-543) and (x == int(new_date[1] )) and (int(new_date[0])==int(dayCombo.get())):
                        t = t + data[1]
                        c = c + data[2]
        if t!=0 and c !=0 :
            aa = t/c 
            allprice.set(t) 
            custo.set(c)
            av.set(f"{aa:^20.2f}")
        else:
            allprice.set(' ') 
            custo.set(' ')
            av.set(' ')


    bg_report_amount_frame = Frame(window,height=700,width=1100)
    bg_report_amount_frame.place(x=0,y=0)
    
     # Create Labellogin
    Label(bg_report_amount_frame,image=backg_report_amount).place(x=-2,y=-2)
    Label(bg_report_amount_frame,text="รายงานสรุปรายได้เฉลี่ย",font="Tahoma 20",bg="#ece1db").place(x=560,y=150)
    
    Label(bg_report_amount_frame,text="รายได้ทั้งหมด",font="Tahoma 15",bg="#f6a477").place(x=435,y=300,relheight=0.125,relwidth=0.158)
    Label(bg_report_amount_frame,text="จำนวนลูกค้า",font="Tahoma 15",bg="#f6a477").place(x=615,y=300,relheight=0.125,relwidth=0.155)
    Label(bg_report_amount_frame,text="ค่าเฉลี่ย",font="Tahoma 15",bg="#f6a477").place(x=792,y=300,relheight=0.125,relwidth=0.15)
    Label(bg_report_amount_frame,textvariable=allprice,font="Tahoma 15",bg="white").place(x=435,y=400,relheight=0.125,relwidth=0.158)
    Label(bg_report_amount_frame,textvariable=custo,font="Tahoma 15",bg="white").place(x=615,y=400,relheight=0.125,relwidth=0.155)
    Label(bg_report_amount_frame,textvariable=av,font="Tahoma 15",bg="white").place(x=792,y=400,relheight=0.125,relwidth=0.15)
    
    
    # mytree.delete(*mytree.get_children()) #delete old data from treeview
    # conn = sqlite3.connect('db/boardgame403.db')
    # cursor = conn.cursor()
    # sql = "SELECT * FROM Boardgame"
    # cursor.execute(sql)# ORDER BY firstname ASC")
    # result = cursor.fetchall()
    # for i,data in enumerate(result):
    #     mytree.insert('', 'end', values=(data[1],data[2], data[3], data[4], data[5]))

    Button(bg_report_amount_frame,text='รายงานสรุปรายได้',bg="#ffffff",font="Tahoma 12",command=lambda:jumpto(bg_report_amount_frame,Report_Income_Boardgame()),activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=115)
    Button(bg_report_amount_frame,text='รายงานสุปบอร์ดเกม',bg="#ffffff",font="Tahoma 12",command=lambda:jumpto(bg_report_amount_frame,Report_Store_Boardgame()),activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=253)
    Button(bg_report_amount_frame,text='รายงานสรุปรายได้เฉลี่ย',bg="#ffffff",font="Tahoma 12",activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,height=3,width=24,bd=0).place(x=34,y=398)
    Button(bg_report_amount_frame,text='ย้อนกลับ',bg="#ffffff",font="Tahoma 20",activebackground="#fff7f3",command=lambda:out_Frame(bg_report_amount_frame),activeforeground="#fff7f3",compound=TOP,bd=0).place(x=34,y=543,relheight=0.099,relwidth=0.202)
    Button(bg_report_amount_frame,text='ตกลง',bg="#ffffff",font="Tahoma 20",activebackground="#fff7f3",activeforeground="#fff7f3",compound=TOP,bd=0,command=done).place(x=615,y=530,relheight=0.075,relwidth=0.155)

    

    dayCombo = ttk.Combobox(bg_report_amount_frame, values=datelstday,font="Tahoma 17", justify='center',state='readonly')
    dayCombo.set("ทุกวัน")
    dayCombo.place(x=468,y=215,relheight=0.06,relwidth=0.10)

    monthCombo = ttk.Combobox(bg_report_amount_frame, values=datelstmonth,font="Tahoma 17", justify='center',state='readonly')
    monthCombo.set('ทุกเดือน')
    monthCombo.bind("<<ComboboxSelected>>",serchmonth)
    monthCombo.place(x=576,y=215,relheight=0.06,relwidth=0.200)

    yearCombo = ttk.Combobox(bg_report_amount_frame, values=datelstyear,font="Tahoma 17", justify='center',state='readonly')
    yearCombo.set('2565')
    yearCombo.bind("<<ComboboxSelected>>",serchmonth)
    yearCombo.place(x=795,y=215,relheight=0.06,relwidth=0.120)
    done()



######
def import_time() :
    global now_hour,now_min
    now = datetime.datetime.now()
    now_hour=now.strftime("%H")
    now_min=now.strftime("%M")
    #now.strftime("%H:%M")

def database() :
    global conn, cursor
    conn = sqlite3.connect('db/boardgame403.db')
    cursor = conn.cursor()

def confirm_add4_name(seat) :
    #addมาเป็นเบอร์สมาชิก
    sql="select name from Player where ta = ?and s = ?"
    cursor.execute(sql,[table_num,str(seat)])
    add = cursor.fetchall()
    for i,j in enumerate(add):
        if j[0]==None:
            name = player_entry.get()
            if (name).isdecimal() is True :
                if len(name) == 10 :
                    sql="select mb_nname from Member where mb_tel = ?"
                    cursor.execute(sql,[name])
                    result = [r for r, in cursor]
                    name =  ''.join(str(x) for x in result)
                    sql="""
                    update Player
                    set name=?,m_check = 1
                    where ta = ? and s = ?
                    """
                    cursor.execute(sql,[name,table_num,str(seat)])
                    conn.commit()
                else :
                    messagebox.showwarning("เบอร์โทรศัพท์ผิดพลาด","ไม่มีเบอร์นี้ในระบบ! โปรดกรอกใหม่อีกครั้ง")
            else :
                sql="""
                update Player
                set name=?
                where ta = ? and s = ?
                """
                cursor.execute(sql,[name,table_num,str(seat)])
                conn.commit()
        
            show4_player_name()
        else:
            messagebox.showwarning("แจ้งเตือน","ตำแหน่งนี้มีผู้เล่นแล้วไม่สามารถเพิ่มได้")
    addn_frame.destroy()

def confirm_add6_name(seat) :
    #addมาเป็นเบอร์สมาชิก
    sql="select name from Player where ta = ?and s = ?"
    cursor.execute(sql,[table_num,str(seat)])
    add = cursor.fetchall()
    for i,j in enumerate(add):
        if j[0]==None:
            name = player_entry.get()
            if (name).isdecimal() is True :
                if len(name) == 10 :
                    sql="select mb_nname from Member where mb_tel = ?"
                    cursor.execute(sql,[name])
                    result = [r for r, in cursor]
                    name =  ''.join(str(x) for x in result)
                    sql="""
                        update Player
                        set name=?,m_check = 1
                        where ta = ? and s = ?
                    """
                    cursor.execute(sql,[name,table_num,str(seat)])
                    conn.commit()
                else :
                    messagebox.showwarning("เบอร์โทรศัพท์ผิดพลาด","ไม่มีเบอร์นี้ในระบบ! โปรดกรอกใหม่อีกครั้ง")
            else :
                sql="""
                update Player
                set name=?
                where ta = ? and s = ?
                """
                
                cursor.execute(sql,[name,table_num,str(seat)])
                conn.commit()
                show6_player_name()
        else:
            messagebox.showwarning("แจ้งเตือน","ตำแหน่งนี้มีผู้เล่นแล้วไม่สามารถเพิ่มได้")
    
    addn_frame.destroy()

def add_name4(s) :
    global addn_frame,player_entry
    seat=s
    addn_frame = Frame(window,height=200,width=200)
    addn_frame.config(bg="#f8f4f2")
    addn_frame.place(x=500,y=250)
    Label(addn_frame,text="กรุณากรอกชื่อ",font="Tahoma 18",bg="#f8f4f2").grid(row=0,columnspan=2,pady=2)
    player_entry = Entry(addn_frame,font="Tahoma 18",bd=0,justify=CENTER)
    player_entry.grid(row=1,columnspan=2)
    Button(addn_frame,text="ยืนยัน",font="Tahoma 18",bd=1,command=lambda:confirm_add4_name(seat)).grid(row=2,column=0,pady=2)
    Button(addn_frame,text="ยกเลิก",font="Tahoma 18",bd=1,command=lambda:addn_frame.destroy()).grid(row=2,column=1,pady=2,padx=5)

def add_name6(s) :
    global addn_frame,player_entry
    seat=s
    addn_frame = Frame(window,height=200,width=200)
    addn_frame.config(bg="#f8f4f2")
    addn_frame.place(x=500,y=250)
    Label(addn_frame,text="กรุณากรอกชื่อ",font="Tahoma 18",bg="#f8f4f2").grid(row=0,columnspan=2,pady=2)
    player_entry = Entry(addn_frame,font="Tahoma 18",bd=0,justify=CENTER)
    player_entry.grid(row=1,columnspan=2)
    Button(addn_frame,text="ยืนยัน",font="Tahoma 18",bd=1,command=lambda:confirm_add6_name(seat)).grid(row=2,column=0,pady=2)
    Button(addn_frame,text="ยกเลิก",font="Tahoma 18",bd=1,command=lambda:addn_frame.destroy()).grid(row=2,column=1,pady=2,padx=5)

def show4_player_name() :
    sql="select name from Player where ta = ?"
    cursor.execute(sql,[table_num])
    name_table = cursor.fetchall()
    n_addSpy41.set(name_table[0])
    n_addSpy42.set(name_table[1])
    n_addSpy43.set(name_table[2])
    n_addSpy44.set(name_table[3])
    
def show6_player_name() :
    sql="select name from Player where ta = ?"
    cursor.execute(sql,[table_num])
    name_table = cursor.fetchall()
    n_addSpy61.set(name_table[0])
    n_addSpy62.set(name_table[1])
    n_addSpy63.set(name_table[2])
    n_addSpy64.set(name_table[3])
    n_addSpy65.set(name_table[4])
    n_addSpy66.set(name_table[5])
    
def start_all_bt() :
    time=now_hour+':'+now_min
    sql="""
    update Player
    set start=?
    where ta = ? and name is not null and start = 0
    """
    cursor.execute(sql,[time,table_num])
    conn.commit()
    
def stop_one_bt(t) :
    sql="select start from Player where ta = ? and  s = ?"
    cursor.execute(sql,[table_num,t])
    start_time = [r for r, in cursor]
    if start_time[0] == 0 :
        messagebox.showwarning("หยุดเวลา","ผู้เล่นนี้ยังไม่มีเวลาเริ่ม โปรดคลิกเริ่มเวลาทั้งหมดก่อนหยุดเวลา")
    else :
        time=now_hour+':'+now_min
        sql="""
        update Player
        set stop=?
        where ta = ? and s = ?
        """
        cursor.execute(sql,[time,table_num,t])
        conn.commit()
    
def stop_all_bt() :
    sql="select start,s,name from Player where ta = ?"
    cursor.execute(sql,[table_num])
    start_time = cursor.fetchall()
    for i,j in enumerate(start_time) :
        if j[0] == 0  and j[2]!= None:
            messagebox.showwarning(title="หยุดเวลา",message="ผู้เล่น "+str(j[2])+" ไม่มีเวลาเริ่ม โปรดคลิกเริ่มเวลาทั้งหมดก่อนหยุดเวลา")
        else :
            time=now_hour+':'+now_min
            sql="""
            update Player
            set stop=?
            where ta = ? and s = ? and name is not null and stop = 0
            """
            cursor.execute(sql,[time,table_num,j[1]])
            conn.commit()

def get_data(*args):
    search_str=e1.get()
    l1.delete(0,END)
    for element in game_list:
        if(re.match(search_str,element,re.IGNORECASE)):
            l1.insert(END,element)     

def select_search(e) :
    my_w = e.widget
    index = int(my_w.curselection()[0]) # position of selection
    value = my_w.get(index) # selected value 
    searchSpy.set(value) # set value for string variable of Entry 
    l1.delete(0,END)

def check_date(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return True
    return False

def report_bplay() :
    #เก็บข้อมูลเข้า report
    now = datetime.datetime.now()
    date = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
    sql="select date from Reportplay where b_name=?"
    cursor.execute(sql,[str(searchSpy.get())])
    gamed = [r for r, in cursor]
    if check_date(gamed,date) :
        sql="select used from Reportplay where b_name=? and date=?"
        cursor.execute(sql,[str(searchSpy.get()),date])
        used = [r for r, in cursor]
        new_used = int(used[0])+1
        #print('yes date')
        sql="""
            update Reportplay
            set used=?
            where b_name=? and date=?
            """
        cursor.execute(sql,[new_used,str(searchSpy.get()),date])
        conn.commit()
    else :
        #print('no date')
        sql="INSERT INTO Reportplay (b_name,used,date) VALUES (?,?,?)"
        cursor.execute(sql,[str(searchSpy.get()),1,date])
        conn.commit()

def confirm_search() :
    #อัพเดท db
    sql="select play_amt from Boardgame where bgame_name=?"
    cursor.execute(sql,[str(searchSpy.get())])
    playamt = [r for r, in cursor]
    amt=int(playamt[0])-1
    sql="""
            update Boardgame
            set play_amt=?
            where bgame_name=?
            """
    cursor.execute(sql,[amt,str(searchSpy.get())])
    conn.commit()
    sql="""
            update Bplay
            set b_name=?
            where ta=?
            """
    cursor.execute(sql,[str(searchSpy.get()),str(table_num)])
    conn.commit()
    report_bplay() 
    b_playspy.set(searchSpy.get())       
    bsearch_frame.destroy()

def bgame_search() :
    global bsearch_frame,game_list,e1,l1
    #เช็คว่ามีเกมก่อนหน้าไหม มีให้คืน
    sql="select b_name from Bplay where ta=?"
    cursor.execute(sql,[str(table_num)])
    result = [r for r, in cursor]
    if result[0] is not None :
        sql="select play_amt from Boardgame where bgame_name=?"
        cursor.execute(sql,[result[0]])
        playamt = [r for r, in cursor]
        amt=int(playamt[0])+1
        sql="""
            update Boardgame
            set play_amt=?
            where bgame_name=?
            """
        cursor.execute(sql,[amt,result[0]])
        conn.commit()
    
    sql="select bgame_name from Boardgame where play_amt!=0"
    cursor.execute(sql)
    game_list=[r for r, in cursor]
    
    bsearch_frame = Frame(window,height=500,width=500)
    bsearch_frame.config(bg="#f8f4f2")
    bsearch_frame.place(x=500,y=390)
    #autocomplete listbox
    e1=Entry(bsearch_frame,textvariable=searchSpy,font="Tahoma 18")
    e1.grid(row=1,column=1,padx=10,pady=10)
    l1=Listbox(bsearch_frame,height=6,font="Tahoma 18",relief='flat',bg="#f8f4f2",highlightcolor= 'SystemButtonFace')
    l1.grid(row=2,column=1,padx=10,pady=5)
    Button(bsearch_frame,text="ยืนยัน",font="Tahoma 18",bd=1,command=confirm_search).grid(row=3,column=1,pady=5)
    
    l1.bind('<<ListboxSelect>>', select_search)
    searchSpy.trace('w',get_data)

def cancle_game() :
    sql="select b_name from Bplay where ta=?"
    cursor.execute(sql,[str(table_num)])
    result = [r for r, in cursor]
    if result[0] is None :
        messagebox.showwarning("ยกเลิกเกม","ไม่มีข้อมูลเกมที่โต๊ะนี้")
    else :
        sql="select play_amt from Boardgame where bgame_name=?"
        cursor.execute(sql,[result[0]])
        playamt = [r for r, in cursor]
        amt=int(playamt[0])+1
        sql="""
            update Boardgame
            set play_amt=?
            where bgame_name=?
            """
        cursor.execute(sql,[amt,result[0]])
        conn.commit()
        sql="""
            update Bplay
            set b_name = null
            where ta=?
            """
        cursor.execute(sql,[str(table_num)])
        conn.commit()
        b_playspy.set("None")

 
def tables_window() :
    tables_frame = Frame(window,height=700,width=1100)
    tables_frame.place(x=0,y=0)

    def table_click(t) :
        global table_num
        table_num = t #int
        tables_frame.destroy()
        if table_num == 1 or table_num == 2 or table_num == 3: 
            add1_window()
        elif table_num == 4 or table_num == 5 or table_num == 6:
            add2_window()

    def add1_window() :
        global add1_frame
        add1_frame = Frame(window,height=700,width=1100)
        add1_frame.place(x=0,y=0)
        show4_player_name()
        Label(add1_frame,image=bgadd1).place(x=-2,y=-2)
        Label(add1_frame,text="บอร์ดเกมที่กำลังเล่น...",font="Tahoma 20",bg="#f8e4d9").place(x=70,y=570)
        Label(add1_frame,font="Tahoma 20",bg="#bdefa8",textvariable=n_addSpy41).place(x=277,y=143,relwidth=0.297,relheight=0.087)
        Label(add1_frame,font="Tahoma 20",bg="#bdefa8",textvariable=n_addSpy42).place(x=277,y=226,relwidth=0.297,relheight=0.087)
        Label(add1_frame,font="Tahoma 20",bg="#bdefa8",textvariable=n_addSpy43).place(x=277,y=309,relwidth=0.297,relheight=0.087)
        Label(add1_frame,font="Tahoma 20",bg="#bdefa8",textvariable=n_addSpy44).place(x=277,y=392,relwidth=0.297,relheight=0.087)
        Button(add1_frame,image=search1,bg="#f8e4d9",bd=0,activebackground="#f8e4d9",command=bgame_search).place(x=70,y=620)
        Button(add1_frame,image=search2,bg="#f8e4d9",bd=0,activebackground="#f8e4d9",command=cancle_game).place(x=250,y=620)

        sql="select b_name from Bplay where ta=?"
        cursor.execute(sql,[str(table_num)])
        bname=[r for r, in cursor]
        n=bname[0]
        b_playspy.set(n)    
        Label(add1_frame,font="Tahoma 20",bg="#f8e4d9",textvariable=b_playspy).place(x=350,y=570)

        Button(add1_frame,text="เพิ่ม",font="Tahoma 18",bg="#5ce1e6",bd=0,activebackground="#5ce1e6",command=lambda:add_name4(1)).place(x=165,y=149,relwidth=0.096,relheight=0.0699)
        Button(add1_frame,text="เพิ่ม",font="Tahoma 18",bg="#5ce1e6",bd=0,activebackground="#5ce1e6",command=lambda:add_name4(2)).place(x=165,y=232,relwidth=0.096,relheight=0.0699)
        Button(add1_frame,text="เพิ่ม",font="Tahoma 18",bg="#5ce1e6",bd=0,activebackground="#5ce1e6",command=lambda:add_name4(3)).place(x=165,y=315,relwidth=0.096,relheight=0.0699)
        Button(add1_frame,text="เพิ่ม",font="Tahoma 18",bg="#5ce1e6",bd=0,activebackground="#5ce1e6",command=lambda:add_name4(4)).place(x=165,y=398,relwidth=0.096,relheight=0.0699)

        Button(add1_frame,text="หยุด",font="Tahoma 18",bd=0,command=lambda:stop_one_bt(1)).place(x=607,y=146,relwidth=0.115,relheight=0.079)
        Button(add1_frame,text="หยุด",font="Tahoma 18",bd=0,command=lambda:stop_one_bt(2)).place(x=607,y=229,relwidth=0.115,relheight=0.079)
        Button(add1_frame,text="หยุด",font="Tahoma 18",bd=0,command=lambda:stop_one_bt(3)).place(x=607,y=312,relwidth=0.115,relheight=0.079)
        Button(add1_frame,text="หยุด",font="Tahoma 18",bd=0,command=lambda:stop_one_bt(4)).place(x=607,y=395,relwidth=0.115,relheight=0.079)

        Button(add1_frame,text="เริ่มทั้งหมด",font="Tahoma 18",bg="#ffde59",bd=0,activebackground="#ffde59",command=start_all_bt).place(x=866,y=145,relwidth=0.19,relheight=0.079)
        Button(add1_frame,text="หยุดทั้งหมด",font="Tahoma 18",bg="#ffde59",bd=0,activebackground="#ffde59",command=stop_all_bt).place(x=866,y=230,relwidth=0.19,relheight=0.079)
        Button(add1_frame,text="คิดค่าบริการ",font="Tahoma 18",bg="#ffde59",bd=0,activebackground="#ffde59",command=lambda:check_window(add1_frame,add1_window())).place(x=866,y=321,relwidth=0.19,relheight=0.079)
        Button(add1_frame,text="ย้อนกลับ",font="Tahoma 18",bg="#ffde59",bd=0,activebackground="#ffde59",command=lambda:jumpto(add1_frame,tables_window())).place(x=866,y=411,relwidth=0.19,relheight=0.079)

    def add2_window() :
        add2_frame = Frame(window,height=700,width=1100)
        add2_frame.place(x=0,y=0)
        Label(add2_frame,image=bgadd2).place(x=-2,y=-2)
        show6_player_name()
        Label(add2_frame,text="บอร์ดเกมที่กำลังเล่น...",font="Tahoma 20",bg="#f8e4d9").place(x=70,y=570)
        Label(add2_frame,text="",font="Tahoma 20",bg="#bdefa8",textvariable=n_addSpy61).place(x=283,y=50,relwidth=0.297,relheight=0.087)
        Label(add2_frame,text="",font="Tahoma 20",bg="#bdefa8",textvariable=n_addSpy62).place(x=283,y=135,relwidth=0.297,relheight=0.087)
        Label(add2_frame,text="",font="Tahoma 20",bg="#bdefa8",textvariable=n_addSpy63).place(x=283,y=217,relwidth=0.297,relheight=0.087)
        Label(add2_frame,text="",font="Tahoma 20",bg="#bdefa8",textvariable=n_addSpy64).place(x=283,y=300,relwidth=0.297,relheight=0.087)
        Label(add2_frame,text="",font="Tahoma 20",bg="#bdefa8",textvariable=n_addSpy65).place(x=283,y=382,relwidth=0.297,relheight=0.087)
        Label(add2_frame,text="",font="Tahoma 20",bg="#bdefa8",textvariable=n_addSpy66).place(x=283,y=466,relwidth=0.297,relheight=0.087)
        Button(add2_frame,image=search1,bg="#f8e4d9",bd=0,activebackground="#f8e4d9",command=bgame_search).place(x=70,y=620)
        Button(add2_frame,image=search2,bg="#f8e4d9",bd=0,activebackground="#f8e4d9",command=cancle_game).place(x=250,y=620)
        
        sql="select b_name from Bplay where ta=?"
        cursor.execute(sql,[str(table_num)])
        bname=[r for r, in cursor]
        n=bname[0]
        b_playspy.set(n)    
        Label(add2_frame,font="Tahoma 20",bg="#f8e4d9",textvariable=b_playspy).place(x=350,y=570)


        Button(add2_frame,text="เพิ่ม",font="Tahoma 18",bg="#5ce1e6",bd=0,activebackground="#5ce1e6",command=lambda:add_name6(1)).place(x=171,y=56,relwidth=0.097,relheight=0.0699)
        Button(add2_frame,text="เพิ่ม",font="Tahoma 18",bg="#5ce1e6",bd=0,activebackground="#5ce1e6",command=lambda:add_name6(2)).place(x=171,y=141,relwidth=0.097,relheight=0.0699)
        Button(add2_frame,text="เพิ่ม",font="Tahoma 18",bg="#5ce1e6",bd=0,activebackground="#5ce1e6",command=lambda:add_name6(3)).place(x=171,y=226,relwidth=0.096,relheight=0.0699)
        Button(add2_frame,text="เพิ่ม",font="Tahoma 18",bg="#5ce1e6",bd=0,activebackground="#5ce1e6",command=lambda:add_name6(4)).place(x=171,y=307,relwidth=0.096,relheight=0.0699)
        Button(add2_frame,text="เพิ่ม",font="Tahoma 18",bg="#5ce1e6",bd=0,activebackground="#5ce1e6",command=lambda:add_name6(5)).place(x=171,y=390,relwidth=0.096,relheight=0.0699)
        Button(add2_frame,text="เพิ่ม",font="Tahoma 18",bg="#5ce1e6",bd=0,activebackground="#5ce1e6",command=lambda:add_name6(6)).place(x=171,y=471,relwidth=0.097,relheight=0.0699)

        Button(add2_frame,text="หยุด",font="Tahoma 18",bd=0,command=lambda:stop_one_bt(1)).place(x=614,y=55,relwidth=0.115,relheight=0.079)
        Button(add2_frame,text="หยุด",font="Tahoma 18",bd=0,command=lambda:stop_one_bt(2)).place(x=614,y=138,relwidth=0.115,relheight=0.079)
        Button(add2_frame,text="หยุด",font="Tahoma 18",bd=0,command=lambda:stop_one_bt(3)).place(x=614,y=220,relwidth=0.115,relheight=0.079)
        Button(add2_frame,text="หยุด",font="Tahoma 18",bd=0,command=lambda:stop_one_bt(4)).place(x=614,y=304,relwidth=0.115,relheight=0.079)
        Button(add2_frame,text="หยุด",font="Tahoma 18",bd=0,command=lambda:stop_one_bt(5)).place(x=614,y=386,relwidth=0.115,relheight=0.079)
        Button(add2_frame,text="หยุด",font="Tahoma 18",bd=0,command=lambda:stop_one_bt(6)).place(x=614,y=469,relwidth=0.115,relheight=0.079)

        Button(add2_frame,text="เริ่มทั้งหมด",font="Tahoma 18",bg="#ffde59",bd=0,activebackground="#ffde59",command=start_all_bt).place(x=866,y=145,relwidth=0.19,relheight=0.079)
        Button(add2_frame,text="หยุดทั้งหมด",font="Tahoma 18",bg="#ffde59",bd=0,activebackground="#ffde59",command=stop_all_bt).place(x=866,y=230,relwidth=0.19,relheight=0.079)
        Button(add2_frame,text="คิดค่าบริการ",font="Tahoma 18",bg="#ffde59",bd=0,activebackground="#ffde59",command=lambda:check_window(add2_frame,add2_window())).place(x=866,y=321,relwidth=0.19,relheight=0.079)
        Button(add2_frame,text="ย้อนกลับ",font="Tahoma 18",bg="#ffde59",bd=0,activebackground="#ffde59",command=lambda:jumpto(add2_frame,tables_window())).place(x=866,y=411,relwidth=0.19,relheight=0.079)


    to = []
    per = []
    color = []
    
    for i in range(6):
        sqlite_select_query = f"SELECT * from Player WHERE ta == {i+1}"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        total = len(records)
        person = 0
        for row in records:
            if row[2] != None:
                person += 1
            
        to.append(total)
        per.append(person)
        if person > 0 and person < total:
            color.append("#5271FF")
        elif person == 0:
            color.append("#36D1B7")
        elif person == total:
            color.append("#FF7878")

    Label(tables_frame,image=bgtables).place(x=-2,y=-2)
    Label(tables_frame,text=f"{per[0]}:{to[0]}",font="Tahoma 20",bg="#fce5dd",fg=color[0]).place(x=179,y=57)
    Label(tables_frame,text=f"{per[1]}:{to[1]}",font="Tahoma 20",bg="#fce5dd",fg=color[1]).place(x=537,y=57)
    Label(tables_frame,text=f"{per[2]}:{to[2]}",font="Tahoma 20",bg="#fce5dd",fg=color[2]).place(x=887,y=57)
    Label(tables_frame,text=f"{per[3]}:{to[3]}",font="Tahoma 20",bg="#fce5dd",fg=color[3]).place(x=179,y=350)
    Label(tables_frame,text=f"{per[4]}:{to[4]}",font="Tahoma 20",bg="#fce5dd",fg=color[4]).place(x=537,y=350)
    Label(tables_frame,text=f"{per[5]}:{to[5]}",font="Tahoma 20",bg="#fce5dd",fg=color[5]).place(x=887,y=350)

    btn_t1=Button(tables_frame,image=t1,bg="#ece1db",bd=0,activebackground="#ece1db")
    btn_t1.bind("<Double-1>",lambda x:table_click(1))
    btn_t1.place(x=62,y=120)
    btn_t2=Button(tables_frame,image=t2,bg="#ece1db",bd=0,activebackground="#ece1db")
    btn_t2.bind("<Double-1>",lambda x:table_click(2))
    btn_t2.place(x=418,y=120)
    btn_t3=Button(tables_frame,image=t3,bg="#ece1db",bd=0,activebackground="#ece1db")
    btn_t3.bind("<Double-1>",lambda x:table_click(3))
    btn_t3.place(x=768,y=120)
    btn_t4=Button(tables_frame,image=t4,bg="#ece1db",bd=0,activebackground="#ece1db")
    btn_t4.bind("<Double-1>",lambda x:table_click(4))
    btn_t4.place(x=62,y=415)
    btn_t5=Button(tables_frame,image=t5,bg="#ece1db",bd=0,activebackground="#ece1db")
    btn_t5.bind("<Double-1>",lambda x:table_click(5))
    btn_t5.place(x=418,y=415)
    btn_t6=Button(tables_frame,image=t6,bg="#ece1db",bd=0,activebackground="#ece1db")
    btn_t6.bind("<Double-1>",lambda x:table_click(6))
    btn_t6.place(x=768,y=415)
    Button(tables_frame,bg="#fce5dd",text="ย้อนกลับ",font="Tahoma 20",width=8,height=1,command=lambda:jumpto(tables_frame,usermenu_admin_window())).place(x=30,y=620)

def charge_checkwin(i,pay,spy):
    if i < len(total_list) :
        change = int(pay)-total_list[i]
        spy.set(str(change)+' B')
    else :
        messagebox.showwarning("คำนวณค่าบริการ","ไม่มีข้อมูลค่าบริการ")

def reset_player():
    sql="select name from Player where ta = ? and stop != 0"
    cursor.execute(sql,[table_num])
    name = [r for r, in cursor]
    for i in range(len(name)) :
        sql="""
        update Player
        set name = null,start=0,stop=0,time=0,service_c=0,other_c=0,total=0,m_check=0
        where ta = ? and name = ?
        """
        cursor.execute(sql,[table_num,name[i]])
        conn.commit()

def done_checkwin(total) :
        if total !=0:
            te="boardgame service"
            now = datetime.datetime.now()
            date = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
            sql = "INSERT INTO Reportincome (name,price,date) VALUES (?,?,?)"
            cursor.execute(sql,[te,total,date])
            conn.commit()
            #
            num=len(total_list)
            avg="{:.3f}".format(total/num)
            sql = "INSERT INTO Reportavg (total_avg,num_avg,avg,date) VALUES (?,?,?,?)"
            cursor.execute(sql,[total,num,avg,date])
            conn.commit()
        
        reset_player()
        check_frame.destroy()
        tables_window()

def check_window(a,b) :
    global check_frame
    a.destroy()
    check_frame = Frame(window,height=700,width=1100)
    check_frame.place(x=0,y=0)
    #คิดเงินคนที่มีเวลาหยุด
    sql="select name from Player where ta = ? and stop != 0"
    cursor.execute(sql,[table_num])
    name = [r for r, in cursor]
    for i in range(len(name)) :
        #คิด time
        sql="select start,stop,m_check from Player where ta = ? and name = ?"
        cursor.execute(sql,[table_num,str(name[i])])
        time = cursor.fetchall()
        for j,m in enumerate(time) :
            #print(m[0],m[1]) --> 18:13 22:10
            start = m[0].split(':')
            stop = m[1].split(':')
            #print(start[0],stop[0]) --> 18 22
            min_start = (int(start[0])*60)+int(start[1])
            min_stop = (int(stop[0])*60)+int(stop[1])
            hr=(min_stop-min_start)//60
            left=(min_stop-min_start)%60
            if left >= 15 and left < 45 :
                hr+=0.5
            elif left >= 45 :
                hr+=1
            service=hr*30  #คิด service change
            if m[2] == 1 :
                service = int(service-hr*5)
                
            sql="""
            update Player
            set time=?,service_c=?
            where ta = ? and name = ?
            """
            cursor.execute(sql,[hr,service,table_num,str(name[i])])
            conn.commit()
    
        sql="select service_c,other_c from Player where ta = ? and name = ?"
        cursor.execute(sql,[table_num,str(name[i])])
        charge = cursor.fetchall() #(service_c-0,other_c-1)
        for o,n in enumerate(charge) :
            total=n[0]+n[1]
            sql="""
                update Player
                set total=?
                where ta = ? and name = ?
                """
            cursor.execute(sql,[total,table_num,str(name[i])])
            conn.commit()
    
    Label(check_frame,image=bgbill).place(x=-2,y=-2)
    Label(check_frame,text="ชื่อ",font="Tahoma 14",bg="#fff7f3").place(x=90,y=53)
    Label(check_frame,text="เวลา(ชม.)",font="Tahoma 14",bg="#fff7f3").place(x=207,y=53)
    Label(check_frame,text="ค่าบริการ",font="Tahoma 14",bg="#fff7f3").place(x=345,y=53)
    Label(check_frame,text="ค่าใช้จ่ายอื่น ๆ",font="Tahoma 14",bg="#fff7f3").place(x=468,y=53)
    Label(check_frame,text="รวมทั้งสิ้น",font="Tahoma 14",bg="#fff7f3").place(x=630,y=53)
    Label(check_frame,text="รับเงินมา",font="Tahoma 14",bg="#fff7f3").place(x=840,y=53)
    Label(check_frame,text="ทอน",font="Tahoma 14",bg="#fff7f3").place(x=980,y=53)
    
    p1=Entry(check_frame,font="Tahoma 18",bd=1,width=7)
    p1.place(x=830,y=110)
    p1.bind('<Return>',lambda x:charge_checkwin(0,p1.get(),c_changeSpy0))
    Label(check_frame,font="Tahoma 18",bg="#fff7f3",textvariable=c_changeSpy0).place(x=944,y=110,relwidth=0.123)
    p2=Entry(check_frame,font="Tahoma 18",bd=1,width=7)
    p2.place(x=830,y=160)
    p2.bind('<Return>',lambda x:charge_checkwin(1,p2.get(),c_changeSpy1))
    Label(check_frame,font="Tahoma 18",bg="#fff7f3",textvariable=c_changeSpy1).place(x=944,y=160,relwidth=0.123)
    p3=Entry(check_frame,font="Tahoma 18",bd=1,width=7)
    p3.place(x=830,y=210)
    p3.bind('<Return>',lambda x:charge_checkwin(2,p3.get(),c_changeSpy2))
    Label(check_frame,font="Tahoma 18",bg="#fff7f3",textvariable=c_changeSpy2).place(x=944,y=210,relwidth=0.123)
    p4=Entry(check_frame,font="Tahoma 18",bd=1,width=7)
    p4.place(x=830,y=260)
    p4.bind('<Return>',lambda x:charge_checkwin(3,p4.get(),c_changeSpy3))
    Label(check_frame,font="Tahoma 18",bg="#fff7f3",textvariable=c_changeSpy3).place(x=944,y=260,relwidth=0.123)
    p5=Entry(check_frame,font="Tahoma 18",bd=1,width=7)
    p5.place(x=830,y=310)
    p5.bind('<Return>',lambda x:charge_checkwin(4,p5.get(),c_changeSpy4))
    Label(check_frame,font="Tahoma 18",bg="#fff7f3",textvariable=c_changeSpy4).place(x=944,y=310,relwidth=0.123)
    p6=Entry(check_frame,font="Tahoma 18",bd=1,width=7)
    p6.place(x=830,y=360)
    p6.bind('<Return>',lambda x:charge_checkwin(5,p6.get(),c_changeSpy5))
    Label(check_frame,font="Tahoma 18",bg="#fff7f3",textvariable=c_changeSpy5).place(x=944,y=360,relwidth=0.123)

    Label(check_frame,text="ยอดสุทธิ",font="Tahoma 18",bg="#ece1db").place(x=200,y=500)
    #หา total รวม
    sql="select total from Player where ta = ? and stop != 0"
    cursor.execute(sql,[table_num])
    all = [r for r, in cursor]
    profit = 0
    for i in all :
        profit+=i
    Label(check_frame,text=profit,font="Tahoma 18",bg="white",width=12,height=2).place(x=350,y=490)
    Button(check_frame,bg="#ffbfbf",text="เสร็จสิ้น",font="Tahoma 20",width=8,height=1,bd=0,command=lambda:done_checkwin(profit)).place(x=930,y=620)
    Button(check_frame,bg="#ffbfbf",text="ย้อนกลับ",font="Tahoma 20",width=8,height=1,bd=0,command=lambda:jumpto(check_frame,b)).place(x=40,y=620)   

    global total_list
    total_list=[]

    sql = "SELECT * FROM Player"
    cursor.execute(sql)# ORDER BY firstname ASC")
    result_board = cursor.fetchall()
    py=110
    for i,data in enumerate(result_board):
        if int(data[0]) == table_num  and data[2] != None  and  data[3]!=0 and data[4]!=0 :
            Label(check_frame,text=data[2],font="Tahoma 18",bg="#fff7f3").place(x=32,y=py,relwidth=0.1315)
            Label(check_frame,text=data[5],font="Tahoma 18",bg="#fff7f3").place(x=180,y=py,relwidth=0.122)
            Label(check_frame,text=str(data[7])+' B',font="Tahoma 18",bg="#fff7f3").place(x=317,y=py,relwidth=0.127)
            Label(check_frame,text=str(data[8])+' B',font="Tahoma 18",bg="#fff7f3").place(x=460,y=py,relwidth=0.122)
            Label(check_frame,text=str(data[9])+' B',font="Tahoma 18",bg="#fff7f3").place(x=597,y=py,relwidth=0.1445)
            total_list.append(data[9])
            py+=50
            






# 
datelstday = []
datelstmonth = ['ทุกเดือน','มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']
datelstyear = []
for i in range(0,50):
    datelstyear.append(i+2563)
# 
IDstocklst = []
namestock_lst = []
playamt_lst = []
saleamt_lst = []
takeprice_lst = []
saleprice_lst = []


#  login_window
window = create_window()
bglogin = PhotoImage(file="bgtocode/login.png")
# adminmenu_window
bgadminmenu = PhotoImage(file="bgtocode/adminmenu.png")
iconoffice = PhotoImage(file="icon/backoffice.png")
iconstore = PhotoImage(file="icon/storesystem.png")
iconback = PhotoImage(file="icon/back.png")
# adminmenu_window
bgbackendmenu = PhotoImage(file="bgtocode/backendmenu.png")
# usermenu_admin_window
bgstorefront = PhotoImage(file="bgtocode/storefront.png")
iconrent = PhotoImage(file="icon/rent.png")
iconsell = PhotoImage(file="icon/sell.png")
iconback = PhotoImage(file="icon/back.png")
# create_window
bgboardst = PhotoImage(file="bgtocode/boardst2.png")
bgproductrg = PhotoImage(file="bgtocode/productrg2.png")
iconserch = PhotoImage(file="icon/s.png")
# 
food_icon = PhotoImage(file="icon/food.png")
drink_icon = PhotoImage(file="icon/Drink.png")
boardgame_icon = PhotoImage(file="icon/BoardGame.png")
# 
backg_Food = PhotoImage(file="bgtocode/backgroundFood.png")
backg_Drink = PhotoImage(file="bgtocode/backgroundDrink.png")
backg_Boardgame = PhotoImage(file="bgtocode/backgroundBoardgame.png")
# 
bguserregist = PhotoImage(file="bgtocode/userregist.png")
iconadd = PhotoImage(file="icon/Add.png")
iconedit = PhotoImage(file="icon/edit.png")
bgaddemploy = PhotoImage(file="bgtocode/addemploy.png")
bgeditemploy = PhotoImage(file="bgtocode/editemploy.png")
# 
createconnection()
user_login = StringVar()
password_login = StringVar()
# 
datelst=["owner","staff"]
bgmemberregist = PhotoImage(file="bgtocode/member2.png")
# 
backg_report_amount = PhotoImage(file="bgtocode/BGamountreport.png")
backg_report_income = PhotoImage(file="bgtocode/BGincomereport.png")
backg_report_Store = PhotoImage(file="bgtocode/BGstorereport.png")
# 
bggame1 = PhotoImage(file="bgtocode/8.png")
bgdrinks1 = PhotoImage(file="bgtocode/4.png")
bgfood1 = PhotoImage(file="bgtocode/6.png")
bggame2 = PhotoImage(file="bgtocode/9.png")
bgfood2 = PhotoImage(file="bgtocode/7.png")
bgdrinks2 = PhotoImage(file="bgtocode/5.png")
exitimg = PhotoImage(file="bgtocode/exitsee.png")

#imgadd
bgadd1 = PhotoImage(file="bgtocode/11.png")
search1 = PhotoImage(file="bgtocode/s1.png")
bgadd2 = PhotoImage(file="bgtocode/13.png")
search2 = PhotoImage(file="bgtocode/s2.png")
#imgcheckbill
bgbill = PhotoImage(file="bgtocode/12.png")
#imgtable
bgtables = PhotoImage(file="bgtocode/10.png")
t1 = PhotoImage(file="bgtocode/t1.png")
t2 = PhotoImage(file="bgtocode/t2.png")
t3 = PhotoImage(file="bgtocode/t3.png")
t4 = PhotoImage(file="bgtocode/t4.png")
t5 = PhotoImage(file="bgtocode/t5.png")
t6 = PhotoImage(file="bgtocode/t6.png")
#Spy
searchSpy = StringVar()
#Spy add4
n_addSpy41 = StringVar()
n_addSpy42 = StringVar()
n_addSpy43 = StringVar()
n_addSpy44 = StringVar()
b_playspy = StringVar()
#Spy add6
n_addSpy61 = StringVar()
n_addSpy62 = StringVar()
n_addSpy63 = StringVar()
n_addSpy64 = StringVar()
n_addSpy65 = StringVar()
n_addSpy66 = StringVar()
b_playspy6 = StringVar()
#Spy checkbill
c_changeSpy0 = StringVar()
c_changeSpy1 = StringVar()
c_changeSpy2 = StringVar()
c_changeSpy3 = StringVar()
c_changeSpy4 = StringVar()
c_changeSpy5 = StringVar()
database()
import_time()
login_window()
window.mainloop()