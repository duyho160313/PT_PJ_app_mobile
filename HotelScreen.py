from kivy import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class HotelScreen(App):
    def build(self):
        main_layout = BoxLayout(orientation = "vertical", padding = 0 , spacing = 10)
        hotel_image = Image(source ='download.jpg')
        main_layout.add_widget(hotel_image)

        welcome_label = Label(text="Welcome hotel screen")
        main_layout.add_widget(welcome_label)

        buttons = BoxLayout(orientation="horizontal", size_hint_y=None, height=40, spacing=10)
        buttons.add_widget(Button(text="button 1"))
        buttons.add_widget(Button(text="button 2"))
        buttons.add_widget(Button(text="button 3"))
        main_layout.add_widget(buttons)

        room_image = Image(source='room.webp')
        main_layout.add_widget(room_image)

        room = Label(text="This is the room")
        main_layout.add_widget(room)

        label = Label(text="..........")
        main_layout.add_widget(label)
        
        return main_layout


if __name__ == "__main__":
 HotelScreen().run()