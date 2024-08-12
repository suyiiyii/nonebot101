from pydantic import BaseModel, field_validator


class Config(BaseModel):
    time_user_id: int
