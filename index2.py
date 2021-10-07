from tkinter import *
from tkinter import ttk
import pymysql


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee-ApK")
        self.root.geometry("800x600+511+30")
        picture=PhotoImage(file="teamwork.png")
        self.root.iconphoto(False,picture)
        # self.root.Icon("teamwork.png")
        self.root.configure(background="light blue")
        self.root.resizable(False,False)
        title=Label(self.root,text="Employee-Management",bg="orange")
        title.pack(fill=X)
        frame=Frame(self.root)
        frame.place(x=1,y=30,width=790,height=460)
        #:::::::WE WILL MAKE HORIZONTAL SCROLL::::
        scroll_x=Scrollbar(frame,orient=HORIZONTAL)
        #:::::::WE WILL MAKE VERTICAL SCROOL:::::
        scroll_y=Scrollbar(frame,orient=VERTICAL)

        self.Employee_Table=ttk.Treeview(frame,columns=("username","work","phone","country","gender"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set,)

        scroll_x.config(command=self.Employee_Table.xview)
        scroll_y.config(command=self.Employee_Table.yview)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        self.Employee_Table.place(x=18,y=1,width=755,height=440)
        
        #:::::::::next command we will make heading Names With Employee_Table:::::::::::

        self.Employee_Table['show']='headings'
        self.Employee_Table.heading("username",text="Emp-Username")
        self.Employee_Table.heading("work",text="Emp-Work")
        self.Employee_Table.heading("phone",text="Emp-Phone")
        self.Employee_Table.heading("country",text="Emp-Country")
        self.Employee_Table.heading("gender",text="Emp-Gender")


        #:::::::::::::::HERE::::::::::::::::::::::::::
        self.Employee_Table.column("username",width=75)
        self.Employee_Table.column("work",width=75)
        self.Employee_Table.column("phone",width=75)
        self.Employee_Table.column("country",width=75)
        self.Employee_Table.column("gender",width=75)

        #:::::::we create Field:::::::::::::::::::::::::

        self.dell=StringVar
        Entr1=Entry(self.root,width=25,textvariable=self.dell)
        Entr1.place(x=160,y=520,height=41)

        #::::::::::we create Button To delete name from filed:::::
        btn1=Button(self.root,text="Remove_Emp",width=10,height=2,command=self.Delete,bg='orange')
        btn1.place(x=76,y=520)
        
        #:::::::::::we create Button To Refresh data In Fields:::::::
        btn1=Button(self.root,text="Refresh_Data",width=10,height=2,command=self.refresh,bg='orange')
        btn1.place(x=320,y=519)
        #::::::::::we execute Fetch_data Function To be Eecuted:::::::
        self.fetch_data()

    def fetch_data(self):
        connect_with_DB=pymysql.connect(host="localhost",user="root",password="",database="data")
        cur=connect_with_DB.cursor()
        cur.execute("SELECT * FROM users")
        rows=cur.fetchall()

        if len(rows) !=0:
            self.Employee_Table.delete(*self.Employee_Table.get_children())

            for row in rows:
                self.Employee_Table.insert("",END,values=row)

            connect_with_DB.commit()
        connect_with_DB.close()

    def Delete(self):
        conn=pymysql.connect(host='localhost',user='root',password='',database='data')
        cur=conn.cursor()
        try:
             cur.execute("delete from users where username=%s",self.dell.get())
        except TypeError as e:
            print(e)


        conn.commit()

        self.fetch_data()

        conn.close()

    def refresh(self):
        self.fetch_data()
        

if __name__ == '__main__':
    root=Tk()
    os=Employee(root)
    root.mainloop()
