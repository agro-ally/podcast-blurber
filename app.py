from operator import truediv
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
kivy.require("2.1.0")

class SearchPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Pod Search Text"))
        self.search_val = TextInput(multiline=False)
        self.add_widget(self.search_val)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.submit_button)
        self.add_widget(Label())
        self.add_widget(self.submit)

    def submit_button(self, instance):
        s_val = self.search_val.text
        print(f"Attempting to search {s_val}")

        with open("prev_details.txt", "w") as f:
            f.write(f"search {s_val}")

class BlurberApp(App):
    def build(self):
        return SearchPage()

if __name__ == "__main__":
    BlurberApp().run()
