# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.


class BaseCommand:
    """Base command to execute from manage.py script."""

    @classmethod
    def execute(cls):
        pass
