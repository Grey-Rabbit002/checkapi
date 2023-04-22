from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def pri() :
    return {"Random" : "This is random text"}