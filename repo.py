from sqlalchemy import select

from db import new_session, TaskModel
from schemas import STaskAdd, STask


class TaskRepo:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_data = data.model_dump()
            task = TaskModel(**task_data)

            session.add(task)
            await session.flush()
            await session.commit()

            return task.id

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskModel)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [
                STask.model_validate(task_model, from_attributes=True)
                for task_model in task_models
            ]
            return task_schemas
