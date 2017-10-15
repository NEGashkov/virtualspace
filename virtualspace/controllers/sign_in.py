from kivy.uix.screenmanager import Screen

from virtualspace import settings
from virtualspace.models import Account
from virtualspace.utils.db import get_app_sa_session
from virtualspace.utils.models.query import get_instance_or_none
from virtualspace.utils.text import capfirst
from virtualspace.utils.translation import gettext as _


class SignInScreen(Screen):
    def do_login(self, username, password):
        sa_session = get_app_sa_session()

        self.username = username
        self.password = password

        success = self.__check(sa_session)

        if success:
            self.manager.current = settings.MENU_SCREEN_NAME

    def __check(self, sa_session):
        success = True

        query = ((Account.username == self.username) & (Account.password == self.password))
        instance = get_instance_or_none(sa_session, Account, query)

        if instance is None:
            self.ids['username_error_label'].text = capfirst(_('wrong username or password'))
            success = False
        if not self.username:
            self.ids['username_error_label'].text = capfirst(_('required field'))
            success = False
        if not self.password:
            self.ids['password_error_label'].text = capfirst(_('required field'))
            success = False

        return success
