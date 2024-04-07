from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from conf.db.models import Model


class StatusChoice:
    NOT_PROCESSED = "NOT_PROCESSED"
    PROCESSED = "PROCESSED"
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"


class Video(Model):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    file = Column(String)
    status = Column(String, default=StatusChoice.NOT_PROCESSED)
