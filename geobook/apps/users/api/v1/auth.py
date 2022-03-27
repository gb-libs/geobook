from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from geobook.apps.users.models.auth import AccessToken
from geobook.apps.users.models.user import UserReadModel, UserWriteModel
from geobook.apps.users.services.auth import AuthService
from geobook.apps.users.services.user import UserService

router = APIRouter(prefix='/auth', tags=['Auth'])
security = HTTPBearer()


@router.post(
    path='/signup',
    response_model=UserReadModel,
)
async def signup(
    user_write_model: UserWriteModel,
    user_service: UserService = Depends(),
):
    return await user_service.create_user(user=user_write_model)


@router.post(
    path='/login',
    response_model=AccessToken,
)
async def login(
    user_write_model: UserWriteModel,
    user_service: UserService = Depends(),
    auth_service: AuthService = Depends(),
):
    own_user = await user_service.get_user_by_username(user=user_write_model)

    if own_user is None:
        raise HTTPException(status_code=401, detail='Invalid username')

    if not user_service.verify_password(
        password=user_write_model.password.get_secret_value(),
        encoded_password=own_user.password.get_secret_value(),
    ):
        raise HTTPException(status_code=401, detail='Invalid password')

    return await auth_service.encode_token(username=own_user.username)


@router.get(
    path='/refresh_token',
    response_model=AccessToken,
)
async def refresh_token(
    credentials: HTTPAuthorizationCredentials = Security(security),
    auth_service: AuthService = Depends(),
):
    return auth_service.decode_token(token=credentials.credentials)
