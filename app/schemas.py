from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(..., min_length=2, max_length=1000)


class AskResponse(BaseModel):
    question: str
    answer: str
    context: list[str]
    is_valid: bool
    errors: list[str]
