from fastapi import FastAPI

app = FastAPI()


@app.get("/", description="GET")
async def base_get_route():
    return {'message': 'hello world from get'}


@app.post("/")
async def post():
    return {'message': 'hello world from post'}


@app.put("/")
async def put():
    return {'message': 'hello world from put'}
