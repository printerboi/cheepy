import datetime
from pydantic import BaseModel


class MessageModel(BaseModel):
    sender: str
    receiver: str
    content: str
    is_image: bool