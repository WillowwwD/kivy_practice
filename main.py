from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label

class NotesHomeScreen(Widget):
    home_screen_label = Label(text="Hello world")


class NotesApp(App):
    def build(self):
        return NotesHomeScreen()

if __name__ == '__main__':
    NotesApp().run()