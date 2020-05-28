from typing import Any, Dict, List

from isort.main import __version__, main
from ramos.mixins import ThreadSafeCreateMixin

from decker.conf import Config
from decker.utils import convert_parameters_to_argv

from .base import Formatter


class IsortBackend(ThreadSafeCreateMixin, Formatter):

    id = 'isort'

    version = __version__

    def run(self, config: Config) -> None:
        main(argv=self.get_argv(config))

    def get_argv(self, config: Config) -> List[str]:
        argv = list(config.sources)
        argv.extend(convert_parameters_to_argv(self.get_parameters(config)))
        return argv

    @staticmethod
    def get_parameters(config: Config) -> Dict[str, Any]:
        extra = config.tools
        extra = extra.get('isort') or {}
        return {
            '--apply': True,
            '--atomic': extra.get('atomic', True),
            '--balanced': extra.get('--balanced'),
            '--builtin': extra.get('known_standard_library', []),
            '--case-sensitive': extra.get('case_sensitive', True),
            '--check-only': False,
            '--combine-as': extra.get('combine_as_imports', True),
            '--combine-star': extra.get('combine_star'),
            '--conda-env': extra.get('conda_env'),
            '--diff': extra.get('show_diff', False),
            '--dont-order-by-type': extra.get('dont_order_by_type'),
            '--dont-skip': extra.get('not_skip', ['__init__']),
            '--filter-files': extra.get('filter_files'),
            '--force-adds': extra.get('force_adds'),
            '--force-alphabetical-sort': extra.get('force_alphabetical_sort'),
            '--force-alphabetical-sort-within-sections': extra.get(
                'force_alphabetical_sort'
            ),
            '--force-grid-wrap': extra.get('force_grid_wrap'),
            '--force-single-line-imports': extra.get('force_single_line'),
            '--force-sort-within-sections': extra.get(
                'force_sort_within_sections'
            ),
            '--from-first': extra.get('from_first'),
            '--future': extra.get('known_future_library', []),
            '--ignore-whitespace': extra.get('ignore_whitespace'),
            '--indent': extra.get('indent'),
            '--jobs': extra.get('jobs'),
            '--keep-direct-and-as': extra.get('keep_direct_and_as_imports'),
            '--length-sort': extra.get('length_sort'),
            '--line-ending': extra.get('line_ending'),
            '--line-width': extra.get('line_length', config.line_length),
            '--lines-after-imports': extra.get('lines_after_imports', 2),
            '--lines-between-types': extra.get('lines_between_types'),
            '--multi-line': extra.get('multi_line_output', 3),
            '--no-inline-sort': extra.get('no_inline_sort'),
            '--no-lines-before': extra.get('no_lines_before', []),
            '--no-sections': extra.get('no_sections'),
            '--order-by-type': extra.get('--order-by-type', True),
            '--project': extra.get('known_first_party'),
            '--quiet': False,
            '--recursive': extra.get('recursive', True),
            '--remove-import': extra.get('remove_imports', ['__future__']),
            '--reverse-relative': extra.get('reverse_relative'),
            '--section-default': extra.get('default_section'),
            '--skip': extra.get('skip', []),
            '--skip-glob': extra.get('skip_glob', '*venv*'),
            '--stdout': False,
            '--thirdparty': extra.get('known_third_party', []),
            '--top': extra.get('force_to_top', []),
            '--trailing-comma': extra.get('include_trailing_comma', True),
            '--unsafe': extra.get('unsafe'),
            '--use-parentheses': extra.get('use_parentheses', True),
            '--verbose': extra.get('verbose', config.verbose),
            '--virtual-env': extra.get('virtual_env'),
            '--wrap-length': extra.get('wrap_length'),
        }
