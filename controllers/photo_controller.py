from models.yolo_model import YOLOModel
import utils.photo_utils as image_utils
import utils.labels_utils as labels_utils
import utils.dog_api as dog_api


def detect_photo(uploaded_file):
    photo = image_utils.convert_photo_to_array(uploaded_file)

    model = YOLOModel()

    result = model.predict(photo)

    detected_labels = labels_utils.get_top3_labels_with_conf(result)

    for label in detected_labels:
        label['label'] = label['label'].replace('_', ' ')
        image = dog_api.get_dog_image_by_breed(label['label'])
        label['image'] = image

    return detected_labels
