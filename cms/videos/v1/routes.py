from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from fastapi import FastAPI, status, Response

from cms.videos import crud
from cms.videos.v1 import schemas
from conf.db.dependencies import get_db
from utils.auth.session import get_resource_id_from_request
from utils.auth.session import PermissionValidator

router = APIRouter()


def get_video_or_raise_exception(db: Session, video_id: int):
    db_video = crud.get_video(db, video_id=video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video


@router.get("/videos/")
def list_videos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    # videos = crud.get_videos(db, skip, limit)
    videos = []
    return videos


@router.post("/videos/")
def create_video(
    video: schemas.VideoCreate,
    db: Session = Depends(get_db),
):
    # db_video = crud.create_video(db, video=video)
    db_video = {}
    return db_video


@router.get("/videos/{resource_id}/")
def get_video(
    resource_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(
        PermissionValidator(
            action="read",
            resource_kind="video",
            get_resource_id=get_resource_id_from_request,
        )
    ),
):
    # db_video = get_video_or_raise_exception(db, resource_id)
    db_video = {}
    return db_video


@router.patch("/videos/{resource_id}/")
def update_video(
    resource_id: int,
    video: schemas.VideoUpdate,
    db: Session = Depends(get_db),
    user: dict = Depends(
        PermissionValidator(
            action="update",
            resource_kind="video",
            get_resource_id=get_resource_id_from_request,
        )
    ),
):
    # db_video = get_video_or_raise_exception(db, resource_id)
    #
    # updated_video = crud.update_video(db, db_video, video)
    updated_video = {}
    return updated_video


@router.delete("/videos/{resource_id}/")
def delete_video(
    resource_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(
        PermissionValidator(
            action="delete",
            resource_kind="video",
            get_resource_id=get_resource_id_from_request,
        )
    ),
):
    # db_video = get_video_or_raise_exception(db, resource_id)
    # crud.delete_video(db, db_video)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
