from fastapi import FastAPI, Body
from fastapi.params import Query
from pydantic import BaseModel
import ollama

app = FastAPI()


@app.post("/generate")
def generate(request: str):

    """
    Generate a response based on the provided prompt.
    """
    print(f"Received prompt: {request}")
    try:
        response = ollama.chat(
            model="deepseek-r1",
            messages=[{"role": "user", "content": request}]
        )
        return {"response": response["message"]["content"]}

    except Exception as e:
        return {"error": str(e)}
