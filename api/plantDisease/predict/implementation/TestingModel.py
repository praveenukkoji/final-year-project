import numpy as np
import pickle
import cv2
from tensorflow.keras.utils import img_to_array

# Load model
filename = 'predict/implementation/plant_disease_classification_model.pkl'
model = pickle.load(open(filename, 'rb'))

# Load labels
filename = 'predict/implementation/plant_disease_label_transform.pkl'
image_labels = pickle.load(open(filename, 'rb'))

# Dimension of resized image
DEFAULT_IMAGE_SIZE = tuple((256, 256))


def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None:
            image = cv2.resize(image, DEFAULT_IMAGE_SIZE)
            return img_to_array(image)
        else:
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None


def predict_disease(image_path):
    image_array = convert_image_to_array(image_path)
    np_image = np.array(image_array, dtype=np.float16) / 225.0
    np_image = np.expand_dims(np_image, 0)

    predict_x = model.predict(np_image)
    classes_x = np.argmax(predict_x, axis=1)

    return image_labels.classes_[classes_x][0]
