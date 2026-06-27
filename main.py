from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import tasks_router, categories_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
)

app.include_router(categories_router)
app.include_router(tasks_router)

