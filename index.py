from kivy.app import App
from kivy.core import text, window
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
import mysql.connector as sql


Window.clearcolor=(100/255,0,1,0)
Window.size=(300,500)
class Demo(App):
    def build(self):
        self.title="Employes-Apk"
        self.icon="teamwork.png"
        layout=GridLayout(cols=1)
        self.Img=Image(source="employee.png")
        self.label1=Label(text='Employee',size_hint=(0.1,0.3 ))
        self.label2=Label(text="Add New Employee",size_hint=(0.1,0.3 ))
        self.username=TextInput(hint_text="Username",size_hint=(0.1,0.3 ))
        self.work=TextInput(hint_text="Work",size_hint=(0.1,0.3 ))
        self.phone=TextInput(hint_text="Phone",size_hint=(0.1,0.3 ))
        self.country=TextInput(hint_text="Country",size_hint=(0.1,0.3 ))
        self.Gender=TextInput(hint_text="Gender",size_hint=(0.1,0.3 ))
        self.button=Button(text="Register Employeed",size_hint=(0.1,0.3),on_press=self.Sub)
        
        layout.add_widget(self.Img)
        layout.add_widget(self.label1)
        layout.add_widget(self.label2)
        layout.add_widget(self.username)
        layout.add_widget(self.work)
        layout.add_widget(self.phone)
        layout.add_widget(self.country)
        layout.add_widget(self.Gender)
        layout.add_widget(self.button)
        return layout
    def Sub(self,ob):
        # define username variable::::
        un=self.username.text
        wk=self.work.text
        ph=self.phone.text
        #we define Country Variable:::
        ctr=self.country.text
        Gd=self.Gender.text

        conn=sql.connect(host='localhost',user='root',password='',database='data')
        curr=conn.cursor()
        query="Insert into users (username,work,phone,country,gender) values (%s,%s,%s,%s,%s) "
        val=(un,wk,ph,ctr,Gd)
        #AND Here We Execute Function it mean enter info to database::
        curr.execute(query,val)
        conn.commit()
        conn.close()


if __name__=='__main__':
    Demo().run()