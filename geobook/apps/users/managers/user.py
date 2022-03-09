import typing

from geobook.apps.users.models.user import UserModel, UserReadModel, \
    UserWriteModel
from geobook.db.backends.mongodb import client


class UserManager(client.DatabaseClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def create_user(
            self,
            user: UserWriteModel,
    ) -> UserReadModel:
        user_collection = await self.get_collection(name=UserModel.__name__)
        row = await user_collection.insert_one(user.to_db())
        user_db = await user_collection.find_one({'_id': row.inserted_id})
        return UserReadModel.from_db(user_db)

    async def get_user_by_username(
            self,
            username: str,
    ) -> typing.Optional[UserReadModel]:
        user_collection = await self.get_collection(name=UserModel.__name__)
        user_db = await user_collection.find_one({'username': username})
        if user_db:
            return UserReadModel.from_db(user_db)

        return None
