from pydantic import UUID4
from starlite import Starlite, Controller, Partial, get, post, put, patch, delete
from datetime import datetime

from api.models.on_publish import OnPublishIn


class PublishController(Controller):
    path = "/onpublish"

    @post()
    async def publish_start(self, data: OnPublishIn) -> bool:
        print(data)
        return True


app = Starlite(route_handlers=[PublishController])
