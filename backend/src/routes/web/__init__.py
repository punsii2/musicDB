from fastapi import APIRouter
from .person import router as person_router
from .author import router as author_router

router = APIRouter(prefix="/web")
router.include_router(person_router)
router.include_router(author_router)
