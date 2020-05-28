import sys
from contextlib import contextmanager
from typing import IO, Any, Dict, List, Union

import click


def convert_parameters_to_argv(parameters: Dict[str, Any]) -> List[str]:
    argv = []
    for param, value in parameters.items():
        if value is not None:
            if isinstance(value, list):
                argv.extend(f'{param}={str(v)}' for v in value)
            elif isinstance(value, bool):
                if value:
                    argv.append(f'{param}')
            else:
                argv.append(f'{param}={value}')
    return argv


@contextmanager
def indent_output():
    stderr, stdout = sys.stderr, sys.stdout
    sys.stderr, sys.stdout = (
        IndentedOutput(file=stderr),
        IndentedOutput(file=stdout),
    )
    try:
        yield
    finally:
        sys.stderr, sys.stdout = stderr, stdout


def print_action(message: str) -> None:
    print_message(
        click.style(message, fg='yellow') + click.style(':', fg='yellow')
    )


def print_executing(message: str) -> None:
    print_message(click.style(f'Executing {message}', fg='white'))


def print_done() -> None:
    print_message(click.style('Done.', fg='yellow'))


def print_message(message: str) -> None:
    click.echo(
        click.style(' + ', fg='yellow') + message, err=True,
    )


class IndentedOutput:
    def __init__(self, file: IO, char: str = '|') -> None:
        self.file = file
        self.char = char

    def write(self, message: Union[bytes, str]) -> None:
        if isinstance(message, bytes):
            message = message.decode()

        message = message.rstrip()

        if message:
            print(
                click.style(f' {self.char}   ', fg='white'),
                file=self.file,
                end='',
            )
            print(click.style(message, fg='white'), file=self.file)

    def flush(self):
        self.file.flush()
