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

            Return:
            Common Name
            Scientific Name
            Venomous or Non-venomous
            Confidence Percentage
            """
        ]
    )

    return response.text