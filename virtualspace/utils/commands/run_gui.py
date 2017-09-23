# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from virtualspace.utils.commands.base import BaseCommand

from virtualspace.controllers.app import VirtualSpaceApp


class RunGuiCommand(BaseCommand):
    """Command to run GUI of a Virtual Space."""

    @classmethod
    def execute(cls):
        app = VirtualSpaceApp()
        app.run()
