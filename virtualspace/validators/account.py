# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from gettext import gettext as _

from virtualspace.utils.validators import BaseValidator


class AccountValidator(BaseValidator):
    MAX_USERNAME_LENGTH = 128

    CANNOT_BE_NULL = 'cannot_be_null'
    CANNOT_BE_THIS_LONG = 'cannot_be_this_long'
    CANNOT_DELETE = 'cannot_delete'

    fail_messages = (
        (CANNOT_BE_NULL, _('username cannot be null')),
        (CANNOT_BE_THIS_LONG, _('username should be shorter than {max_username_length}').format(
            max_username_length=MAX_USERNAME_LENGTH
        )),
        (CANNOT_DELETE, _('cannot delete username')),
    )

    @property
    def account_model(self):
        # TODO: Implement lazy model loading.
        from virtualspace.models import Account
        return Account

    @classmethod
    def validate_username(cls, field_name, value, is_remove):
        if not value:
            cls.fail(field_name, cls.CANNOT_BE_NULL)
        elif len(value) > cls.MAX_USERNAME_LENGTH:
            cls.fail(field_name, cls.CANNOT_BE_THIS_LONG)
        elif is_remove:
            cls.fail(field_name, cls.CANNOT_DELETE)
        # TODO: Validate uniqueness

        return value
