from picamera2 import Picamera2, Preview
from time import sleep
from datetime import datetime
from gpiozero import Button
from signal import pause
import cv2
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from openvino.runtime import Core

matplotlib.use('GTK3Agg')
ie = Core()
timestamp = datetime.now().isoformat()
picam2 = Picamera2()
button = Button(17)
button2 = Button(27)
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)

def capture():
    picam2.start()
    print("image processing")
    sleep(3)
    picam2.capture_file('/home/<user-name>/Pictures/picture_%s.jpg' % timestamp)
    print("image taken")
    picam2.stop()

def classify():
    model = ie.read_model(model="model/v3-small_224_1.0_float.xml")
    compiled_model = ie.compile_model(model=model, device_name="MYRIAD")
    output_layer = compiled_model.output(0)
    image = cv2.cvtColor(cv2.imread('/home/<user-name>/Pictures/picture_%s.jpg' % timestamp), code=cv2.COLOR_BGR2RGB)
    input_image = cv2.resize(src=image, dsize=(224,224))
    input_image = np.expand_dims(input_image, 0)
    result_infer = compiled_model([input_image])[output_layer]
    result_index = np.argmax(result_infer)
    imagenet_classes = open("model/imagenet_2012.txt").read().splitlines()
    imagenet_classes = ['background'] + imagenet_classes
    print(imagenet_classes[result_index])
    
    
button.when_pressed = capture
button2.when_pressed = classify
pause()