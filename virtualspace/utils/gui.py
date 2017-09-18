# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from PyQt5.QtWidgets import QDesktopWidget


def center_window_on_screen(window):
    desktop_widget = QDesktopWidget()
    screen_size = desktop_widget.screenGeometry()
    window_size = window.geometry()

    screen_width, screen_height = screen_size.width(), screen_size.height()
    window_width, window_height = window_size.width(), window_size.height()

    horizontal_center_px = (screen_width / 2) - (window_width / 2)
    vertical_center_px = (screen_height / 2) - (window_height / 2)

    window.move(horizontal_center_px, vertical_center_px)
