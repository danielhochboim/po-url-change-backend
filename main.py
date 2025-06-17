from fastapi import FastAPI
from routers.channels_router import router
from fastapi.middleware.cors import CORSMiddleware


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