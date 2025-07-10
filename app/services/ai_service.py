from openai import OpenAI
from app.core.config import settings
from app.core.system_prompt import get_system_prompt

client = OpenAI(
    base_url=settings.OPENROUTER_API_BASE_URL,
    api_key=settings.OPENAI_API_KEY,
)


def generate_response(prompt: str) -> str:
    """
    Generate a response based on the provided prompt.
    """
    system_prompt = get_system_prompt()
    print(f"Received prompt: {prompt}")

    try:
        response = client.chat.completions.create(
            model=settings.MODELS['WizardLM'],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        print("Response generated successfully.")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error generating response: {e}")
        raise e
