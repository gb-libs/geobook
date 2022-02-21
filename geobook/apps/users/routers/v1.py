from fastapi import APIRouter
from geobook.apps.users.api.v1 import auth, user

router = APIRouter()
router.include_router(auth.router, prefix='/v1')
router.include_router(user.router, prefix='/v1')
