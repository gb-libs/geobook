from geobook.apps.users.managers.user import UserManager
from geobook.apps.users.models.user import UserReadModel, UserWriteModel
from geobook.db.backends.mongodb import exceptions
from geobook.settings import get_config
from passlib.context import CryptContext

settings = get_config()


class UserService:
    pwd_context = CryptContext(schemes=['bcrypt'])

    def __init__(self):
        self.settings = settings
        self.user_manager = UserManager(settings=settings)

    def encode_password(
            self,
            password: str,
    ) -> str:
        return self.pwd_context.hash(password)

    def verify_password(
            self,
            password: str,
            encoded_password: str,
    ) -> bool:
        return self.pwd_context.verify(password, encoded_password)

    async def create_user(
            self,
            user: UserWriteModel,
    ) -> UserReadModel:
        if await self.user_manager.get_user_by_username(username=user.username):
            raise exceptions.ValidationError(
                f'Username "{user.username}" is already taken, '
                f'choose another username.',
            )

        user.password = await self.get_password_hash(user=user)
        return await self.user_manager.create_user(user=user)

    async def get_password_hash(self, user: UserWriteModel) -> str:
        return self.pwd_context.hash(user.password.get_secret_value())

    async def get_user_by_username(
            self,
            user: UserWriteModel,
    ) -> UserReadModel:
        return await self.user_manager.get_user_by_username(
            username=user.username)
