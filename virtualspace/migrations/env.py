import inspect
import logging

import os
import sys
from alembic import context
from sqlalchemy import engine_from_config, pool, MetaData
from logging.config import fileConfig

log = logging.getLogger(__name__)

try:
    from virtualspace import models, settings
    from virtualspace.models.base import BaseModel
except ImportError as e:
    log.debug(e)

    current_path = os.path.dirname(__file__)
    root = os.path.abspath(os.path.join(current_path, '..', '..'))
    sys.path.append(root)

    from virtualspace import settings
    from virtualspace import models
    from virtualspace.utils.models.base import BaseModel


# Config is an alembic .ini file with configuration.
config = context.config

fileConfig(config.config_file_name)
logger = logging.getLogger(__name__)
config.set_main_option('sqlalchemy.url', settings.DB_URL)


def get_all_models_metadata():
    metadata = []

    for name, cls in inspect.getmembers(models):
        if inspect.isclass(cls) and issubclass(cls, BaseModel):
            metadata.append(cls.metadata)

    return metadata


def combine_metadata(*args):
    m = MetaData()
    for metadata in args:
        for t in metadata.tables.values():
            t.tometadata(m)
    return m


target_metadata = combine_metadata(*get_all_models_metadata())


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL and not an Engine, though an
    Engine is acceptable here as well.  By skipping the Engine creation we
    don't even need a DB API to be available.

    Calls to context.execute() here emit the given string to the script output.

    """
    url = config.get_main_option('sqlalchemy.url')
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine and associate a connection
    with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
