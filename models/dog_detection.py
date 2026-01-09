"""
A class to represent a dog detection with label, confidence score, and image data.
It includes methods for hashing, equality comparison, and string representation.
It functions as a data wrapper to store information about detected dogs.
"""


class DogDetection:
    """
    A class to represent a dog detection with label, confidence score, and image data.
    """

    def __init__(self, label, confidence, image):
        self.label = label
        self.confidence = confidence
        self.image = image

    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        return self.label == other.label

    def __str__(self):
        return f"DogDetection(label={self.label}, confidence={self.confidence})"
