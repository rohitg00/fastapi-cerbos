from sqlalchemy.orm import Session

from cms.videos import models
from cms.videos.v1 import schemas


def get_video(db: Session, video_id: int):
    return db.query(models.Video).filter(models.Video.id == video_id).first()


def get_videos(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Video).offset(skip).limit(limit).all()


def create_video(db: Session, video: schemas.VideoCreate):
    db_video = models.Video(
        title=video.title, description=video.description, is_active=video.is_active
    )
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video


def save_updated_video(db: Session, video: models.Video):
    db.add(video)
    db.commit()
    db.refresh(video)
    return video


def update_video(db: Session, video: models.Video, updated_data: schemas.VideoUpdate):
    updated_data = updated_data.dict(exclude_unset=True)
    for key, value in updated_data.items():
        setattr(video, key, value)

    return save_updated_video(video)


def update_file_in_video(db: Session, filename: str, video: models.Video):
    video.file = filename
    return save_updated_video(video)


def update_status_in_video(db: Session, status: str, video: models.Video):
    video.status = status
    return save_updated_video(video)


def delete_video(db: Session, video: models.Model):
    db.delete(video)
    db.commit()
