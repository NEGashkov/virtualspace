#!/usr/bin/env python3.6

# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import click

from utils.commands.run_gui import RunGuiCommand


@click.group()
def main():
    pass


@main.command()
def run_gui():
    command = RunGuiCommand()
    command.execute()


if __name__ == '__main__':
    main()
