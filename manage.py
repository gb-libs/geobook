import importlib
import os
import pkgutil
import typing
from pathlib import Path
from typing import List, Optional

import click
from click import Command, Context


def load_command_class(app_name: str, command_name: str):
    module = importlib.import_module(
        f'{app_name}.management.commands.{command_name}'
    )
    return module


def find_commands(management_dir: str) -> typing.List[str]:
    command_dir = os.path.join(management_dir, 'commands')
    return [
        name for _, name, is_pkg in pkgutil.iter_modules([command_dir])
        if not is_pkg and not name.startswith('_')
    ]


class ManagementCLI(click.MultiCommand):

    def list_commands(self, ctx: Context) -> List[str]:
        commands = [
            name for name in find_commands(
                os.path.join(Path(__file__).parent, 'geobook', 'management'),
            )
        ]
        commands.sort()
        return commands

    def get_command(self, ctx: Context, cmd_name: str) -> Optional[Command]:
        mod = load_command_class(app_name='geobook', command_name=cmd_name)
        return getattr(mod, 'cli', None)


def main() -> click.MultiCommand:
    app = ManagementCLI(
        name='Management CLI',
    )
    return app()


if __name__ == '__main__':
    main()
