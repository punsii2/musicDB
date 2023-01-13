from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

import models
from models.person import Gender
from database import get_db
from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from templates import templates

router = APIRouter(prefix="/persons")


@router.get("")
def get_all(request: Request, db: Session = Depends(get_db)):
    persons = db.query(models.Person).all()
    return templates.TemplateResponse(
        "base.html", {"request": request, "person_list": persons}
    )


@router.post("")
def web_create(
    request: Request,
    name_first: str = Form(...),
    name_last: str = Form(...),
    gender: Gender = Form(...),
    born_in: str = Form(...),
    memo: str = Form(...),
    db: Session = Depends(get_db),
):
    new_person = models.Person(
        name_first=name_first,
        name_last=name_last,
        gender=gender,
        born_in=born_in,
        memo=memo,
    )
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    print(new_person)

    url = request.url_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@router.get("/delete/{id}")
def web_delete(request: Request, id: int, db: Session = Depends(get_db)):
    id = int(id)
    person = db.query(models.Person).filter(models.Person.id == id).first()
    if person == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Person with id: {id} does not exist.",
        )
    db.delete(person)
    db.commit()
    url = request.url_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
