import os
# os.environ['DISPLAY'] = ":0.0"
# os.environ['KIVY_WINDOW'] = 'egl_rpi'
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from pidev.MixPanel import MixPanel
from pidev.kivy.PassCodeScreen import PassCodeScreen
from pidev.kivy.PauseScreen import PauseScreen
from pidev.kivy import DPEAButton
from pidev.kivy import ImageButton
from pidev.kivy.selfupdatinglabel import SelfUpdatingLabel

SCREEN_MANAGER = ScreenManager()
START_SCREEN_NAME = 'start'
PLAY_SCREEN_NAME = 'play'
TYPE_SCREEN_NAME = 'type'
LEADERBOARD_SCREEN_NAME = 'leader'

class MazeGUI(App):
    def build(self):
        return SCREEN_MANAGER


Window.clearcolor = (1, 1, 1, 1)  # White


class StartScreen(Screen):
    def enter(self):
        pass
    def transition(self):
        SCREEN_MANAGER.current = PLAY_SCREEN_NAME


class PlayScreen(Screen):
    def enter(self):
        pass
    def transition(self):
        SCREEN_MANAGER.current = TYPE_SCREEN_NAME

class TypeScreen(Screen):
    def enter(self):
        pass
    def transition(self):
        SCREEN_MANAGER.current = LEADERBOARD_SCREEN_NAME


class LeaderboardScreen(Screen):
    def enter(self):
        pass
    def transition(self):
        SCREEN_MANAGER.current = START_SCREEN_NAME


Builder.load_file('Screens/StartScreen.kv')
Builder.load_file('Screens/PlayScreen.kv')
Builder.load_file('Screens/TypeScreen.kv')
Builder.load_file('Screens/LeaderboardScreen.kv')
SCREEN_MANAGER.add_widget(StartScreen(name=START_SCREEN_NAME))
SCREEN_MANAGER.add_widget(PlayScreen(name=PLAY_SCREEN_NAME))
SCREEN_MANAGER.add_widget(TypeScreen(name=TYPE_SCREEN_NAME))
SCREEN_MANAGER.add_widget(LeaderboardScreen(name=LEADERBOARD_SCREEN_NAME))
if __name__ == "__main__":
    MazeGUI().run()
