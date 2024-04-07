from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from cms.videos.v1 import routes as v1_videos_router
from conf.settings import Settings

load_dotenv()


app = FastAPI(debug=Settings.DEBUG)


app.add_middleware(
    CORSMiddleware,
    allow_origins=Settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_videos_router.router, prefix="/api/v1/cms")
