# Team 97

This is a service project designed to assist visually impaired individuals by enabling a NAO robot to read books aloud. The project uses a camera to capture text, converts the text to speech, and integrates with an intelligent AI API to enable interactive Q&A.

## Features and Functionality
### Laptop Folder

This folder contains code and resources for leveraging the laptop's built-in camera to perform various tasks, including:

- **OCR (Optical Character Recognition):** Capture images and extract text using OCR technology.
- **Reading Aloud:** Read the extracted text aloud, simulating a natural reading experience.
- **Music Playback:** Integrate with a music player to play background music while reading or during other activities.
- **Emotion-based Reading:** Enhance the reading experience by modulating the voice based on the emotional content of the text.

### Music Folder

This folder contains a curated list of music tracks that can be played during various activities to enhance the user experience.

### NLTK Data Folder

This folder includes the NLTK data used as a training dataset for natural language processing tasks. It supports sentiment analysis and text classification, which are used to enhance the emotion-based reading functionality in the project.

### Robot Folder

This folder contains code and resources for utilizing the NAO robot's camera to perform similar tasks as the laptop, such as capturing images for OCR. It also includes functionalities that leverage the robot's capabilities for reading aloud and interacting with users, making the interaction more engaging.



### Prerequisites

Ensure that you have the following installed on your system:

- Python 2.7
- Tesseract OCR
- OpenCV
- NAOqi SDK

### macOS

1. **Install Homebrew (if you don't have it):**  
   Open a terminal and run:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. **Install Python2.7**: brew install python@2
3. **Install Tesseract OCR**: brew install tesseract
4.**Install OpenCV**:brew install opencv@2
5. **Install NAOqi SDK**


### Windows

1. **Install Python 2.7:**  
   Download and install Python 2.7 from the [official Python website](https://www.python.org/downloads/release/python-2718/).

2. **Install Tesseract OCR:**  
   Download and install Tesseract OCR from the [official GitHub repository](https://github.com/tesseract-ocr/tesseract/wiki).

3. **Install OpenCV:**  
   You can download and install OpenCV for Python 2.7 from [this link](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_install/py_install_windows/py_install_windows.html).

4. **Install NAOqi SDK:**  
   Download the NAOqi SDK for Windows from the [SoftBank Robotics Developer Center](https://developer.softbankrobotics.com/) and follow the installation instructions provided.

   




