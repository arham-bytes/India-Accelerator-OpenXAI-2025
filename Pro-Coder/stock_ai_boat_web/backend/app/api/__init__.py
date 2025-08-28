from fastapi import APIRouter

router = APIRouter()

from . import predict, auth

router.include_router(predict.router, prefix='/predict')
router.include_router(auth.router, prefix='/auth')
