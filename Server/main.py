from src.prisma import prisma
from fastapi.middleware.gzip import GZipMiddleware
from fastapi import FastAPI
from src.apis import users , auth , classroom , enrollment
app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)

@app.on_event("startup")
async def startup():
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(classroom.router)
app.include_router(enrollment.router)

@app.get("/")
def read_root():
    return {"version": "1.0.0"}
