import datetime


class Message:
    date: datetime
    sender: str
    receiver: str
    content: str
    is_image: bool

    def __init__(self, date: datetime, sender: str, receiver: str, content: str, is_image: bool):
        self.date = date
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_image = is_image
