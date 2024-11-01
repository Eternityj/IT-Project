# Team 97 - ReadMate

**Project Description**  
ReadMate assists visually impaired individuals by enabling a NAO robot to read books aloud. The system captures text using a camera, converts the text to speech, and integrates an intelligent Q&A system using GPT-4 *(updated from GPT-3.5)*.

---

## Table of Contents
- [System Configuration and Installation](#system-configuration-and-installation)
- [Features](#features)
  - [Captures images and performs OCR](#captures-images-and-performs-ocr)
  - [Voice Command Interaction](#voice-command-interaction)
  - [Language Switching](#language-switching)
  - [Volume and Speed Management](#volume-and-speed-management)
  - [Sentiment Analysis and Emotion-Based Modulation](#sentiment-analysis-and-emotion-based-modulation)
  - [Intelligent Q&A System](#intelligent-q-a-system)
  - [Music Playback Control](#music-playback-control)
  - [Text Reading with Emotion Tracking](#text-reading-with-emotion-tracking)
- [Required Libraries](#required-libraries)
- [Additional Setup](#additional-setup)
- [Included Files](#included-files)
  - [Laptop Folder](#laptop-folder)
  - [Robot Folder](#robot-folder)
- [Key Algorithms](#key-algorithms)
  - [Image Capture and Text Recognition](#image-capture-and-text-recognition)
  - [Interactive Module for Voice-Activated Commands](#interactive-module-for-voice-activated-commands)
  - [Reading Functionality with Emotional Tone Modulation](#reading-functionality-with-emotional-tone-modulation)
  - [Sentiment Analysis for Emotion-Based Modulation](#sentiment-analysis-for-emotion-based-modulation)
- [Changelog](#changelog)
- [Detected Bugs](#detected-bugs)
- [Test Cases](#test-cases)
- [Traceability Matrix](#traceability-matrix)
---

### System Configuration and Installation

Follow the instructions in **System Configuration and Installation** to set up the environment and install necessary dependencies on either macOS or Windows.

---

### Features

- **Captures images and performs OCR**  
  - Uses both NAO robot and laptop’s camera for image capture and OCR processing (`camera_module.py`).
  
- **Voice Command Interaction**  
  - Facilitates interaction with the NAO robot using voice commands (`interactive_module.pyd`, `interactive_module1.py`).

- **Language Switching**  
  - Switches languages for both speech recognition and text-to-speech (`language_module.py`).

- **Volume and Speed Management**  
  - Manages the NAO robot’s volume and reading speed for a customized listening experience (`voice_module.py`).

- **Sentiment Analysis and Emotion-Based Modulation**  
  - Performs sentiment analysis on text and adjusts speech rate and volume based on the detected emotion (`emotion_module.py`).

- **Intelligent Q&A System**  
  - Answers questions about the text using the GPT API for an interactive Q&A experience (`gpt.py`).

- **Music Playback Control**  
  - Plays and stops music on the NAO robot, adding an additional layer of engagement (`music.py`).

- **Text Reading with Emotion Tracking**  
  - Reads text aloud with tracking and emotional modulation for a dynamic and engaging experience (`read_module.py`).

### Required Libraries

To run the project, install the following Python libraries:

- **OpenCV**: For image processing.
  ```bash
  pip install opencv-python
- **NumPy**: For numerical operations and handling arrays.
  ```bash
  pip install numpy
- **TextBlob**:  For natural language processing and sentiment analysis.
  ```bash
  pip install textblob
- **NLTK**: For tokenizing text and other language processing tasks.
  ```bash
  pip install nltk

### Additional Setup

#### Tesseract OCR Engine

To use Tesseract OCR, install the Tesseract executable separately based on your operating system:

- **Windows**: Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
- **macOS**: Install with Homebrew:
  ```bash
  brew install tesseract
- **Linux**: Install via the package manager:
  ```bash
  sudo apt install tesseract-ocr


### Included Files

#### Laptop Folder
- **camera_module.py**: Captures images using the system’s camera and processes them for OCR.
- **emotion_module.py**: Analyzes text sentiment and adjusts reading rate and volume accordingly.
- **gpt.py**: Sends text and questions to GPT-4 API for generating responses (updated from GPT-3.5).
- **music_module.py**: Manages music playback and stopping functions on the laptop.
- **read_module.py**: Handles text-to-speech reading with emotional modulation.
- **voice_module.py**: Adjusts volume and reading speed for text-to-speech functionality.

#### Robot Folder
- **camera_module.py**: Captures images from the NAO robot’s camera and performs OCR.
- **interactive_module.pyd**: Facilitates interaction with the NAO robot using voice commands.
- **language_module.py**: Switches language for both speech recognition and text-to-speech.
- **read_module.py**: Reads text aloud with sentence segmentation and emotional modulation.
- **voice_module.py**: Adjusts the NAO robot's volume and speech rate settings.
- **emotion_module.py**: Analyzes text sentiment and adjusts rate and volume for reading.
- **gpt.py**: Processes text and user questions with GPT-4 API for interactive Q&A (updated from GPT-3.5).
- **music.py**: Handles music playback on the NAO robot.
- **flip_page_module.py**: Captures images and flips pages using the NAO robot’s arm.

---

### Key Algorithms

#### Image Capture and Text Recognition
Utilizes the NAOqi SDK to access the NAO robot’s top camera, capturing images for processing. The captured image is converted into a NumPy array for compatibility with OpenCV, transformed to grayscale to enhance OCR accuracy, and processed with Tesseract to extract readable text. This process includes error handling for potential capture failures. Integrating the NAOqi SDK for camera access, OpenCV for image processing, and Tesseract for text extraction allows effective conversion of visual data into a usable text format.

#### Interactive Module for Voice-Activated Commands
Manages voice-activated interactions with the NAO robot through the NAOqi SDK, handling text-to-speech, speech recognition, and memory functionalities. The module initializes with a set vocabulary of commands and listens for recognized speech. When a command is detected with sufficient confidence, the robot executes actions such as capturing and reading text, controlling music playback, adjusting volume, and switching languages. The integration with camera, voice, music, reading, and GPT modules provides a versatile interactive experience. Error handling manages subscription failures and unrecognized commands.

#### Reading Functionality with Emotional Tone Modulation
Leverages the NAOqi SDK to implement voice synthesis on the NAO robot. The `read_text` function takes a string input, tokenizes it into sentences with NLTK, and iteratively reads each sentence aloud, monitoring for pause commands. Text-to-speech parameters adjust based on the emotional tone of each sentence using the `emotion_read` function. The reading can be paused or resumed with `pause_reading` and `continue_reading` functions, respectively. The module integrates components for voice control, language processing, and emotion detection, creating an interactive reading experience.

#### Sentiment Analysis for Emotion-Based Modulation
Uses the TextBlob library to evaluate the emotional tone of a text. The `analyze_sentiment` function calculates the polarity and subjectivity scores for input text, which the `emotion_read` function uses to adjust text-to-speech parameters on the NAO robot. Based on the polarity score, it assigns appropriate speech rate and volume levels, enhancing expressiveness in reading. This integration allows the robot to convey emotions more effectively, resulting in a more engaging user experience.

---

### Changelog

#### Version 1.1.0
- **Updated** GPT integration to use GPT-4 for improved Q&A interaction (previously GPT-3.5).
- **Removed** duplicate `read_module.py` in the robot folder.
- **Revised** `interactive_module.pyd` to include only one interactive module.
- **Updated** `nltk` functionality to limit its scope to sentence segmentation.

---

### Detected Bugs

1. **Emotion Modulation Lag**: Some delays occur when adjusting reading speed based on emotional content.
2. **OCR Accuracy**: Occasional inaccuracies in text capture due to image quality variations.
3. **Voice Command Recognition**: In high-noise environments, the NAO robot sometimes fails to recognize voice commands.
4. **Page Flip Mechanism**: The NAO robot occasionally struggles to flip thin book pages.

### Test Cases

| **Test Case**           | **Description**                                   | **Expected Result**                                          | **Status**   |
|-------------------------|---------------------------------------------------|--------------------------------------------------------------|--------------|
| OCR Capture             | Capture text via NAO camera for OCR processing    | Accurate text extraction                                     | Pass         |
| Sentiment Modulation    | Adjust reading rate based on sentiment            | Higher rate for positive text, lower for negative text       | Pass         |
| Voice Commands          | Respond to "start read" and "pause reading"       | Robot starts/pauses reading accordingly                      | Pass         |
| GPT Q&A Interaction     | User asks questions about text                    | Relevant responses based on text content                     | Pass         |
| Language Switching      | Switch language for TTS and recognition           | Robot speaks/recognizes in the selected language             | Pass         |
| Music Playback          | Play and stop music on command                    | Robot plays and stops music as requested                     | Pass         |
| Page Flip               | Use NAO arm to flip a book page                   | Page flips successfully                                      | Conditional  |

---

### Traceability Matrix

| **Requirement**                    | **Module**                | **Test Case**           | **Status**   |
|------------------------------------|---------------------------|--------------------------|--------------|
| OCR Image Capture                  | `camera_module.py`        | OCR Capture              | Pass         |
| Emotion-Based Speech Adjustment    | `emotion_module.py`       | Sentiment Modulation     | Pass         |
| Voice Command Interaction          | `interactive_module.pyd`  | Voice Commands           | Pass         |
| GPT-4 Q&A                          | `gpt.py`                  | GPT Q&A Interaction      | Pass         |
| Language Switching                 | `language_module.py`      | Language Switching       | Pass         |
| Music Playback Control             | `music_module.py`         | Music Playback           | Pass         |
| Page Flipping                      | `flip_page_module.py`     | Page Flip                | Conditional  |
