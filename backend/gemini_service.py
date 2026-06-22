import json
from google import genai
from dotenv import load_dotenv
from PIL import Image
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def identify_snake_image(image_path):

    image = Image.open(image_path)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            image,
            """
            Identify this snake.

            Return ONLY valid JSON.

            Example:

            {
                "common_name": "",
                "scientific_name": "",
                "venomous_status": "",
                "confidence": ""
            }

            Do not add explanations.
            Do not use markdown.
            Return only JSON.
            """
        ]
    )

    try:
        return json.loads(response.text)

    except Exception:
        return {
            "error": response.text
        }