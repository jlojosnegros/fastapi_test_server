from fastapi import FastAPI

from server_test.models import ModelName

app = FastAPI()


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
