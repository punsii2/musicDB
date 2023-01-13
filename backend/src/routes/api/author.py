from sqlalchemy.orm import Session
from starlette.responses import Response

import models
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, Request, status

router = APIRouter(prefix="/authors")


@router.get("")
def get_all(request: Request, db: Session = Depends(get_db)):
    return db.query(models.Author).all()


@router.post("")
def post(
    request: Request,
    author: schemas.CreateAuthor,
    db: Session = Depends(get_db),
):
    new_author = models.Author(**author.dict())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    print(new_author)

    return {"data": new_author}


@router.get("/{id}")
def get(id: int, db: Session = Depends(get_db)):
    return db.query(models.Author).filter(models.Author.id == id).first()


# @router.put("/api/author/update/{author_id}")
# def update(request: Request, author_id: schemas.Author, db: Session = Depends(get_db)):
#     author = db.query(models.Author).filter(models.Author.id == author_id).first()
#     author.name = "A"
#     db.commit()
#     return Response()


@router.delete("/{id}")
def delete(request: Request, id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == id).first()
    if author == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with id: {id} does not exist.",
        )
    db.delete(author)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
