import os
from dataclasses import dataclass
from pathlib import Path
from typing import IO, Any, Dict, Iterable, Optional, Union

import click
import toml
from click import Context

from decker.utils import indent_output


@dataclass(frozen=True)
class Config:
    ctx: Context
    pyproject: 'PyProjectConfig'
    line_length: int
    sources: Optional[Iterable[str]] = None
    exclude: Optional[str] = None
    verbose: bool = False

    @property
    def decker(self) -> 'PyProjectConfig':
        return self.tools.get('decker') or PyProjectConfig()

    @property
    def tools(self) -> 'PyProjectConfig':
        return self.pyproject.get('tool') or PyProjectConfig()

    @classmethod
    def create(
        cls,
        ctx: Context,
        line_length: Optional[int] = 79,
        sources: Optional[Iterable[Union[str, Path]]] = None,
        exclude: Optional[Iterable[Union[str, Path]]] = None,
        verbose: bool = False,
    ) -> 'Config':
        pyproject = PyProjectConfig.load()
        decker = pyproject.get('tool', {}).get('decker') or {}

        if not sources:
            sources = [str(module) for module in Path('.').glob('*.py')]
            if os.path.exists('src'):
                sources.append('src/')

        return cls(
            ctx=ctx,
            exclude=exclude or decker.get('exclude'),
            line_length=decker.get('line_length', line_length),
            pyproject=pyproject,
            sources=sources or decker.get('sources'),
            verbose=decker.get('verbose', verbose),
        )


class PyProjectConfig:
    def __init__(self) -> None:
        self.toml: Dict[str, Any] = {}

    def __getitem__(self, key: str) -> Any:
        return self.toml[self.normalize_key(key)]

    def __setitem__(self, key: str, value: Any) -> None:
        self.toml[self.normalize_key(key)] = value

    def __repr__(self):
        return f'<PyProjectConfig({self.toml})>'

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self.toml.get(self.normalize_key(key), default)

    @staticmethod
    def normalize_key(key: str) -> str:
        return key.replace('-', '_').strip().lower()

    @staticmethod
    def print_invalidation(file: IO, error: toml.TomlDecodeError) -> None:
        file.seek(0)
        print(click.style(' + Unable to load pyproject.toml:', fg='red'))
        with indent_output():
            for no, line in enumerate(file, 1):
                if line.startswith('['):
                    print('\b')
                print(line, end='')
                if no == error.lineno:
                    print(click.style(f'\n + ^ {error.msg}', fg='red'))

    @classmethod
    def from_dict(cls, dictionary: Dict[str, Any]) -> 'PyProjectConfig':
        config = cls()
        for key, value in dictionary.items():
            if isinstance(value, dict):
                value = cls.from_dict(value)
            config[key] = value
        return config

    @classmethod
    def load(cls, filename: str = 'pyproject.toml') -> 'PyProjectConfig':
        if not os.path.exists(filename):
            return PyProjectConfig()

        with open(filename, 'r') as file:
            try:
                return PyProjectConfig.from_dict(toml.load(file))
            except toml.TomlDecodeError as e:
                cls.print_invalidation(file, error=e)
                raise SystemExit()
