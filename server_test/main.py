from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_route():
    return {"message": "Hello there!"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
