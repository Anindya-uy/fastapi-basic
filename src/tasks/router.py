from fastapi import APIRouter
from src.tasks import controller
from src.tasks.dtos import TaskSchema



task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create")
def create_task(data:TaskSchema):
    return controller.create_task(data)