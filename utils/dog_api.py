"""
Utility functions to interact with the Dog CEO API to fetch dog images by breed.
"""
from io import BytesIO
from PIL import Image
import requests

BASE_URL = "https://dog.ceo/api/breed"


def get_dog_image_by_breed(breed_name: str):
    """
    Fetch a random dog image URL for the given breed name from the Dog CEO API.
    Then downloads the image and returns it as a PIL Image object.
    :param breed_name:
    :return: image or None
    """

    if breed_name == 'none':
        return None

    breed_parts = breed_name.lower().split()

    if len(breed_parts) == 2:
        api_url = f"{BASE_URL}/{breed_parts[0]}/{breed_parts[1]}/images/random"
    else:
        api_url = f"{BASE_URL}/{breed_parts[0]}/images/random"

    response = requests.get(api_url, timeout=10)
    data = response.json()

    if data["status"] == "success":
        img_path = data["message"]
        response = requests.get(img_path, timeout=10)
        response.raise_for_status()
        if img_path is None:
            image = Image.open("assets/no_image_available.jpg")
        else:
            image = Image.open(BytesIO(response.content))
        return image

    return None
