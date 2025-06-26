from kivy import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 1. Create home screen
        main_layout = BoxLayout(orientation="vertical", padding=0, spacing=10)

        # a. Add label
        welcome_label = Label(text="Welcome home screen")
        main_layout.add_widget(welcome_label)

        # b. Search input
        search_input = TextInput(hint_text="Search here", size_hint_y=None, height=40)
        main_layout.add_widget(search_input)

        # c. Label
        label2 = Label(text="Options:")
        main_layout.add_widget(label2)

        # d. Buttons
        button_row = BoxLayout(orientation="horizontal", size_hint_y=None, height=40, spacing=10)
        button_row.add_widget(Button(text="Button A"))
        button_row.add_widget(Button(text="Button B"))
        main_layout.add_widget(button_row)

        # e. Label
        choices = Label(text="Options:")
        main_layout.add_widget(choices)

        # f. 4 buttons
        button_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height=160)

        # i. Button 1: change to Hotel screen
        b1 = Button(text="Button 1: Hotel")
        b1.bind(on_press=self.change_screen)
        button_grid.add_widget(b1)

        button_grid.add_widget(Button(text="Button 2"))
        button_grid.add_widget(Button(text="Button 3"))
        button_grid.add_widget(Button(text="Button 4"))
        main_layout.add_widget(button_grid)

        bottom_button = BoxLayout(orientation="horizontal", size_hint_y=None, height=40, spacing=10)
        bottom_button.add_widget(Button(text="button 1"))
        bottom_button.add_widget(Button(text="button 2"))
        bottom_button.add_widget(Button(text="button 3"))
        main_layout.add_widget(bottom_button)
        self.add_widget(main_layout)

    def change_screen(self, *args):
        self.manager.current = 'screen2'

class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # create 1 main layout and 3 sub layout
        main_layout = BoxLayout(orientation="vertical", padding=0, spacing=10)
        welcome_layout = BoxLayout(orientation="vertical", padding=0, spacing=10)
        buttons_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=40, spacing=10)
        hotel_layout = BoxLayout(orientation="horizontal", padding=0, spacing=10)

        # create dictionary
        hotel_room = {
            "room1": {"size": "large",
                      "quantity": "1 bed",
                      "view": "has a beach view",
                      'price': 2000},
            "room2": {"size": "small",
                      "quantity": "2 bed",
                      "view": "has a city view",
                      'price': 1800}}

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
        buttons_layout.add_widget(Button(text="button 1"))
        buttons_layout.add_widget(Button(text="button 2"))
        buttons_layout.add_widget(Button(text="button 3"))


        #create room imformation
        room1_layout = BoxLayout(orientation="vertical", padding=0, spacing=10)
        room1_image = Image(source='room.webp')
        room1_layout.add_widget(room1_image)
        room1 = Label(text="This is room 1")
        room1_layout.add_widget(room1)
        label1 = Label(text=hotel_room["room1"]["size"])
        room1_layout.add_widget(label1)
        hotel_layout.add_widget(room1_layout)

        # create room2 information
        room2_layout = BoxLayout(orientation="vertical", padding=0, spacing=10)
        room2_image = Image(source='room.webp')
        room2_layout.add_widget(room2_image)
        room2 = Label(text="This is room 2")
        room2_layout.add_widget(room2)
        label2 = Label(text=hotel_room["room2"]["size"])
        room2_layout.add_widget(label2)
        hotel_layout.add_widget(room2_layout)



        # #room3
        # room2_image = Image(source='room2.jpeg')
        # hotel_layout.add_widget(room2_image)
        # room2 = Label(text="This is room 2")
        # hotel_layout.add_widget(room2)
        # label2 = Label(text=hotel_room["room2"]["view"])
        # hotel_layout.add_widget(label2)



        # main_layout.add_widget(hotel_layout)


        #
        # welcome_label = Label(text="Welcome hotel screen")
        # main_layout.add_widget(welcome_label)



        # buttons_layout.add_widget(Button(text="button 1"))
        # buttons_layout.add_widget(Button(text="button 2"))
        # buttons_layout.add_widget(Button(text="button 3"))
        # main_layout.add_widget(buttons_layout)
        #
        # room1_image = Image(source='room.webp')
        # hotel_layout.add_widget(room1_image)
        #
        # room1 = Label(text="This is room 1")
        # hotel_layout.add_widget(room1)
        #
        # hotel_room = {
        #     "room1": {"size":"large",
        #             "quantity": "1 bed",
        #             "view" : "has a beach view",
        #             'price': 2000},
        #     "room2": {"size":"small",
        #                 "quantity": "2 bed",
        #                 "view": "has a city view",
        #                 'price': 1800}
        #
        # }
        #
        # room2_image = Image(source='room2.jpeg')
        # hotel_layout.add_widget(room2_image)
        #
        # room2 = Label(text="This is room 2")
        # hotel_layout.add_widget(room2)
        #
        # label2 = Label(text=hotel_room["room2"]["view"])
        # hotel_layout.add_widget(label2)
        #
        #
        label1 = Label(text= hotel_room["room1"]["size"])
        hotel_layout.add_widget(label1)
        self.add_widget(main_layout)


    # def CreateRoomInfor(self,source, text, ):
    #     Room_layout =
    #     room_image = Image(source='room2.jpeg')
    #     hotel_layout.add_widget(room_image)
    #     room2 = Label(text="This is room 2")
    #     hotel_layout.add_widget(room2)
    #     label2 = Label(text=hotel_room["room2"]["view"])
    #     hotel_layout.add_widget(label2)

    def change_screen(self, *args):
        self.manager.current = 'screen1'

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        return sm

if __name__ == '__main__':
    MyApp().run()