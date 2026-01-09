"""
Controller for handling photo uploads and dog breed detection and whole pipline.
"""
from models.yolo_model import YOLOModel
from utils import photo_utils
from utils import labels_utils
from utils import dog_api


def detect_photo(uploaded_file):
    """
    Perform dog bread detection pipeline.
    First, it converts the uploaded file to an array,
    then it uses the YOLO model to predict the dog breeds in the photo.
    Finally, it retrieves the top 3 detected labels along with corresponding images.
    :param uploaded_file:
    :return: detected labels with images
    """
    photo = photo_utils.convert_photo_to_array(uploaded_file)

    model = YOLOModel()

    result = model.predict(photo)

    if len(result[0].boxes) == 0:
        return []

    detected_labels = labels_utils.get_top3_labels_with_conf(result)

    for label in detected_labels:
        api_label = labels_utils.map_label_to_api(label['label'])
        label['label'] = labels_utils.map_label_to_polish(label['label'])
        image = dog_api.get_dog_image_by_breed(api_label)
        label['image'] = image

    return detected_labels
