from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

import models
from database import get_db
from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from templates import templates

router = APIRouter(prefix="/authors")


@router.get("")
def get_all(request: Request, db: Session = Depends(get_db)):
    authors = db.query(models.Author).all()
    return templates.TemplateResponse(
        "base.html", {"request": request, "author_list": authors}
    )


@router.post("")
def web_create(
    request: Request,
    work_id: int = Form(...),
    person_id: int = Form(...),
    role_id: int = Form(...),
    db: Session = Depends(get_db),
):
    new_author = models.Author(
        work_id=work_id,
        person_id=person_id,
        role_id=role_id,
    )
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    print(new_author)

    url = request.url_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@router.get("/delete/{id}")
def web_delete(request: Request, id: int, db: Session = Depends(get_db)):
    id = int(id)
    author = db.query(models.Author).filter(models.Author.id == id).first()
    if author == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with id: {id} does not exist.",
        )
    db.delete(author)
    db.commit()
    url = request.url_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
