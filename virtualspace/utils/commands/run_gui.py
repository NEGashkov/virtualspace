# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import sys

from PyQt5.QtWidgets import QApplication

from virtualspace.gui.main import MainWindow
from virtualspace.utils.commands.base import BaseCommand


class RunGuiCommand(BaseCommand):
    """Command to run GUI of a Virtual Space."""

    @classmethod
    def execute(cls):
        app = QApplication(sys.argv)
        main_window = MainWindow()
        sys.exit(app.exec_())
