"""JSON RPC views for the server
"""

import base64

from flask_jsonrpc import JSONRPC
import skimage.io

def init_jsonrpc(app, predictor):
    jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

    @jsonrpc.method('PREDICTOR.predict')
    def predict(img_b64):
        """Get a prediction for the image tiles
        """
        """Test:
        curl -i -X POST    -H "Content-Type: application/json; indent=4"    -d '{
            "jsonrpc": "2.0",
            "method": "PREDICTOR.predict",
            "params": {"img_b64": "`base64  tst1.jpg`"},
            "id": "1"
        }' http://localhost:5000/api
        """
        print("PREDICT:")
        print("IMG: {}".format(img_b64))
        if img_b64.startswith('data:'):  # data:image/png;base64,...
            img_b64 = img_b64[img_b64.find(',')+1 : ]
        imgbytes = base64.b64decode(img_b64)  # Image is bytes b''
        img = skimage.io.imread(imgbytes, plugin='imageio')

        '''
        #TODO
        load img in sklearn
        tile it
        predict
        build response
        '''
        # return {
        #     "img_id": img_id,
        #     "annotations": annotations.get_annotations(img_id)
        # }










    # @jsonrpc.method('IMG.get_new_img')
    # def get_new_img():
    #     """Return a non-tagged image.
    #     """
    #     """Test:
    #     curl -i -X POST    -H "Content-Type: application/json; indent=4"    -d '{
    #         "jsonrpc": "2.0",
    #         "method": "IMG.get_new_img",
    #         "params": {},
    #         "id": "1"
    #     }' http://localhost:5000/api
    #     """
    #     return {
    #         "img_id": annotations.get_not_annotated_image()
    #     }
    #
    #
    # @jsonrpc.method('IMG.get_annotations')
    # def get_annotations(img_id):
    #     """Return the information from an image
    #     """
    #     """Test:
    #     curl -i -X POST    -H "Content-Type: application/json; indent=4"    -d '{
    #         "jsonrpc": "2.0",
    #         "method": "IMG.get_annotations",
    #         "params": {"img_id": "face.jpeg"},
    #         "id": "1"
    #     }' http://localhost:5000/api
    #     """
    #     return {
    #         "img_id": img_id,
    #         "annotations": annotations.get_annotations(img_id)
    #     }
    #
    #
    # @jsonrpc.method('IMG.add_annotations')
    # def add_annotations(img_id, bboxes):
    #     """Set the bboxes for an image.
    #     """
    #     """Test:
    #     curl -i -X POST    -H "Content-Type: application/json; indent=4"    -d '{
    #     "jsonrpc": "2.0",
    #     "method": "IMG.add_annotations",
    #     "params": {
    #       "img_id": "face.jpeg",
    #       "bboxes": [
    #         {"x":0,  "y":0,  "width":10, "height":10},
    #         {"x":90,  "y":10,  "width":21, "height":12}
    #       ]
    #     },
    #     "id": "1"
    #     }' http://localhost:5000/api
    #     """
    #     if not annotations.is_annotated(img_id):
    #         for bbox in bboxes:
    #             annotations.add_annotation(
    #                 img_id,
    #                 bbox['x'],
    #                 bbox['y'],
    #                 bbox['width'],
    #                 bbox['height'],
    #             )
    #         annotations.set_annotated(img_id)
    #     return 'OK'
