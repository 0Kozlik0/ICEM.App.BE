from fastapi import APIRouter

from .endpoints import test_apy

api_router = APIRouter()

api_router.include_router(test_apy.router, tags=['Test API'])

# api_router.include_router(mc.router, tags=['Mitosis detection'])