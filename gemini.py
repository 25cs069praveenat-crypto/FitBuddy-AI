from google import genai
from google.genai import errors
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_fitness_plan(prompt: str):

    models = [
        "gemini-3.8-flash",
        "gemini-3.5-flash-lite"
    ]

    for model in models:
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            return response.text

        except errors.ServerError:
            continue

        except errors.ClientError as e:
            if "429" in str(e):
                continue
            return "Gemini API error. Please check your API key and settings."

    return "Gemini quota is currently unavailable. Please try again later."