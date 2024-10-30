from fastapi import APIRouter

from .endpoints import data_api

api_router = APIRouter()

api_router.include_router(data_api.router, tags=['Data processing API'])