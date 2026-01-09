"""
Controller for managing dog breed library functionalities.
"""

from utils import labels_utils
from utils import dog_api


def get_all_breads_with_images():
    """
    Get all dog breeds with their corresponding images.
    :return:
    """
    breeds = labels_utils.get_all_breeds()

    breeds_with_images = []

    for breed_label, breed_name in breeds.items():
        api_label = labels_utils.map_label_to_api(breed_label)

        image = dog_api.get_dog_image_by_breed(api_label)

        breeds_with_images.append({
            'label': breed_name,
            'image': image
        })

    return breeds_with_images
