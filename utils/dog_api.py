import requests


def get_dog_image_by_breed(breed_name: str) -> str:
    """
    Fetch a random dog image URL for the given breed name from the Dog CEO API.
    :param breed_name:
    :return: str: URL of the dog image
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
