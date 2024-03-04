from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel



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


@app.get("/users")
async def list_users():
    return {'message': 'list users'}


@app.get("/users/me")
async def get_current_user():
    return {'Message': 'This is the current user'}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {'item_id': user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}

    if food_name.value == "fruits":
        return {"food_name": food_name, "message": "you are still healthy"}

    return {"food_name": food_name, "message": "I like chocolate"}


fake_items_db = [{"item_name": "Foo"},
                 {"item_name": "Bar"},
                 {"item_name": "Baz"}]


@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def get_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Some text"})
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    pass


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict


@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@app.get("/items")
async def read_items(q: str | None = Query(None, max_length=10)):
    results = {"items": [{"item_name": "Foo"}, {"item_name": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
