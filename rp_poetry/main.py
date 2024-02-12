"""
FastAPI application to serve models.
"""

from enum import Enum
from typing import Union
from fastapi import FastAPI
import uvicorn

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class ModelName(str, Enum):
    """
    Enumeration class for specifying model names.

    This class represents a set of predefined model names that can be used in the application.
    It inherits from the `Enum` class and defines constants for commonly used model names.

    Attributes:
        ALEXNET (str): Constant representing the 'alexnet' model.
        RESNET (str): Constant representing the 'resnet' model.
        LENET (str): Constant representing the 'lenet' model.
    """
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"

app = FastAPI()

@app.get("/")
async def root():
    """
    Root endpoint handler function.

    This function handles requests to the root endpoint ("/").
    It returns a JSON response with a simple greeting message.

    Returns:
        dict: A dictionary containing a message key with a greeting message.

    Example:
        >>> response = await root()
        >>> print(response)
        {'message': 'Hello World'}
    """
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Root endpoint handler function.

    This function handles requests to the root endpoint ("/").
    It returns a JSON response with a simple greeting message.

    Returns:
        dict: A dictionary containing a message key with a greeting message.

    Example:
        >>> response = await root()
        >>> print(response)
        {'message': 'Hello World'}
    """
    return {"item_id": item_id}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """
    Root endpoint handler function.

    This function handles requests to the root endpoint ("/").
    It returns a JSON response with a simple greeting message.

    Returns:
        dict: A dictionary containing a message key with a greeting message.

    Example:
        >>> response = await root()
        >>> print(response)
        {'message': 'Hello World'}
    """
    return {"file_path": file_path}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    Root endpoint handler function.

    This function handles requests to the root endpoint ("/").
    It returns a JSON response with a simple greeting message.

    Returns:
        dict: A dictionary containing a message key with a greeting message.

    Example:
        >>> response = await root()
        >>> print(response)
        {'message': 'Hello World'}
    """
    if model_name == ModelName.ALEXNET:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name == ModelName.LENET:
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    """
    Root endpoint handler function.

    This function handles requests to the root endpoint ("/").
    It returns a JSON response with a simple greeting message.

    Returns:
        dict: A dictionary containing a message key with a greeting message.

    Example:
        >>> response = await root()
        >>> print(response)
        {'message': 'Hello World'}
    """
    return fake_items_db[skip: skip + limit]

@app.get("/read_item/{item_id}")
async def read_item_with_query_param(item_id: str, q: Union[str, None] = None):
    """
    Root endpoint handler function.

    This function handles requests to the root endpoint ("/").
    It returns a JSON response with a simple greeting message.

    Returns:
        dict: A dictionary containing a message key with a greeting message.

    Example:
        >>> response = await root()
        >>> print(response)
        {'message': 'Hello World'}
    """
    if q:
        return {"item_id": item_id, "q": q}

    return {"item_id": item_id}

def start():
    """
    Root endpoint handler function.

    This function handles requests to the root endpoint ("/").
    It returns a JSON response with a simple greeting message.

    Returns:
        dict: A dictionary containing a message key with a greeting message.

    Example:
        >>> response = await root()
        >>> print(response)
        {'message': 'Hello World'}
    """
    uvicorn.run("rp_poetry.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()
