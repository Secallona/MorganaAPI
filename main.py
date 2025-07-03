from fastapi import FastAPI, Body
from fastapi.params import Query
from pydantic import BaseModel
import ollama

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate(request: PromptRequest = Query(...)):

    """
    Generate a response based on the provided prompt.
    """
    print(f"Received prompt: {request.prompt}")
    try:
        response = ollama.chat(
            model="dolphin-mistral",
            messages=[{"role": "user", "content": request.prompt}]
        )
        return {"response": response["message"]["content"]}

    except Exception as e:
        return {"error": str(e)}
