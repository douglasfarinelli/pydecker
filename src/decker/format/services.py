from typing import List, Optional

from decker.conf import Config
from decker.utils import indent_output, print_action, print_executing

from .pool import FormatterBackendPool


def run_format(config: Config, backends: Optional[List[str]] = None):
    formatting_config = config.decker.get('formatting', {})
    backends = backends or formatting_config.get('backends') or None

    print_action(f'Formatting "{" ".join(config.sources)}"')
    for backend in FormatterBackendPool.all():
        if backends and backend.id not in backends:
            continue
        print_executing(backend.display)
        with indent_output():
            backend.run(config)
