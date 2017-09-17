#!/usr/bin/env python3.6

# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import click
import logging.config

from virtualspace import settings
from virtualspace.utils.commands import RunGuiCommand


@click.group()
def main():
    logging.config.fileConfig(settings.LOGGING_INI_PATH, disable_existing_loggers=False)


@main.command()
def run_gui():
    RunGuiCommand.execute()


if __name__ == '__main__':
    main()
