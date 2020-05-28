import sys
from typing import Any, Dict, List

import autoflake
from ramos.mixins import ThreadSafeCreateMixin

from decker.conf import Config
from decker.utils import convert_parameters_to_argv

from .base import Formatter


class AutoflakeBackend(ThreadSafeCreateMixin, Formatter):
    id = 'autoflake'

    version = autoflake.__version__

    def run(self, config: Config) -> None:
        autoflake._main(  # NOQA
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
        extra = extra.get('autoflake') or {}
        return {
            '--check': False,
            '--exclude': extra.get('exclude', []),
            '--expand-star-imports': extra.get('expand_star_imports', True),
            '--ignore-init-module-imports': extra.get(
                'ignore_init_module_imports'
            ),
            '--imports': extra.get('imports'),
            '--in-place': True,
            '--recursive': True,
            '--remove-all-unused-imports': extra.get(
                'remove_all_unused_imports', True
            ),
            '--remove-duplicate-keys': extra.get('remove_duplicate_keys'),
            '--remove-unused-variables': extra.get(
                'remove_unused_variables', True
            ),
        }
