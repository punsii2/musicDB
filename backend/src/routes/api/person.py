from sqlalchemy.orm import Session
from starlette.responses import Response

import models
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, Request, status

router = APIRouter(prefix="/persons")


@router.get("")
def get_all(request: Request, db: Session = Depends(get_db)):
    return db.query(models.Person).all()


@router.post("")
def post(
    request: Request,
    person: schemas.CreatePerson,
    db: Session = Depends(get_db),
):
    new_person = models.Person(**person.dict())
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    print(new_person)

    return {"data": new_person}


@router.get("/{id}")
def get(id: int, db: Session = Depends(get_db)):
    return db.query(models.Person).filter(models.Person.id == id).first()


# @router.put("/api/person/update/{person_id}")
# def update(request: Request, person_id: schemas.Person, db: Session = Depends(get_db)):
#     person = db.query(models.Person).filter(models.Person.id == person_id).first()
#     person.name = "A"
#     db.commit()
#     return Response()


@router.delete("/{id}")
def delete(request: Request, id: int, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id == id).first()
    if person == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Person with id: {id} does not exist.",
        )
    db.delete(person)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
