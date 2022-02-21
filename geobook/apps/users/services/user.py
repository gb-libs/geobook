from geobook.apps.users.managers.user import UserManager
from geobook.apps.users.models.user import UserReadModel, UserWriteModel
from geobook.apps.users.services.base import BaseUserService
from geobook.db.backends.mongodb import exceptions
from geobook.settings.common import Settings


class UserService(BaseUserService):

    def __init__(
        self,
        settings: Settings,
    ):
        self.settings = settings
        self.user_manager = UserManager(settings=settings)

    async def create_user(
            self,
            user: UserWriteModel,
    ) -> UserReadModel:
        if await self.user_manager.get_user_by_username(username=user.username):
            raise exceptions.ValidationError(
                {
                    'username': f'Username "{user.username}" is already taken, '
                                f'choose another username.',
                },
            )

        user.password = await self.get_password_hash(user=user)
        return await self.user_manager.create_user(user=user)

    async def get_password_hash(self, user: UserWriteModel) -> str:
        return self.pwd_context.hash(user.password.get_secret_value())
