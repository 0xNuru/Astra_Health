from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/patient",
    tags=["patient management"]
)

@router.get("/")
def root():
    return {"message": "Hello World"}

