
import kivy
kivy.require('2.0.0')

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'dock')

from screens import *
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import VKeyboardPatch
from kivy.uix.screenmanager import RiseInTransition

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
