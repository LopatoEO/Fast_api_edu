from fastapi import FastAPI
from routers.books import router as books_router
import uvicorn

app = FastAPI()
app.include_router(books_router, prefix="/books", tags=["books"])


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Books API"}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
