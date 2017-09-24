from kivy.uix.screenmanager import Screen

from virtualspace import settings
from virtualspace.models import Account
from virtualspace.utils.db import get_app_sa_session
from virtualspace.utils.models.query import get_instance_or_none


class SignInScreen(Screen):
    def do_login(self, username, password):
        sa_session = get_app_sa_session()
        query = (Account.username == username and Account.password == password)
        instance = get_instance_or_none(sa_session, Account, query)

        if instance is None:
            self.manager.current = settings.SIGN_UP_SCREEN_NAME
        else:
            self.manager.current = settings.MENU_SCREEN_NAME
