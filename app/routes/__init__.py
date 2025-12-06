# app/routes/__init__.py
from fastapi import FastAPI
from . import user_route


def init_routes(app: FastAPI):
    prefix = "/api/v1"
    app.include_router(user_route.router, prefix=prefix)
