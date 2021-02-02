import sys
from typing import List

import click

from decker.conf import Config
from decker.utils import print_done

from .pool import FormatterBackendPool
from .services import run_format


@click.option(
    '-b',
    '--backend',
    type=click.Choice([backend.id for backend in FormatterBackendPool.all()]),
    multiple=True,
    help='Specify formatting backends.',
)
@click.option(
    '-l',
    '--line-length',
    type=int,
    default=79,
    help='How many characters per line to allow.',
    show_default=True,
)
@click.option(
    '--exclude',
    type=str,
    default=None,
    help='Files and directories that should be excluded on recursive searches.',
)
@click.argument(
    'sources',
    nargs=-1,
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=True,
        readable=True,
        allow_dash=True,
    ),
    is_eager=True,
)
@click.command(name='format')
@click.pass_context
def format_command(
    ctx: click.Context,
    backend: List[str],
    sources: List[str],
    line_length: int,
    exclude: str,
) -> None:
    """
    Run code style format.
    """
    config = Config.create(
        ctx=ctx, sources=sources, line_length=line_length, exclude=exclude
    )

    run_format(
        config,
        backends=backend,
    )

    print_done()

    sys.exit(0)
