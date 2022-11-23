from typing import Optional

from pydantic import BaseModel


class OnPublishIn(BaseModel):
    """
    See https://github.com/arut/nginx-rtmp-module/wiki/Directives#on_publish
    """
    call: str
    addr: str
    clientid: str
    app: str
    flashVer: Optional[str]
    swfUrl: Optional[str]
    tcUrl: Optional[str]
    pageUrl: Optional[str]
    name: str
