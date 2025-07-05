Markdown

# Interactive AI Storyteller 🗣️📖✨

## A Fun and Engaging AI-Powered Narrative Experience for Kids

This project is an interactive AI storyteller that allows users, especially children, to engage in a unique storytelling experience. It utilizes speech recognition to capture spoken input, generates imaginative stories using a large language model, and then narrates these stories aloud using text-to-speech technology.

Perfect for bedtime stories, creative play, or simply exploring the magic of AI, this application provides an immersive and personalized narrative journey.

## Features

* **🎙️ Speech-to-Text Input**: Integrates the **Vosk** library for robust and offline transcription of spoken words into text, making interaction natural and hands-free.
* **✍️ AI Story Generation**: Leverages the power of **Qwen2.5-0.5B** from Hugging Face Transformers. This compact yet powerful language model generates creative, cheerful, and easy-to-understand stories specifically tailored for a 5-year-old audience based on the user's prompt.
* **🗣️ Text-to-Speech Output**: Narrates the generated stories using the `pyttsx3` library, bringing the AI-created narratives to life with an engaging voice.
* **🔄 Interactive Loop**: Provides a continuous storytelling session, prompting the user for new story ideas and offering the option to generate another story or gracefully exit.

## Demonstration

*(Optional: Consider adding a short GIF or screenshot here to visually demonstrate your project in action. This significantly enhances the README's appeal.)*

Example:
![AI Storyteller in action](https://www.example.com/your-demo-gif.gif)
*(Replace `https://www.example.com/your-demo-gif.gif` with the actual link to your GIF or image once uploaded to your repository or an external host.)*

## Setup Instructions

Follow these steps to get your Interactive AI Storyteller up and running on your local machine.

### Prerequisites

* **Python 3.8 or higher**: Download from [python.org](https://www.python.org/downloads/).
* **Microphone**: A functional microphone connected to your computer is required for speech input.
* **Internet Connection**: Required for the initial download of the Qwen2.5-0.5B model from Hugging Face.

### 1. Clone the Repository

First, navigate to the directory where you want to store your project. If you're setting up a new Git repository, you can initialize it here.

```bash
# Create a project folder (if you haven't already)
mkdir ai-storyteller
cd ai-storyteller

# Initialize a Git repository (optional, if you plan to push to GitHub)
git init

2. Download Vosk Model

The Vosk speech recognition model is crucial for the application's speech-to-text capabilities and needs to be downloaded separately.

    Go to the Vosk Models page.

    Download the vosk-model-small-en-us-0.15 archive (or a more recent, small English model suitable for your needs).

    Extract the contents of the downloaded archive. This will typically create a folder named vosk-model-small-en-us-0.15.

    Place this entire extracted model folder inside your ai-storyteller project's root directory.

    Important Note: The MODEL_PATH variable defined in main.py needs to accurately point to the location of this downloaded Vosk model. While your original code used an absolute path (E:/fyp/vosk-model-small-en-us-0.15), it's highly recommended to update this in your main.py to a relative path for better portability across different systems. For example:
    Python

    # In main.py
    MODEL_PATH = "./vosk-model-small-en-us-0.15" # Assuming you placed it directly inside your project folder

3. Install Dependencies

It is highly recommended to use a Python virtual environment to manage project dependencies. This isolates your project's libraries and avoids conflicts with other Python installations.
Bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the required Python packages
pip install -r requirements.txt

Running the Application

Once all dependencies are installed and the Vosk model is in place, you can launch the Interactive AI Storyteller:
Bash

# Ensure your virtual environment is activated
python main.py

The application will verbally greet you and prompt you to speak a topic for a story. After you provide your input (e.g., "a brave knight" or "a magical forest"), it will generate a story and read it aloud. Following the story, it will ask if you'd like another. Simply respond with "yes" or "no" to continue the fun or exit the application.

Project Structure

The project is organized into modular files for better maintainability and readability:

ai-storyteller/
├── main.py                   # The main entry point and orchestrator of the application.
├── speech_utils.py           # Contains functions for Text-to-Speech (TTS) and Automatic Speech Recognition (ASR) using pyttsx3 and Vosk.
├── text_gen_utils.py         # Manages the loading of the Hugging Face LLM (Qwen2.5-0.5B) and the story generation logic.
├── requirements.txt          # Lists all the Python package dependencies.
├── README.md                 # This comprehensive project description and setup guide.
└── vosk-model-small-en-us-0.15/ # Directory containing the downloaded Vosk speech recognition model files.
    └── ... (model files like conf, graph, ivector, etc.)

Customization

You can easily customize various aspects of the storyteller:

    Vosk Model: To use a different Vosk model (e.g., a larger one for higher accuracy or a model for a different language), update the MODEL_PATH in main.py to point to the new model's directory.

    Text Generation Model: The MODEL_NAME variable in main.py currently specifies Qwen/Qwen2.5-0.5B. You can change this to another compatible Hugging Face model, such as:

        Smaller Qwen variants for less resource usage.

        microsoft/phi-2 for another compact model.

        Larger models like mistralai/Mistral-7B-Instruct-v0.2 if you have sufficient GPU memory and computational power.
        Be aware that larger models will significantly increase memory footprint and story generation time.

    TTS Voice: The init_tts() function in speech_utils.py allows you to select a different voice provided by your operating system. You can inspect engine.getProperty("voices") to see available voice IDs and names, then set engine.setProperty("voice", voices[index].id) to your preferred voice.

Troubleshooting

Here are some common issues and their solutions:

    Audio Input/Output Issues:

        Ensure your microphone and speakers are properly connected and selected as the default audio input/output devices in your operating system's sound settings.

        Check your system's volume mixer to ensure the application isn't muted and has microphone access permissions.

    Vosk Model Not Found Error:

        Verify that the vosk-model-small-en-us-0.15 folder (or your chosen Vosk model folder) is extracted directly into your project's root directory, as described in Step 2.

        Confirm that the MODEL_PATH variable in main.py is correctly set to the exact path of your Vosk model directory.

    Hugging Face Model Download Errors:

        The transformers library will download the Qwen/Qwen2.5-0.5B model the first time you run the application. Ensure you have an active and stable internet connection.

        If you encounter authentication or connection problems, try running a small test in a Python interpreter:
        Python

        from transformers import AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen2.5-0.5B')

        This can help diagnose specific network or authentication issues (e.g., if you need to run huggingface-cli login for certain models).

    ModuleNotFoundError:

        This usually means a required Python package is not installed. Ensure your virtual environment is activated (.\venv\Scripts\activate or source venv/bin/activate) before running pip install -r requirements.txt and python main.py.

Contributing

We welcome contributions to enhance the Interactive AI Storyteller! If you have ideas for new features, improvements, or bug fixes, please follow these steps:

    Fork the repository.

    Create a new branch for your feature or fix (git checkout -b feature/your-feature-name or git checkout -b bugfix/issue-description).

    Make your changes and test them thoroughly.

    Commit your changes with a clear and concise message (git commit -m 'feat: Add new awesome feature' or fix: Resolve audio input bug).

    Push to your branch (git push origin feature/your-feature-name).

    Open a Pull Request to the main branch of this repository, describing your changes in detail.

License

This project is open-sourced under the MIT License. See the LICENSE file (if you create one) for more details.

Acknowledgements

    Vosk for providing an efficient and open-source offline speech recognition toolkit.

    Hugging Face Transformers for their incredible library and pre-trained language models, making advanced NLP accessible.

    Pyttsx3 for its straightforward cross-platform Text-to-Speech capabilities.

(Last Updated: July 5, 2025)
