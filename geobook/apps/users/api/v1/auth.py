from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from geobook.apps.users.models.auth import AccessToken
from geobook.apps.users.models.user import UserReadModel, UserWriteModel
from geobook.apps.users.services.auth import AuthService
from geobook.apps.users.services.user import UserService
from geobook.settings import get_config

router = APIRouter(prefix='/auth', tags=['Auth'])
settings = get_config()
security = HTTPBearer()


@router.post(
    path='/signup',
    response_model=UserReadModel,
)
async def signup(
        user_write_model: UserWriteModel,
        user_service: UserService(settings=settings) = Depends()
):
    new_user = await user_service.create_user(user=user_write_model)
    return new_user


@router.post(
    path='/login',
    response_model=AccessToken,
)
async def login(
        user_write_model: UserWriteModel,
        user_service: UserService(settings=settings) = Depends(),
        auth_service: AuthService(settings=settings) = Depends(),
):
    own_user = await user_service.get_user_by_username(user=user_write_model)

    if own_user is None:
        return HTTPException(status_code=401, detail='Invalid username')

    if not user_service.verify_password(
            password=user_write_model.password,
            encoded_password=own_user.password,
    ):
        return HTTPException(status_code=401, detail='Invalid password')

    return await auth_service.encode_token(username=own_user.username)


@router.get(
    path='/refresh_token',
    response_model=AccessToken,
)
async def refresh_token(
        credentials: HTTPAuthorizationCredentials = Security(security),
        auth_service: AuthService(settings=settings) = Depends(),
):
    return auth_service.decode_token(token=credentials.credentials)
