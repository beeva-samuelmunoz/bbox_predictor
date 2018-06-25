
from tensorflow import keras

# Todo import tiler



class Simple():

    def __init__(self, path_model):
        self.model = keras.models.load_model(filepath=path_model)


    def predict(img_sklearn, bboxes=[]):
        pass
