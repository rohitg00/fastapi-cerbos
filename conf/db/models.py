from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from conf.settings import Settings

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{Settings.MYSQL_USER}:{Settings.MYSQL_PASSWORD}@"
    f"{Settings.MYSQL_HOST}:{Settings.MYSQL_PORT}/{Settings.MYSQL_DB}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Model = declarative_base()
