from fastapi import APIRouter

view = APIRouter()


@view.get("/upload")
async def upload():
    return {"message": "Hello World"}
