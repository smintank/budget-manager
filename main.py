from fastapi import FastAPI
import uvicorn

from api.v1.budget.views import router as budget_router
from api.v1.users.views import router as user_router
from core.database import create_tables

app = FastAPI()
app.include_router(budget_router, tags=['Budget'])
app.include_router(user_router, tags=['User'])


@app.on_event("startup")
async def on_startup():
    await create_tables()

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
