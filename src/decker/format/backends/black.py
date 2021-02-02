import black
import click
from ramos.mixins import ThreadSafeCreateMixin

from decker.conf import Config

from .base import Formatter


class BlackBackend(ThreadSafeCreateMixin, Formatter):

    id = 'black'

    version = black.__version__

    def run(self, config: Config) -> None:
        try:
            self.run_black(config)
        except click.exceptions.Exit as e:
            if e.exit_code != 0:
                raise

    @staticmethod
    def run_black(config: Config) -> None:
        extra = config.tools
        extra = extra.get('black') or {}
        black.main.callback(
            code=None,
            check=False,
            config=None,
            diff=extra.get('diff', False),
            exclude=extra.get('exclude', config.exclude) or '',
            fast=extra.get('fast', False),
            include=extra.get('include') or '',
            line_length=extra.get('line_length', config.line_length),
            py36=None,
            pyi=extra.get('pyi', False),
            quiet=extra.get('quiet', False),
            skip_string_normalization=True,
            src=tuple(extra.get('src', config.sources)),
            target_version=extra.get('target_version'),
            verbose=extra.get('verbose', config.verbose),
        )
