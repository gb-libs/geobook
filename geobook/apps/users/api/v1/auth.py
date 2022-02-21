from fastapi import APIRouter

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/signup')
def signup():
    return 'Sign up endpoint'


@router.post('/login')
def login():
    return 'Login user endpoint'


@router.get('/refresh_token')
def refresh_token():
    return 'New token'


@router.post('/secret')
def secret_data():
    return 'Secret data'


@router.get('/notsecret')
def not_secret_data():
    return 'Not secret data'
