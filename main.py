
import kivy
kivy.require('2.0.0')

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'dock')


from screens import *
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Keyboard, Window
from kivy.uix.screenmanager import ScreenManager, RiseInTransition
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox

Builder.load_file('main.kv')
Builder.load_file('./KV_SCREENS/appointments.kv')
Builder.load_file('./KV_SCREENS/entry_form.kv')
Builder.load_file('./KV_SCREENS/info.kv')
Builder.load_file('./KV_SCREENS/menu_screen.kv')
Builder.load_file('./KV_SCREENS/survey.kv')

Window.size = (1024, 600)
Window.borderless = True

class MainApp(App):
    '''Contains the main app and the title of the app'''
    def build(self):
        '''Builds the app by returning the Screen Manager'''
        return MyScreenManager(transition = RiseInTransition())


if __name__ == "__main__":
    MainApp().run()
    