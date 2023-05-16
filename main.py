from contextvars import ContextVar
from uuid import uuid1

from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from typing import Annotated, Final, Optional

from sqlalchemy import inspect
from sqlalchemy.orm import scoped_session, sessionmaker
from starlette.requests import Request

from database import engine
from api import api_router


async def not_found(request, exc):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": [{"msg": "Not Found."}]}
    )

exception_handlers = {404: not_found}

app = FastAPI(exception_handlers=exception_handlers, openapi_url="")
app.include_router(api_router)


REQUEST_ID_CTX_KEY: Final[str] = "request_id"
_request_id_ctx_var: ContextVar[Optional[str]] = ContextVar(REQUEST_ID_CTX_KEY, default=None)


def get_request_id() -> Optional[str]:
    return _request_id_ctx_var.get()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request_id = str(uuid1())

    # we create a per-request id such that we can ensure that our session is scoped for a particular request.
    # see: https://github.com/tiangolo/fastapi/issues/726
    ctx_token = _request_id_ctx_var.set(request_id)

    # add correct schema mapping depending on the request
    # can we set some default here?
    schema_engine = engine.execution_options(
        schema_translate_map={
            None: "None",
        }
    )
    try:
        session = scoped_session(sessionmaker(autocommit=False, autoflush=False,bind=engine), scopefunc=get_request_id)
        request.state.db = session()
        # print("set request.db")
        response = await call_next(request)
    except Exception as e:
        raise e from None
    finally:
        request.state.db.close()

    _request_id_ctx_var.reset(ctx_token)
    return response

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}