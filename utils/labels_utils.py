import numpy as np


def get_top3_labels_with_conf(results, labels_map=None):
    """
    Extract the top 3 labels with the highest confidence from model results.
    :param results: list of model prediction results
    :param labels_map:
    :return: list of top 3 dicts for labels,confidence based on confidence
    """
    result0 = results[0]
    if len(result0.boxes) == 0:
        return []

    class_indices = result0.boxes.cls.cpu().numpy().astype(int)
    confidences = result0.boxes.conf.cpu().numpy()

    sorted_idx = np.argsort(confidences)[::-1]
    top3_idx = sorted_idx[:3]

    top3 = []
    for i in top3_idx:
        label = result0.names[class_indices[i]]
        if labels_map:
            label = labels_map.get(label, label)
        top3.append({'label': label, 'confidence': float(confidences[i])})

    return top3
