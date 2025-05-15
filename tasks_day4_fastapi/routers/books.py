from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_session
from models import BookDB
from schemas import BookCreate, BookResponse
from sqlalchemy import select

router = APIRouter()

@router.post("/", response_model=BookResponse)
async def create_book(book: BookCreate, db: Session = Depends(get_session)):
    db_book = BookDB(**book.dict())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book

@router.get("/")
async def get_books(db: Session = Depends(get_session)):
    result = await db.execute(select(BookDB))
    return result.scalars().all()