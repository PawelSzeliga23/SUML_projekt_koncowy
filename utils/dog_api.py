import requests


def get_dog_image_by_breed(breed_name: str) -> str:
    """
    Fetch a dog image URL from the Dog CEO API based on the breed name.

    Parameters:
    breed_name (str): The name of the dog breed.

    Returns:
    str: URL of the dog image.
    """

    base_url = "https://dog.ceo/api/breed"
    breed_parts = breed_name.lower().split()
    if breed_parts[1] == 'dog':
        breed_parts.pop(1)

    if len(breed_parts) == 2:
        api_url = f"{base_url}/{breed_parts[1]}/{breed_parts[0]}/images/random"
    else:
        api_url = f"{base_url}/{breed_parts[0]}/images/random"

    response = requests.get(api_url)
    data = response.json()

    if data["status"] == "success":
        return data["message"]
    else:
        return None
