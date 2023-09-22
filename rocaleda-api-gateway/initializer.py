from fastapi import FastAPI

from app.post.controllers import post_controller
from app.health.controllers import health_controller
from app.post.services.post_service import PostsService
from app.candidate.controllers import candidate_controller
from app.health.services.health_service import HealthService
from app.post.repositories.post_repository import PostRepository
from app.candidate.services.candidate_service import CandidateService
from app.candidate.repositories.candidate_repository import CandidateRepository


class Initializer:
    def __init__(self, app: FastAPI):
        self.app = app

    def setup(self):
        self.init_health_module()
        self.init_candidate_module()
        self.init_post_module()

    def init_health_module(self):
        health_service = HealthService()
        health_controller.initialize(health_service)
        self.app.include_router(health_controller.router)

    def init_candidate_module(self):
        candidate_repository = CandidateRepository()
        candidate_service = CandidateService(candidate_repository)
        candidate_controller.initialize(candidate_service)
        self.app.include_router(candidate_controller.router)

    def init_post_module(self):
        post_repository = PostRepository()
        post_service = PostsService(post_repository)
        post_controller.initialize(post_service)
        self.app.include_router(post_controller.router)
