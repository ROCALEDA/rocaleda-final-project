from fastapi import APIRouter, Request

from app.post.services.post_service import PostsService

router = APIRouter(
    prefix="/post", tags=["post"], responses={404: {"description": "Not found"}}
)


def initialize(post_service: PostsService):
    @router.post("/")
    async def create_post(request: Request):
        return await post_service.create_post(request)

    @router.get("")
    async def get_post(request: Request):
        return await post_service.get_post(request)
