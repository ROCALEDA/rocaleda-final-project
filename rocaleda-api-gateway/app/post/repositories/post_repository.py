import os

from fastapi import Request

import httpx


class PostRepository:
    def __init__(self):
        self.post_host = os.getenv("POST_MS")

    async def create_post(self, request: Request):
        async with httpx.AsyncClient() as client:
            try:
                body = request.json()

                response = await client.post(
                    f"https://{self.post_host}/posts",
                    json=body,
                    headers=request.headers,
                )

                return response.json()
            except Exception as exc:
                print(f"Exception type: {type(exc)}")
                print(f"Exception arguments: {exc.args}")
                print("Exception traceback:", exc.__traceback__)

    async def get_post(self, request: Request):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"https://{self.post_host}/posts",
                    params=request.query_params,
                    headers=request.headers,
                )
                return response.json()
            except Exception as exc:
                print(f"Exception type: {type(exc)}")
                print(f"Exception arguments: {exc.args}")
                print("Exception traceback:", exc.__traceback__)
