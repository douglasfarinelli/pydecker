import functools

import click

from decker import __version__
from decker.format.command import format_command


@click.group()
@click.version_option(message='decker==%(version)s', version=__version__)
def decker():
    """
    Welcome to Decker!

    Simple development tool that simplifies a pythonist's daily tasks.
    """


decker.add_command(format_command)

main = functools.partial(decker, auto_envvar_prefix='DECKER')
