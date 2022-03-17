import asyncio

import click
from geobook.app import run


@click.command()
def cli() -> None:
    asyncio.run(run())
