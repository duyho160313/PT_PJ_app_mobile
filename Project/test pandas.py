from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import pandas as pd

class DataFrameViewer(App):
    def build(self):
        # Create a sample DataFrame
        data = {'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']}
        df = pd.DataFrame(data)

        # Create a GridLayout
        grid = GridLayout(cols=df.shape[1], size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height')) # Adjust height based on content

        # Add headers
        for col in df.columns:
            grid.add_widget(Label(text=str(col), bold=True))

        # Add data rows
        for index, row in df.iterrows():
            for value in row:
                grid.add_widget(Label(text=str(value)))

        # Embed the GridLayout in a ScrollView
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(grid)

        return scroll_view

if __name__ == '__main__':
    DataFrameViewer().run()