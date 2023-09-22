from fastapi import Request

from app.post.repositories.post_repository import PostRepository


class PostsService:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    async def create_post(self, request: Request):
        return await self.post_repository.create_post(request)

    async def get_post(self, request: Request):
        return await self.post_repository.get_post(request)
