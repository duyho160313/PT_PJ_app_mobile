from kivy import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
########################
import pandas as pd
import matplotlib.pyplot as plt


# create dictionary
data_dict = {
            'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
            'Revenue': [100, 150, 80, 200, 180]
        }
hotel_room = {
    "room1": {
        "size": "large",
        "quantity": "1 bed",
        "view": "has a beach view",
        'price': 2000
    },
    "room2": {
        "size": "small",
        "quantity": "2 bed",
        "view": "has a city view",
        'price': 1800},
    "room3": {
        "size": "normal",
        "quantity": "1 bed",
        "view": "has a city view",
        'price': 1700
        }}


class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        a = 1
        # 1. Create home screen
        main_layout = BoxLayout(orientation="vertical", padding=0, spacing=10)
        print(a)
        # a. Add label
        welcome_label = Label(text="Welcome home screen")
        main_layout.add_widget(welcome_label)
        #
        # b. Search input
        search_input = TextInput(hint_text="Search here", size_hint_y=None, height=40)
        main_layout.add_widget(search_input)
        #
        # c. Label
        label2 = Label(text="Options:")
        main_layout.add_widget(label2)
        #
        # d. Buttons
        # button_row = BoxLayout(orientation="horizontal", size_hint_y=None, height=40, spacing=10)
        # button_row.add_widget(Button(text="Button A"))
        # button_row.add_widget(Button(text="Button B"))
        # button_row.add_widget(Button(text="Button C"))
        # main_layout.add_widget(button_row)

        # e. Label
        choices = Label(text="Options:")
        main_layout.add_widget(choices)
        #
        # f. 4 buttons
        button_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height=160)

        # i. Button 1: change to Hotel screen
        button_switch_hotel = Button(text="Button: Hotel")
        button_switch_hotel.bind(on_press=self.change_screen_hotel)
        button_grid.add_widget(button_switch_hotel)
        button_switch_data = Button(text="Button: Data")
        button_switch_data.bind(on_press=self.change_screen_data)
        button_grid.add_widget(button_switch_data)

        button_grid.add_widget(Button(text="Button 3"))
        button_grid.add_widget(Button(text="Button 4"))
        main_layout.add_widget(button_grid)

        # bottom_button = BoxLayout(orientation="horizontal", size_hint_y=None, height=40, spacing=10)
        # bottom_button.add_widget(Button(text="button 1"))
        # bottom_button.add_widget(Button(text="button 2"))
        # bottom_button.add_widget(Button(text="button 3"))
        # main_layout.add_widget(bottom_button)
        self.add_widget(main_layout)

    def change_screen_hotel(self, *args):
        self.manager.current = 'screen_hotel'
    def change_screen_data(self, *args):
        self.manager.current = 'screen_data'
class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # create 1 main layout and 3 sub layout
        main_layout = BoxLayout(orientation="vertical", padding=0, spacing=10)
        welcome_layout = BoxLayout(orientation="vertical", padding=0, spacing=10)
        buttons_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=40, spacing=10)
        hotel_layout = BoxLayout(orientation="horizontal", padding=0, spacing=10)

        #add 3 subs layout in main layout
        main_layout.add_widget(welcome_layout)
        main_layout.add_widget(buttons_layout)
        main_layout.add_widget(hotel_layout)

        #create welcome text
        welcome_label = Label(text="Welcome hotel screen")
        welcome_layout.add_widget(welcome_label)

        #create image
        hotel_image = Image(source='download.jpg')
        welcome_layout.add_widget(hotel_image)


        #create buttons
        button_switch_home = (Button(text="button 1: to home screen"))
        button_switch_home.bind(on_press=self.change_screen_home)
        buttons_layout.add_widget(button_switch_home)
        button_switch_data =(Button(text="button 2: to data screen"))
        button_switch_data.bind(on_press=self.change_screen_data)
        buttons_layout.add_widget(button_switch_data)
        buttons_layout.add_widget(Button(text="button 3"))

        #create room imformation
        # room1_layout = BoxLayout(orientation="vertical", padding=0, spacing=10)
        # room1_image = Image(source='room.webp')
        # room1_layout.add_widget(room1_image)
        # room1 = Label(text="This is room 1")
        # room1_layout.add_widget(room1)
        # label1 = Label(text=hotel_room["room1"]["size"])
        # room1_layout.add_widget(label1)
        # hotel_layout.add_widget(room1_layout)
        hotel_layout.add_widget(self.CreateRoomInfor('room2.jpeg', 'This is room 2', hotel_room["room2"]))
        hotel_layout.add_widget(self.CreateRoomInfor('room2.jpeg', 'This is room 3', hotel_room["room3"]))
        hotel_layout.add_widget(self.CreateRoomInfor('room.webp', 'This is room 1',hotel_room["room1"]))

        button_book = Button(text = "book room")
        button_book.bind(on_press=self.book_room)
        hotel_layout.add_widget(button_book)

        self.add_widget(main_layout)

    def book_room(self):
        print('Booked')
    def CreateRoomInfor(self, source, text, room_data ):
        room_layout = BoxLayout(orientation="vertical", padding=0, spacing=10)
        room_image = Image(source=source)
        room_label = Label(text=text)

        book_room_button = Button(text = "book room")

        room_layout.add_widget(room_image)
        room_layout.add_widget(room_label)
        room_layout.add_widget(book_room_button)


        return room_layout


    def change_screen_data(self, *args):
        self.manager.current = 'screen_data'

    def change_screen_home(self, *args):
        self.manager.current = 'screen_home'




class Screen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        df = pd.DataFrame(data_dict)

        plt.figure(figsize=(15, 10))
        plt.plot(df['Day'], df['Revenue'], marker='*')
        plt.title("Daily Revenue")
        plt.xlabel("Day")
        plt.ylabel("Amount ($)")
        plt.grid(True)
        plt.tight_layout()

        plot_path = 'plot.png'
        plt.savefig(plot_path)
        plt.close()

        layout = BoxLayout(orientation='vertical')
        image = Image(source=plot_path)
        layout.add_widget(image)

        back_button = Button(text="Back to Home", size_hint_y=None, height=40)
        back_button.bind(on_press=self.change_screen_home)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def change_screen_home(self, *args):
        self.manager.current = 'screen_home'



class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        print("2")
        sm = MyScreenManager()
        sm.add_widget(Screen1(name='screen_home'))
        sm.add_widget(Screen2(name='screen_hotel'))
        sm.add_widget(Screen3(name='screen_data'))
        return sm



if __name__ == '__main__':
    MyApp().run()
