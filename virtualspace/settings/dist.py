# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import os

PROJECT_ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LOGGING_INI_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, '..', 'logging.ini'))
KV_UI_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'ui', 'virtualspace.kv'))

LANGUAGE = 'ru'
LOCALE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'locale'))
LOCALE_DOMAIN = 'messages'
