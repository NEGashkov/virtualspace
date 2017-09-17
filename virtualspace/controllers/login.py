from virtualspace.models import Account
from virtualspace.utils.models.query import get_instance_or_none


class LoginController:
    model = Account

    @classmethod
    def do_login(cls, sa_session, username, password):
        success = False

        query = (Account.username == username and Account.password == password)
        instance = get_instance_or_none(sa_session, cls.model, query)

        if instance is None:
            return success

        success = True
        # TODO: Save current user somewhere.

        return success
