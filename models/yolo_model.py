"""
YOLO Model Wrapper
"""

from .yolo_init import MODEL


class YOLOModel:
    """
    YOLO Model wrapper class for predictions.
    """

    def __init__(self):
        """
        Initialize the YOLO model.
        """
        self.model = MODEL

    def predict(self, source, imgsz=640, conf=0.4, save=False, show_labels=True):
        """
        Perform prediction using the YOLO model.
        :param source: Input source for prediction.
        :param imgsz: Image size for prediction.
        :param conf: Confidence threshold.
        :param save: Boolean to save the results.
        :param show_labels: Boolean to show labels on the results.
        :return:
        """
        results = self.model.predict(
            source=source,
            imgsz=imgsz,
            conf=conf,
            save=save,
            show_labels=show_labels
        )
        return results
