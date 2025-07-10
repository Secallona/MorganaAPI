import time
from fastapi import APIRouter, Query
from app.models.prompt_request import PromptRequest
from app.services.ai_service import generate_response

router = APIRouter()


@router.post("/generate")
def generate(request: PromptRequest = Query(...)):
    inicio = time.perf_counter()
    try:
        response = generate_response(request.prompt)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
    finally:
        fin = time.perf_counter()
        print(f"Request processed in {fin - inicio:.2f} seconds.")
