import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "FastAPI!"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
