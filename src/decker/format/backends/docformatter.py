import sys
from typing import Any, Dict, List

import docformatter
from ramos.mixins import ThreadSafeCreateMixin

from decker.conf import Config
from decker.utils import convert_parameters_to_argv

from .base import Formatter


class DocformatterBackend(ThreadSafeCreateMixin, Formatter):
    id = 'docformatter'

    version = docformatter.__version__

    def run(self, config: Config) -> None:
        docformatter._main(  # NOQA
            self.get_argv(config),
            standard_out=sys.stdout,
            standard_error=sys.stderr,
            standard_in=sys.stdin,
        )

    def get_argv(self, config: Config) -> List[str]:
        argv = ['']
        argv.extend(convert_parameters_to_argv(self.get_parameters(config)))
        argv.extend(config.sources)
        return argv

    @staticmethod
    def get_parameters(config: Config) -> Dict[str, Any]:
        extra = config.tools
        extra = extra.get('docformatter') or {}
        return {
            '--blank': extra.get('blank', False),
            '--check': False,
            '--exclude': extra.get('exclude', []),
            '--force-wrap': extra.get('force_wrap'),
            '--in-place': True,
            '--make-summary-multi-line': extra.get(
                'make_summary_multi_line', True
            ),
            '--pre-summary-newline': extra.get('pre_summary_newline', True),
            '--range': extra.get('range'),
            '--recursive': True,
            '--wrap-descriptions': extra.get('wrap_descriptions'),
            '--wrap-summaries': extra.get('docformatter', config.line_length),
        }
