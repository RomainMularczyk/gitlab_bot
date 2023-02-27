from fastapi import APIRouter


router = APIRouter()


@router.post("/new_merge_request", status_code=200)
async def new_merge_request(merge_request):
    print("okay")
    print(merge_request)
