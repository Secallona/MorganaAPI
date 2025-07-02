from fastapi import FastAPI
import ollama


app = FastAPI()

@app.post("/generate")
def generate(prompt: str):
    """
    Generate a response based on the provided prompt.
    """
    try:
        response = ollama.chat(model="deepseek-r1", messages=[{"role": "user", "content": prompt}])
        return {"response": response["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}