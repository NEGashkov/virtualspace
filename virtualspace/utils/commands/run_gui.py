# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from virtualspace.controllers.app import VirtualSpaceApp
from virtualspace.utils.commands.bases import BaseCommand


class RunGuiCommand(BaseCommand):
    """Command to run GUI of a Virtual Space."""

    @classmethod
    def execute(cls):
        app = VirtualSpaceApp()
        app.run()
