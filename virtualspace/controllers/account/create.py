# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import logging

from virtualspace.models import Account
from virtualspace.utils.exceptions import ValidationError

log = logging.getLogger(__name__)


class AccountCreateController:
    model = Account

    @classmethod
    def create_account(cls, sa_session, username, password, email):
        success, error_dict = True, dict()
        try:
            account = cls.model(username=username, password=password, email=email)
        except ValidationError as e:
            log.debug(e)
            success = False
            error_dict = e.error_dict
        else:
            sa_session.add(account)
            sa_session.commit()

        return success, error_dict
