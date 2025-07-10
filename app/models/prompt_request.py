from pydantic import BaseModel

""" Model for prompt requests."""


class PromptRequest(BaseModel):
    prompt: str
