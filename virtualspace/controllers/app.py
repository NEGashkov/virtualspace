# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition

from virtualspace import settings
from virtualspace.controllers.menu import MenuScreen
from virtualspace.controllers.sign_in import SignInScreen
from virtualspace.controllers.sign_up import SignUpScreen
from virtualspace.utils.db import get_new_sa_session
from virtualspace.utils.ui import set_up_kivy_config, set_up_kivy_builder


set_up_kivy_builder()
set_up_kivy_config()


class VirtualSpaceApp(App):
    @property
    def sa_session(self):
        return get_new_sa_session()

    def build(self):
        screen_manager = ScreenManager(transition=NoTransition())

        screen_manager.add_widget(MenuScreen(name=settings.MENU_SCREEN_NAME))
        screen_manager.add_widget(SignInScreen(name=settings.SIGN_IN_SCREEN_NAME))
        screen_manager.add_widget(SignUpScreen(name=settings.SIGN_UP_SCREEN_NAME))

        screen_manager.current = settings.SIGN_IN_SCREEN_NAME

        return screen_manager
