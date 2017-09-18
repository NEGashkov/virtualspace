# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
import logging

from PyQt5.QtWidgets import QWidget, QGridLayout

log = logging.getLogger(__name__)


class BaseView(QWidget):
    controller = None

    grid = tuple()

    def __init__(self, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.init_widgets()
        self.connect_buttons()
        self.init_layout()

    def init_widgets(self):
        self.init_labels()
        self.init_line_edits()
        self.init_buttons()

    def init_labels(self):
        pass

    def init_line_edits(self):
        pass

    def init_buttons(self):
        pass

    def connect_buttons(self):
        pass

    def init_layout(self):
        self.layout = QGridLayout(self)

        for row, widgets in enumerate(self.grid):
            for col, widget_data in enumerate(widgets):
                if isinstance(widget_data, tuple):
                    widget_str, row_span, col_span = widget_data
                elif isinstance(widget_data, str):
                    widget_str = widget_data
                    row_span, col_span = 1, 1
                else:
                    log.error('Wrong widget data for grid layout: {widget_data}'.format(widget_data=widget_data))
                    continue

                widget = getattr(self, widget_str, None)
                if widget is None:
                    log.error('Cannot fetch widget {widget_str} for {cls}'.format(
                        widget_str=widget_str, cls=self.__class__.__name__)
                    )
                else:
                    self.layout.addWidget(widget, row, col, row_span, col_span)

    @property
    def stacked_widget(self):
        return self.parentWidget()

    @property
    def main_window(self):
        return self.stacked_widget.parentWidget()

    @property
    def sa_session(self):
        return self.main_window.sa_session
