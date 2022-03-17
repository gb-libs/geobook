# @cli.command()
# def shell():  # pragma: no cover
#     """Opens an interactive shell with objects auto imported"""
#     _vars = {
#         "app": app,
#         "settings": settings,
#         "User": User,
#         "engine": engine,
#         "cli": cli,
#         "create_user": create_user,
#         "select": select,
#         "session": Session(engine),
#         "Content": Content,
#     }
#     typer.echo(f"Auto imports: {list(_vars.keys())}")
#     try:
#         from IPython import start_ipython
#
#         start_ipython(argv=[], user_ns=_vars)
#     except ImportError:
#         import code
#
#         code.InteractiveConsole(_vars).interact()