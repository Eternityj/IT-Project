import cv2
import numpy as np
import pytesseract
from naoqi import ALProxy

NAO_IP = "127.0.0.1"
NAO_PORT = 9559

video_device = ALProxy("ALVideoDevice", NAO_IP, NAO_PORT)

def capture_image():
    try:
        # The nao's camera is called, the top camera is called (0 for the top camera, 1 for the bottom camera),
        # 1 specifies the image resolution, 13 specifies the color space of the image, and 10 specifies the camera frame rate
        video_client = video_device.subscribeCamera("python_client", 0, 1, 13, 10)

        # Get image
        nao_image = video_device.getImageRemote(video_client)
        video_device.unsubscribe(video_client)
        ####### Whether the first few frame rates need to be discarded to obtain the most stable image

        if nao_image is None:
            print("Failed to capture image from NAO camera")
            return ""

        # Convert the image to OpenCV format
        width = nao_image[0]
        height = nao_image[1]
        array = nao_image[6]
        image = np.frombuffer(array, dtype=np.uint8).reshape(height, width, 3)

        # Convert to grayscale image
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # OCR using Tesseract
        text = pytesseract.image_to_string(gray_image)

        return text
    except Exception as e:
        print("An error occurred")
        return ""
