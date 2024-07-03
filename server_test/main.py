from contextlib import asynccontextmanager

from fastapi import FastAPI

from server_test.models import ModelName

items = {}


@asynccontextmanager
async def lifespan(app : FastAPI):
    print("entrando")
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}

    yield
    print("saliendo")

app = FastAPI(lifespan=lifespan)

fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def main_route():
    return {"message": "Hello there!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName.ModelName):
    # REVIEW - ModelName is the name of the module here
    # (aka the python file) and ModuleName is also the
    # name of the class so that is why we need both
    if model_name is ModelName.ModelName.ALEXNET:
        return {"model_name": model_name, "message": "Depp learning"}
    if model_name is ModelName.ModelName.resnet:
        return {"model_name": model_name, "message": "LeCNN"}

    return {"model_name": model_name, "message": "residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/items_str/{item_id}")
async def read_item_id(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item hat has long description"}
        )
    return item
