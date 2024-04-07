from functools import wraps

from conf.db.models import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def with_db_session(task_func):
    @wraps(task_func)
    def session_wrapper(*args, **kwargs):
        db = SessionLocal()
        try:
            # Inject the db session into the task function
            return task_func(*args, db=db, **kwargs)
        finally:
            db.close()

    return session_wrapper
