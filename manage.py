#!/usr/bin/env python3.6

# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import click

from virtualspace.utils.commands import RunGuiCommand
from virtualspace.utils.logging import setup_logging


@click.group()
def main():
    setup_logging()


@main.command()
def run_gui():
    RunGuiCommand.execute()


if __name__ == '__main__':
    main()
