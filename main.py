from fastapi import FastAPI
from routers.channels_router import router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()
origins = [
    "http://localhost:3000",        # Next-dev
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # or ["*"] during local dev
    allow_methods=["GET", "PATCH"], # list all verbs you use
    allow_headers=["*"],            # let all headers through
)


app.include_router(router, prefix="/channels")

if __name__ == "__main__":
    uvicorn.run("main:app", port = 5000)