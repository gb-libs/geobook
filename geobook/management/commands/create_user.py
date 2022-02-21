import asyncio

import click
from geobook.apps.users.models.user import UserWriteModel
from geobook.apps.users.services.user import UserService
from geobook.settings import get_config

settings = get_config()


@click.command()
@click.option(
    '--username',
    '-u',
    prompt=True,
    type=str,
    help='Username for new user.',
)
@click.option(
    '--password',
    '-p',
    prompt=True,
    type=str,
    hide_input=True,
    confirmation_prompt=True,
    help='Password for new user.'
)
def cli(username, password) -> None:
    user_service = UserService(settings=settings)
    asyncio.run(
        user_service.create_user(
            user=UserWriteModel(username=username, password=password),
        ),
    )
    click.secho(f'add username: {username}', fg='green')
