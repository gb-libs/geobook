import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from geobook.apps.users.routers import v1 as users_routers_v1
from geobook.db.backends.mongodb.client import DatabaseClient
from geobook.settings import get_config

config = get_config()


def create_app() -> FastAPI:
    app = FastAPI(
        title=config.TITLE,
        description=config.DESCRIPTION,
        version=config.VERSION,
    )
    return app


def add_router(app: FastAPI) -> None:
    app.include_router(users_routers_v1.router, prefix='/api')


def add_event_handler(app: FastAPI) -> None:
    db_client = DatabaseClient(settings=config)

    app.add_event_handler(
        event_type='startup',
        func=db_client.connection_db,
    )

    app.add_event_handler(
        event_type='shutdown',
        func=db_client.disconnect_db,
    )


def add_middleware(app: FastAPI) -> None:
    if config.CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in config.CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


def create_server(app: FastAPI) -> uvicorn.Server:
    u_config = uvicorn.Config(
        app,
        host=f'{config.SERVER.HOST.host}',
        port=int(config.SERVER.HOST.port),
        reload=config.SERVER.IS_RELOAD,
        log_level=config.SERVER.LOG_LEVEL,
        debug=config.SERVER.IS_DEBUG,
        workers=config.SERVER.WORKER,
        limit_concurrency=config.SERVER.LIMIT_CONCURRENCY,
        limit_max_requests=config.SERVER.LIMIT_MAX_REQUESTS,
    )
    u_config.load()

    return uvicorn.Server(config=u_config)


async def run() -> None:
    app = create_app()
    add_event_handler(app)
    add_router(app)
    add_middleware(app)
    await create_server(app).serve()
