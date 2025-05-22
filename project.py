from kivy import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class HomeScreen(App):
    def build(self):
        main_layout = BoxLayout(orientation = "vertical", padding = 0 , spacing = 10)
        welcome_label = Label(text = "Welcome home screen")
        main_layout.add_widget(welcome_label)
        return main_layout

if __name__ == "__main__":
    HomeScreen().run()