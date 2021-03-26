# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
#import sqlite3

class LoginScreen(BoxLayout):

     def __init__(self, **kwargs):
         super(LoginScreen, self).__init__(**kwargs)
         #self.rows = 1
         #self.cols = 1
         self.orientation='vertical'
         self.row_default_height=20
         self.spacing=1
         self.grilla=GridLayout()
         self.grilla.row_default_height=20
         self.grilla.cols = 2         
         self.grilla.row_force_default=False
         self.grilla.row_default_height=10         
         self.grilla.add_widget(Label(text='User Name'))
         self.username = TextInput(multiline=False)
         self.grilla.add_widget(self.username)
         self.grilla.add_widget(Label(text='password'))
         self.password = TextInput(password=True, multiline=False)
         self.grilla.add_widget(self.password)
         self.add_widget(self.grilla)
  
         self.btn=Button(text='Ok')         
#         self.btn.bind(on_press=self.find_user)
         self.add_widget(self.btn)
         self.result=Label(text='Ingrese al sistema')
         self.add_widget(self.result)
         

     def find_user(self,val):
        connection = sqlite3.connect('dbdata')
        cursor = connection.cursor()
        user = self.username.text        
        cursor.execute("SELECT * FROM users WHERE usuario = '%s'" % user)        
        for row in cursor:
            
            if self.password.text==row[3]:
                self.result.text=row[1]
            else:
                self.result.text='Clave errada'

class MyApp(App):

     def build(self):
         return LoginScreen()


if __name__ == '__main__':
    MyApp().run()