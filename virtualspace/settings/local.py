# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from .dist import *
from .vars import *

DB_DEV_URL = 'postgres+psycopg2://vs_dev:dev@localhost/virtualspace_dev'
DB_TEST_URL = 'postgres+psycopg2://vs_test:test@localhost/virtualspace_test'

DB_URL = DB_DEV_URL
