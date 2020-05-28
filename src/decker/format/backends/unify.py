import sys
from typing import Any, Dict, List

import unify
from ramos.mixins import ThreadSafeCreateMixin

from decker.conf import Config
from decker.utils import convert_parameters_to_argv

from .base import Formatter


class UnifyBackend(ThreadSafeCreateMixin, Formatter):
    id = 'unify'

    version = unify.__version__

    def run(self, config: Config) -> None:
        unify._main(  # NOQA
            self.get_argv(config),
            standard_out=sys.stdout,
            standard_error=sys.stderr,
        )

    def get_argv(self, config: Config) -> List[str]:
        argv = ['']
        argv.extend(convert_parameters_to_argv(self.get_parameters(config)))
        argv.extend(config.sources)
        return argv

    @staticmethod
    def get_parameters(config: Config) -> Dict[str, Any]:
        extra = config.tools
        extra = extra.get('unify') or {}
        return {
            '--check-only': False,
            '--in-place': True,
            '--quote': extra.get('quote', "'"),
            '--recursive': True,
        }
