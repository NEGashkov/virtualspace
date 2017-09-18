# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import logging

from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

log = logging.getLogger(__name__)


def get_instance_or_none(sa_session, model, query):
    try:
        return sa_session.query(model).filter(query).one()
    except (MultipleResultsFound, NoResultFound) as e:
        log.debug(e)

    return None
