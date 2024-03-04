from fastapi import FastAPI

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12"
    }
}


@app.get("/")
def index():
    return {"name": "First Data"}
