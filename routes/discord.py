from fastapi import APIRouter

router = APIRouter()


@router.get("/discord")
def authorize_discord():
    print("hit")
