# 实例化FastAPI
import os

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.staticfiles import StaticFiles

from apps import InitApps
from core.database import init_models, get_session
from core.config import settings
from core.log import log

app = FastAPI(debug=settings.DEBUG, redoc_url=None)
InitApps(app).start()

if not os.path.exists(settings.STATIC_DIR):
    os.makedirs(settings.STATIC_DIR)
app.mount('/assets', StaticFiles(directory=settings.STATIC_DIR), name=settings.STATIC_DIR)


@app.on_event('startup')
async def startup(s: AsyncSession = Depends(get_session)):
    # 初始化数据库
    await init_models(s)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=settings.PORT, reload=settings.DEBUG, workers=settings.WORKERS)
    log.info('Success to start server')
