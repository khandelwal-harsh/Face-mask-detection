from flask import Flask,jsonify,request,send_file
from face_mask_detector import Face_Mask_Detection
import cv2
import numpy
import json

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


app = Flask(__name__)
detector_object = Face_Mask_Detection()

@app.route('/send_input', methods=['GET','POST'])
def run_detection():

	file = request.files.get("image","")
	print('[INFO] Running Face Mask Detection.')
	input_image = cv2.imdecode(numpy.fromstring(file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
	# print(input_image)
	output_image = detector_object.run_face_mask_detection(input_image)
	print('[INFO] Detection Successfully Done.')
	# return send_file(output_image,mimetype='image/gif')
	return json.dumps({"output_image":output_image},cls=NumpyEncoder)

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5001)