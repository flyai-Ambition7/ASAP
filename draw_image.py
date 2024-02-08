from dotenv import load_dotenv
from io import BytesIO
import requests
import os
from openai import OpenAI

load_dotenv(verbose=True)
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
def draw_image_by_DALLE(prompt):
    client=OpenAI(api_key=OPENAI_API_KEY)
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="hd",
        n=1,
    )
    image_url=response.data[0].url
    return BytesIO(requests.get(image_url).content)