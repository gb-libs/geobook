import click
from geobook.settings import get_config


@click.command()
def cli() -> None:
    try:
        config = get_config()
        click.secho(f'{config.TITLE} - ok', fg='green')
    except BaseException as exp:
        click.secho(f'Error: {exp}!', fg='red')
