from PIL import Image
import numpy as np
import cv2


def convert_photo_to_array(image_path):
    """
    Convert an image file to a NumPy array.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    np.ndarray: The image as a NumPy array.
    """
    image = Image.open(image_path).convert('RGB')
    return np.array(image)


from PIL import Image


def convert_model_output_to_image(model_output):
    """
    Convert a NumPy array (RGB) from model output back to a PIL Image.
    """
    return Image.fromarray(model_output)
