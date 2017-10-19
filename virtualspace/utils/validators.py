# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from virtualspace.utils.exceptions import ValidationError
from virtualspace.utils.text import capfirst
from virtualspace.utils.translation import gettext as _


class BaseValidator:
    fail_messages = tuple()

    default_fail_message = _('unknown error')

    @classmethod
    def fail(cls, field_name, key):
        fail_messages = dict(cls.fail_messages)
        fail_message = fail_messages.get(key, cls.default_fail_message)
        raise ValidationError(error_dict={field_name: capfirst(fail_message)})
