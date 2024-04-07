from pydantic import BaseModel


class VideoBase(BaseModel):
    title: str
    description: str
    is_active: bool


class VideoCreate(VideoBase):
    pass


class VideoUpdate(VideoBase):
    title: str | None = None
    description: str | None = None
    is_active: bool | None = None


class Video(VideoBase):
    id: int
    file: str | None = None
    status: str | None = None

    class Config:
        orm_mode = True
