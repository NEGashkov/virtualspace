import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, NoTransition

from virtualspace import settings
from virtualspace.controllers.menu import MenuScreen
from virtualspace.controllers.sign_in import SignInScreen
from virtualspace.controllers.sign_up import SignUpScreen


Builder.load_file(settings.KV_UI_PATH)


class VirtualSpaceApp(App):
    def build(self):
        screen_manager = ScreenManager(transition=NoTransition())

        screen_manager.add_widget(MenuScreen(name=settings.MENU_SCREEN_NAME))
        screen_manager.add_widget(SignInScreen(name=settings.SIGN_IN_SCREEN_NAME))
        screen_manager.add_widget(SignUpScreen(name=settings.SIGN_UP_SCREEN_NAME))

        screen_manager.current = settings.SIGN_IN_SCREEN_NAME

        return screen_manager
