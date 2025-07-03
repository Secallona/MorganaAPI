from fastapi import FastAPI, Body
from fastapi.params import Query
from pydantic import BaseModel
import ollama

# To serve locally for emulated devices run: uvicorn main: app --reload
# To serve within all the network interfaces available run: uvicorn main:app --reload --host 0.0.0.0 --port 8000



app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str


with open('system_prompt.txt', 'r', encoding='utf-8') as file:
    system_prompt = file.read()

print (f"System prompt loaded: {system_prompt[:50]}...")  # Print first 50 characters for verification
@app.post("/generate")
def generate(request: PromptRequest = Query(...)):

    """
    Generate a response based on the provided prompt.
    """
    print(f"Received prompt: {request.prompt}")
    try:
        response = ollama.chat(
            model="dolphin-mistral",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request.prompt}]
        )
        return {"response": response["message"]["content"]}

    except Exception as e:
        return {"error": str(e)}
