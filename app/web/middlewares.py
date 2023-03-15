import typing
from aiohttp_apispec import validation_middleware

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_middlewares(app: "Application"):
    app.middlewares.append(validation_middleware)
