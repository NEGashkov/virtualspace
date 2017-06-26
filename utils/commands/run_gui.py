import sys
from PyQt5.QtWidgets import QApplication

from utils.commands.base import BaseCommand
from virtualspace.gui.main import MainWindow


class RunGuiCommand(BaseCommand):
    """Command to run GUI of a Virtual Space."""

    def execute(cls):
        app = QApplication(sys.argv)
        main_window = MainWindow()
        sys.exit(app.exec_())
