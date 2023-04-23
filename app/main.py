from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import post
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def pri() :
    return {"Random" : "This is updated random text"}


app.include_router(post.route)