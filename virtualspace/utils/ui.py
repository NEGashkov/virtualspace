from kivy import Config
from kivy.lang import Builder

from virtualspace import settings


def set_up_kivy_builder():
    Builder.load_file(settings.KV_UI_PATH)


def set_up_kivy_config():
    graphics_config = {
        'width': settings.MAIN_WINDOW_WIDTH,
        'height': settings.MAIN_WINDOW_HEIGHT,
        'resizable': False
    }
    Config.setall('graphics', graphics_config)
