# Team 97-ReadMate

This is a service project designed to assist visually impaired individuals by enabling a NAO robot to read books aloud. The project uses a camera to capture text, converts the text to speech, and integrates with an intelligent AI API to enable interactive Q&A.

## Features and Functionality
### Laptop Folder

This folder contains code and resources for leveraging the laptop's built-in camera to perform various tasks, including:
- **camera_module.py:** Captures an image using the system’s camera and processes it for OCR (Optical Character Recognition) using Tesseract. It converts the captured image to grayscale for better recognition accuracy and returns the extracted text. The module includes a delay to allow the camera to stabilize before capturing an image.
- **emotion_module.py:** Analyzes the sentiment of text using `TextBlob` and adjusts speech rate and volume based on the sentiment's polarity. Positive text increases the rate and volume, while negative text decreases them, enhancing the emotional expression during reading.
- **gpt.py:** Sends a book excerpt and user question to the OpenAI GPT-3.5 API for processing. It retrieves a response, answering questions about the text based on the current content, and handles any errors that occur during the request.
- **music_module.py:** Plays music from a specified folder on the local system, selecting a random music file (.mp3 or .wav). It uses a subprocess to play the music and includes functionality to stop any currently playing music. The module also supports playing music at regular intervals (e.g., every hour).
- **read_module.py:** Handles text-to-speech reading with emotion-based adjustments for rate and volume. It splits text into sentences, adjusts the reading speed and volume based on emotional content, and reads aloud using the system's speech synthesis. The module supports starting, pausing, continuing, and stopping the reading process, with threading used for concurrent execution.
- **voice_module.py:** Manages volume and reading speed for text-to-speech. It allows adjusting the volume and reading rate, ensuring both stay within defined limits. The current volume is adjusted using system commands, while reading speed is updated based on user input.


### Music Folder

This folder contains a curated list of music tracks that can be played during various activities to enhance the user experience.

### NLTK Data Folder

This folder includes the NLTK data used as a training dataset for natural language processing tasks. It supports sentiment analysis and text classification, which are used to enhance the emotion-based reading functionality in the project.

### Robot Folder
- **Camera_module.py:** Capture images from NAO robot's camera and perform OCR using OpenCV and Tesseract.
- **Interactive_module.pyd:** Enables interaction with the NAO robot using voice commands to trigger various actions such as reading text, playing music, and adjusting volume. It integrates functionalities from the camera, reading, and music modules, and utilizes speech recognition to respond to user commands like "start read," "pause reading," and language switching.
- **Language_module.py:** Handles changing the language of the NAO robot's speech recognition and text-to-speech system based on user input. It checks for supported languages and switches both the speech recognition and TTS systems to the requested language, providing feedback to the user.
- **Read_module.py:** Handles reading text aloud using the NAO robot. It integrates emotion-based adjustments to speech rate and volume, breaking the text into sentences using `nltk`. Users can pause and continue reading, and the system resumes from where it left off.
- **Voice_module.py:** Manages the NAO robot's voice settings, allowing adjustments to volume and speech rate. It includes functions to change and retrieve the current volume and rate, ensuring the robot's voice can be dynamically modified based on user input or emotional reading.
- **emotion_module.py:** Performs sentiment analysis on text using `TextBlob` and adjusts the speech rate and volume based on the text's emotional content. Positive text increases the rate and volume, while negative text slows the rate and softens the volume, enhancing the emotional reading experience.
- **gpt.py:** Sends a book excerpt and user question to the OpenAI GPT-3.5 API, using the API to generate answers based on the current page of the book. It processes the response and returns the generated answer, or an error message if the request fails.
- **interactive_module.py:** Facilitates voice-based interactions with the NAO robot using speech recognition. It handles various commands such as starting and pausing reading, playing and stopping music, adjusting volume, changing languages, and asking questions about the text through GPT. It processes voice commands with dynamic responses based on user input, utilizing different modules for reading, music, and text recognition.
- **interactive_module1.py:** Similar to `interactive_module.py`, this file enables voice interactions with the NAO robot using speech recognition. It handles commands like reading, playing/stopping music, adjusting volume, changing language, and asking questions about text using GPT. It processes user commands and responds accordingly, using text recognition and other modules for dynamic interaction.
- **music.py:** Handles playing and stopping music on the NAO robot. It randomly selects music files from a specified folder and plays them using the NAO robot’s ALAudioPlayer. The module also includes functionality to stop currently playing music and an optional feature to play music every hour.
- **read_module.py:** Responsible for reading text aloud using the NAO robot. The text is broken into sentences using `nltk`, and each sentence is read with dynamic volume and speech rate adjustments based on its emotional content. The module allows for pausing and resuming reading, while keeping track of the current position in the text.






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

   




