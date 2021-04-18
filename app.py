from fastapi import FastAPI
import controller as controller

tags_metadata = [
    {
        'name': 'items',
        'description': 'items',
    }
]

app = FastAPI(
    title='Mini api',
    description='This is my mini api (description)',
    version='1.0.0',
    openapi_tags=tags_metadata
)

@app.get("/")
async def root():
    return controller.get_items()

@app.get("/{item_id}")
async def read_item(item_id: int):
    return controller.get_item(item_id)

