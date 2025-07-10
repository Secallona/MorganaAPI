import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
    OPENROUTER_API_BASE_URL = 'https://openrouter.ai/api/v1'
    ALLOWED_ORIGINS = ["*"]
    MODELS = {
        'DeepSeekV3': 'deepseek/deepseek-chat-v3-0324:free',
        'Llama3.3': 'meta-llama/llama-3.3-70b-instruct:free',
        'WizardLM': 'microsoft/wizardlm-2-8x22b',
        'Dolphin/Mistral': 'cognitivecomputations/dolphin3.0-r1-mistral-24b:free'
    }


settings = Settings()
