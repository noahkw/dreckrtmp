import logging

from starlite import Starlite, Controller, post, Request, Response, Body, RequestEncodingType
from starlite.status_codes import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST
from starlite.utils import create_exception_response

from api.models.on_publish import OnPublishIn

logger = logging.getLogger(__name__)


def logging_exception_handler(request: Request, exc: Exception) -> Response:
    """
    Logs exception and returns appropriate response.

    Parameters
    ----------
    request : Request
        The request that caused the exception.
    exc :
        The exception caught by the Starlite exception handling middleware and passed to the
        callback.

    Returns
    -------
    Response
    """
    logger.error("Application Exception", exc_info=exc)
    return create_exception_response(exc)


class PublishController(Controller):
    path = "/onpublish"

    @post()
    async def publish_start(self, data: OnPublishIn = Body(media_type=RequestEncodingType.MULTI_PART)) -> bool:
        print(data)
        # Add auth
        return True


app = Starlite(route_handlers=[PublishController],
               exception_handlers={HTTP_500_INTERNAL_SERVER_ERROR: logging_exception_handler,
                                   HTTP_400_BAD_REQUEST: logging_exception_handler})
