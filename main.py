import time

from fastapi import FastAPI, Body
from fastapi.params import Query
from pydantic import BaseModel
import ollama
from fastapi.middleware.cors import CORSMiddleware

# To serve locally for emulated devices run: uvicorn main: app --reload
# To serve within all the network interfaces available run: uvicorn main:app --reload --host 0.0.0.0 --port 8000


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O limita con ["https://tuapp.web.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str


with open('system_prompt.txt', 'r', encoding='utf-8') as file:
    system_prompt = file.read()

print(f"System prompt loaded: {system_prompt[:50]}...")  # Print first 50 characters for verification


@app.post("/generate")
def generate(request: PromptRequest = Query(...)):
    inicio = time.perf_counter()

    """
    Generate a response based on the provided prompt.
    """
    print(f"Received prompt: {request.prompt}")
    print("Generating response...")
    try:

        response = ollama.chat(
            model="llama3:latest",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request.prompt}]
        )
        print("Response generated successfully.")
        return {"response": response["message"]["content"]}

    except Exception as e:
        return {"error": str(e)}

    finally:
        fin = time.perf_counter()
        print(f"Response generated in {fin - inicio:.2f} seconds")
