from src.tasks.dtos import TaskSchema

def create_task(data:TaskSchema):
    print(data.model_dump())
    return {"status: Task created successfully.."}
