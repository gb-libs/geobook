import ipaddress
import typing

import click
from click import Context, Parameter


class IpAddress(click.ParamType):
    name = 'ip address'

    def convert(
        self,
        value: typing.Any,
        param: typing.Optional['Parameter'],
        ctx: typing.Optional['Context'],
    ) -> typing.Any:

        try:
            return ipaddress.IPv4Address(value)
        except ipaddress.AddressValueError as exc:
            self.fail(f'{exc}', param, ctx)

    def __repr__(self):
        return self.name.upper()


IP_ADDRESS = IpAddress()
