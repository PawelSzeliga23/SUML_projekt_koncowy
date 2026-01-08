from PIL import Image
import numpy as np
import cv2


def convert_photo_to_array(image_path):
    """
    Convert an image file to a NumPy array (RGB).
    :param image_path: Path to the image file
    :return: NumPy array representation of the image in RGB format
    """
    image = Image.open(image_path).convert('RGB')
    return np.array(image)


def convert_model_output_to_image(model_output):
    """
    Convert model output (NumPy array) back to a PIL Image.
    :param model_output:
    :return:
    """
    return Image.fromarray(model_output)
