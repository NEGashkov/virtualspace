import logging

from virtualspace.models import Account
from virtualspace.utils.exceptions import ValidationError

log = logging.getLogger(__name__)


class AccountCreateController:
    model = Account

    @classmethod
    def create_account(cls, sa_session, username, password, email):
        try:
            account = cls.model(username=username, password=password, email=email)
        except ValidationError as e:
            log.debug(e)
        else:
            sa_session.add(account)
            sa_session.commit()
