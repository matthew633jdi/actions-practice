from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/greeting")
def read_greeting():
    return {'Greeting': 'Wow'}

@app.get("/health")
def heath_check():
    return {"Health": "ok"}