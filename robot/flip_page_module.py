import cv2
import numpy as np
import time
from naoqi import ALProxy

NAO_IP = "192.168.1.108"
NAO_PORT = 9559

video_device = ALProxy("ALVideoDevice", NAO_IP, NAO_PORT)
motion_proxy = ALProxy("ALMotion", NAO_IP, NAO_PORT)

def page_capture_image():
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

        # Convert the image to grayscale for edge detection
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply Gaussian blur to smooth the image
        blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)
        # Perform Canny edge detection
        edges = cv2.Canny(blurred, 50, 150)
        # Find contours in the edge-detected image
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            max_contour = max(contours, key=cv2.contourArea)

            # Get the bounding rectangle of the largest contour
            x, y, w, h = cv2.boundingRect(max_contour)

        return (x + w // 2, y + h // 2)

    except Exception as e:
        print("An error occurred")
        return ""

def flip_page():
    # Capture the position of the page from the image
    position = page_capture_image()
    # Specify the effector (RArm for right arm)
    effector = "RArm"

    # Calculate the offset in x and y direction based on the image
    x_offset = position[0] * 0.001  # Convert pixels to meters (adjust this scale as needed)
    y_offset = position[1] * 0.001

    # Set the initial position for the arm to approach the page
    init_position = [0.2, -0.1 + y_offset, 0.1 + x_offset]
    # Move the arm to the initial position with 20% of max speed
    motion_proxy.setPositions(effector, 0, init_position, 0.2, 7)

    # Open the hand to prepare to grab the page
    motion_proxy.openHand("RHand")
    time.sleep(0.5)  # Wait for 0.5 seconds to ensure the hand is fully open
    # Close the hand to grab the page
    motion_proxy.closeHand("RHand")

    # Set the position for the arm to flip the page
    flip_position = [0.2, 0.1 + y_offset, 0.1 + x_offset]
    # Move the arm to the flip position with 20% speed
    motion_proxy.setPositions(effector, 0, flip_position, 0.2, 7)
    time.sleep(1.0)  # Wait for 1 second to complete the flipping motion
    # Open the hand to release the page after flipping
    motion_proxy.openHand("RHand")
    time.sleep(0.5)  # Wait for 0.5 seconds

    # Move the arm back to the initial position
    motion_proxy.setPositions(effector, 0, init_position, 0.2, 7)

    # Put the robot into resting mode after the action
    motion_proxy.rest()