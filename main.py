from fastapi import FastAPI, Query
from pydantic import BaseModel
from models.User import User
from models.Item import Item
import json

app = FastAPI()

f = open("mock_db.json")
MOCK_DATA = json.load(f)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
async def read_items(q: list[str] | None = Query(default=None, min_length=3, max_length=50)):
    results = {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}]
    }
    if q:
        results.update({"q": q})
    return results

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = Query(default=None, max_length=50)):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "item_name": item.name, 
        "item_id": item_id,
        "price": item.price}

@app.get("/users")
def get_users():
    # TODO: Get all users
    return {"data": [1,2,3,4,5]}

# In the below, user_id is typed to int so passing in a string will have fastapi validate 
@app.get("/users/{user_id}")
def get_user(user_id: int):
    # retrieve user from id
    user_from_db = filter(lambda x: x['id'] == user_id, MOCK_DATA['users'])
    # return 0th element from filter object
    db_object = list(user_from_db)[0]
    # make user model
    user = User(id = db_object['id'], username = db_object['username'])
    return user