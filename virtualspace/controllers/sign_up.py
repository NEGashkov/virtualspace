from kivy.uix.screenmanager import Screen
from sqlalchemy.sql import exists

from virtualspace import settings
from virtualspace.models import Account
from virtualspace.utils.db import get_app_sa_session
from virtualspace.utils.text import capfirst
from virtualspace.utils.translation import gettext as _


class SignUpScreen(Screen):
    def do_sign_up(self, username, email, password, confirm_password):
        sa_session = get_app_sa_session()

        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

        success = self.__check(sa_session)

        if success:
            user = Account(username=username, password=password, email=email)
            sa_session.add(user)
            sa_session.commit()
            self.manager.current = settings.MENU_SCREEN_NAME

    def __check(self, sa_session):
        success = True

        if self.password != self.confirm_password:
            self.ids['confirm_password_error_label'].text = capfirst(_('passwords do not match'))
            success = False
        if sa_session.query(exists().where(Account.username == self.username)).scalar():
            self.ids['username_error_label'].text = capfirst(_('username is taken'))
            success = False

        return success
