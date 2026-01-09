"""
Controller for handling webcam stream capture and dog detection.
"""
# pylint: disable=no-member
import cv2
from models.yolo_model import YOLOModel
from models.dog_detection import DogDetection
from components.dog_card import dog_card
from utils import labels_utils


def capture_webcam_image(result_set, cam_id, stop_signal, frame_placeholder, column):
    """
    Capture stream from webcam and perform dog detection.
    First, it opens the webcam stream using the provided camera ID.
    Then, it continuously reads frames from the webcam until the stop signal is received.
    For each frame, it uses the YOLO model to predict dog breeds.
    Detected dogs are displayed using the dog_card component and
    stored in the result set to avoid duplicates.
    :param result_set: set to store unique dog detections
    :param cam_id: camera ID for the webcam
    :param stop_signal:
    :param frame_placeholder: placeholder to display the webcam frames
    :param column: column to display dog cards
    :return:
    """
    cap = cv2.VideoCapture(cam_id)

    last_frame_rgb = None

    while cap.isOpened() and not stop_signal:

        ret, frame = cap.read()
        if not ret:
            break

        results = YOLOModel().predict(frame, conf=0.6)
        if not results:
            continue

        result = results[0]

        plotted_frame = result.plot(labels=False)
        if isinstance(plotted_frame, cv2.UMat):
            plotted_frame = plotted_frame.get()
        last_frame_rgb = cv2.cvtColor(plotted_frame, cv2.COLOR_BGR2RGB)

        frame_placeholder.image(last_frame_rgb)

        label_with_conf = labels_utils.get_label_and_conf(result)

        if label_with_conf is not None:
            detection = DogDetection(label=label_with_conf['label'],
                                     confidence=label_with_conf['confidence'],
                                     image=last_frame_rgb)
            with column:
                if detection not in result_set:
                    dog_card(detection.label, detection.image, detection.confidence)

            result_set.add(detection)

    if last_frame_rgb is not None:
        frame_placeholder.image(last_frame_rgb)

    cap.release()
    cv2.destroyAllWindows()
    return result_set
