from .yolo_init import MODEL


class YOLOModel:
    def __init__(self):
        self.model = MODEL

    def predict(self, source, imgsz=640, conf=0.1, save=False, show_labels=False):
        results = self.model.predict(source=source, imgsz=imgsz, conf=conf, save=save, show_labels=show_labels)
        return results
