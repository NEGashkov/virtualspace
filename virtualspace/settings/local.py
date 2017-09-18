# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from .dist import *

DB_DEV_URL = 'postgres+psycopg2://vs_dev:dev@localhost/virtualspace_dev'
DB_TEST_URL = 'postgres+psycopg2://vs_test:test@localhost/virtualspace_test'

DB_SQLITE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'data', 'sqlite.db'))
DB_SQLITE_URL = 'sqlite:///{absolute_path}'.format(absolute_path=DB_SQLITE_PATH)

DB_URL = DB_SQLITE_URL

