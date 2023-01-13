from sqlalchemy.orm import Session

import models
from database import engine, get_db
from fastapi import Depends, FastAPI, Request

from routes.api import router as api_router
from routes.web import router as web_router
from templates import templates

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)
app.include_router(web_router)


@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    persons = db.query(models.Person).all()
    return templates.TemplateResponse(
        "base.html", {"request": request, "person_list": persons}
    )
