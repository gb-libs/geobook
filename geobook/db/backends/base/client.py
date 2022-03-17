from abc import abstractmethod


class BaseDatabaseClient:

    @abstractmethod
    def get_collection(self, collection_name: str):
        raise NotImplementedError

    @abstractmethod
    async def client(self):
        raise NotImplementedError

    @abstractmethod
    async def connection_db(self):
        raise NotImplementedError

    @abstractmethod
    async def disconnect_db(self):
        raise NotImplementedError
