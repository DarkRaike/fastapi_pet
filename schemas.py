from pydantic import BaseModel, ConfigDict
from pydantic.mypy import from_attributes_callback


class STaskAdd(BaseModel):
    name: str
    description: str | None = None

class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    ok: bool = True
    task_id: int