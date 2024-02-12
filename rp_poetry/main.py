"""
FastAPI application to serve models.
"""

from enum import Enum
from typing import Union
from fastapi import FastAPI
import uvicorn

class ModelName(str, Enum):
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.ALEXNET:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name == ModelName.LENET:
        return {"model_name": model_name, "message": "LeCNN all the images"}
    else:
        return {"model_name": model_name, "message": "Have some residuals"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/read_item/{item_id}")
async def read_item_with_query_param(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    else:
        return {"item_id": item_id}

def start():
    uvicorn.run("rp_poetry.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()
