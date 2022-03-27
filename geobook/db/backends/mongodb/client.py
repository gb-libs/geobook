import logging

from geobook.db.backends.base import BaseDatabaseClient
from geobook.settings.common import Settings
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection


class DatabaseClient(BaseDatabaseClient):
    def __init__(
        self,
        settings: Settings,
    ):
        self.client = None
        self.database = None
        self.settings = settings

    async def get_collection(
        self,
        name: str,
    ) -> AsyncIOMotorCollection:
        if self.database is None:
            await self.connection_db()
        return self.database.get_collection(name)

    async def client(self) -> AsyncIOMotorClient:
        if self.client is None:
            await self.connection_db()
        return self.client

    async def connection_db(self):
        logging.info('Connecting to MongoDB.')
        self.client = AsyncIOMotorClient(self.settings.DATABASE.MONGO_URI)
        self.database = self.client.get_default_database()
        logging.info('Connected to MongoDB.')

    async def disconnect_db(self):
        logging.info('Closing connection with MongoDB.')
        self.client.close()
        logging.info('Closed connection with MongoDB.')
