# Interactive AI Storyteller 🗣️📖✨

An interactive application that combines speech recognition, AI-powered story generation, and text-to-speech to create engaging and personalized stories for children.

## Table of Contents

* [About the Project](#about-the-project)
* [Features](#features)
* [Demonstration](#demonstration) (Optional: Add a GIF/Screenshot here)
* [Setup Instructions](#setup-instructions)
    * [Prerequisites](#prerequisites)
    * [1. Clone the Repository](#1-clone-the-repository)
    * [2. Download Vosk Model](#2-download-vosk-model)
    * [3. Install Dependencies](#3-install-dependencies)
* [Running the Application](#running-the-application)
* [Project Structure](#project-structure)
* [Customization](#customization)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgements](#acknowledgements)

## About the Project

This project aims to provide a fun and educational experience for young children by allowing them to dictate a story topic and then listen to a unique, AI-generated narrative. It seamlessly integrates several cutting-edge technologies:

* **Vosk**: For robust and offline speech-to-text transcription.
* **Hugging Face Transformers (Qwen2.5-0.5B)**: A powerful, compact language model for creative text generation.
* **Pyttsx3**: A cross-platform Text-to-Speech library to vocalize the stories.

The application is designed to be user-friendly, allowing continuous interaction for multiple stories, making it an ideal companion for bedtime stories or imaginative play.

## Features

* **🎙️ Speech-to-Text Input**: Effortlessly transcribes spoken requests into text using the Vosk library.
* **✍️ AI Story Generation**: Generates unique and imaginative stories tailored to user-provided topics, specifically crafted to be simple and engaging for 5-year-old kids.
* **🗣️ Text-to-Speech Output**: Narrates the generated stories aloud using `pyttsx3`, bringing the narratives to life.
* **🔄 Interactive Loop**: Provides a continuous storytelling experience, prompting the user for new ideas until they choose to stop.

## Demonstration

*(Optional: Replace this text with an animated GIF or a screenshot showing the application in action. This is highly recommended to quickly showcase your project's functionality.)*

Example:
![AI Storyteller Demo](path/to/your/demo.gif)

## Setup Instructions

Follow these steps to set up and run the project on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8 or higher**: You can download it from [python.org](https://www.python.org/downloads/).
* **Microphone**: A working microphone connected to your computer for speech input.

### 1. Clone the Repository

First, create a directory for your project and then navigate into it. If you're setting up a new Git repository, you can initialize it here.

```bash
# Create a project folder (if you haven't already)
mkdir ai-storyteller
cd ai-storyteller

# Initialize a Git repository (if not already done)
git init