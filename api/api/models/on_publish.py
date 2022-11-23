from pydantic import BaseModel, UUID4


class OnPublishIn(BaseModel):
    """
    See https://github.com/arut/nginx-rtmp-module/wiki/Directives#on_publish
    """
    call: str
    addr: str
    clientid: str
    app: str
    flashVer: str
    swfUrl: str
    tcUrl: str
    pageUrl: str
    name: str
