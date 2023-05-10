from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from typing import Annotated


from stock.router import stock_router


async def not_found(request, exc):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": [{"msg": "Not Found."}]}
    )

exception_handlers = {404: not_found}

app = FastAPI(exception_handlers=exception_handlers, openapi_url="")
app.include_router(stock_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# @app.get("/stocks")
# async def get_stocks(db: Annotated[dict, Depends(get_db)]):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)