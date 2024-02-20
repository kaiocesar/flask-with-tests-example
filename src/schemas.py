from pydantic import BaseModel


class InputDataSchema(BaseModel):
    train: bytes
    test: bytes
    model: bytes
    columns: str
