from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hi"}

@app.get("/health")
def heath_check():
    return {"health": "Ok"}