from kivy import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

class HomeScreen(App):
 def build(self):
  # 1. Create home screen
  main_layout = BoxLayout(orientation = "vertical", padding = 0 , spacing = 10)

  # a. Add label
  welcome_label = Label(text = "Welcome home screen")
  main_layout.add_widget(welcome_label)

  # b. Search input
  search_input = TextInput(hint_text = "Search here", size_hint_y = None, height = 40)
  main_layout.add_widget(search_input)

  # c. Label
  label2 = Label(text = "Options:")
  main_layout.add_widget(label2)

  # d. Buttons
  button_row = BoxLayout(orientation = "horizontal", size_hint_y = None, height = 40, spacing = 10)
  button_row.add_widget(Button(text = "Button A"))
  button_row.add_widget(Button(text = "Button B"))
  main_layout.add_widget(button_row)

  # e. Label
  choices = Label(text = "Options:")
  main_layout.add_widget(choices)

  # f. 4 buttons
  button_grid = GridLayout(cols = 2, spacing = 10, size_hint_y = None, height = 160)

  # i. Button 1: change to Hotel screen
  b1 = Button(text = "Button 1: Hotel")
  b1.bind(on_press = self.go_to_hotel)
  button_grid.add_widget(b1)

  button_grid.add_widget(Button(text = "Button 2"))
  button_grid.add_widget(Button(text = "Button 3"))
  button_grid.add_widget(Button(text = "Button 4"))
  main_layout.add_widget(button_grid)

  bottom_button = BoxLayout(orientation = "horizontal", size_hint_y = None, height = 40, spacing = 10)
  bottom_button.add_widget(Button(text = "button 1"))
  bottom_button.add_widget(Button(text="button 2"))
  bottom_button.add_widget(Button(text="button 3"))
  main_layout.add_widget(bottom_button)
  return main_layout

 # i. Button 1: go_to_hotel function
 def go_to_hotel(self, instance):
  self.manager.current = 'screen2'


class HotelScreen(App):
 def build(self):
  main_layout = BoxLayout(orientation="vertical", padding=0, spacing=10)
  hotel_image = Image(source='download.jpg')
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

class MyScreenManager():
 pass
class MyApp(App):
 def build(self):
  sm = MyScreenManager()
  sm.add_widget(HomeScreen(name='screen1'))
  sm.add_widget(HotelScreen(name='screen2'))
  return sm
if __name__ == "__main__":
 MyApp().run()
