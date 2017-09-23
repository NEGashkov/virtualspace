# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import gettext

from virtualspace import settings

translation = gettext.translation(
    domain=settings.LOCALE_DOMAIN,
    localedir=settings.LOCALE_DIR,
    languages=[settings.LANGUAGE]
)

lgettext = translation.lgettext
lngettext = translation.lngettext
gettext = translation.gettext
ngettext = translation.ngettext
