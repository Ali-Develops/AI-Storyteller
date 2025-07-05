
# Interactive AI Storyteller 🗣️📖✨

## A Fun and Engaging AI-Powered Narrative Experience for Kids

This project is an interactive AI storyteller that allows users, especially children, to engage in a unique storytelling experience. It utilizes speech recognition to capture spoken input, generates imaginative stories using a large language model, and narrates them aloud using text-to-speech.

Perfect for bedtime stories, creative play, or simply exploring the magic of AI, this app offers an immersive and personalized narrative journey.



## ✨ Features

- 🎙️ **Speech-to-Text Input**: Powered by **Vosk** for offline voice recognition.
- ✍️ **AI Story Generation**: Uses **Qwen2.5-0.5B** via Hugging Face Transformers to generate child-friendly stories.
- 🗣️ **Text-to-Speech Output**: Narrates stories aloud with **pyttsx3**.
- 🔁 **Interactive Loop**: Continuously engages users with new stories and input prompts.

---

## 📽️ Demonstration

*(Optional: Add a demo GIF or screenshot here for better visualization.)*

```bash
![AI Storyteller Demo](https://www.example.com/your-demo.gif)
````

---

## ⚙️ Setup Instructions

### 📋 Prerequisites

* **Python 3.8+**
* **Microphone** (required)
* **Internet** (for downloading Hugging Face models)

---

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-storyteller.git
cd ai-storyteller
```

---

### 2. Download Vosk Model

* Visit: [https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)
* Download `vosk-model-small-en-us-0.15` (or a preferred version).
* Extract it into your project folder:

```
ai-storyteller/
├── vosk-model-small-en-us-0.15/
│   └── model files...
```

> 🛠️ In `main.py`, set:

```python
MODEL_PATH = "./vosk-model-small-en-us-0.15"
```

---

### 3. Install Dependencies

```bash
# Create and activate virtual environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

---

### 🚀 Running the App

```bash
python main.py
```

Speak a topic (e.g., "a flying turtle") and listen as your personalized story is generated and narrated!

---

## 📁 Project Structure

```
ai-storyteller/
├── main.py                   # App entry point
├── speech_utils.py           # TTS and ASR (Vosk + pyttsx3)
├── text_gen_utils.py         # Hugging Face model & story generation
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── vosk-model-small-en-us-0.15/  # Vosk STT model
```

---

## 🔧 Customization

* **Speech Model**: Change `MODEL_PATH` to another Vosk model directory.
* **LLM Model**: Modify `MODEL_NAME` in `main.py` to any Hugging Face-supported model.
* **Voice Settings**: Use `speech_utils.py` to change the voice properties (`rate`, `volume`, etc.).

---

## 🧰 Troubleshooting

| Issue                     | Fix                                                           |
| ------------------------- | ------------------------------------------------------------- |
| **Mic/Audio not working** | Check system mic/speaker permissions & volume                 |
| **Vosk model not found**  | Ensure correct model path in `main.py`                        |
| **Model download fails**  | Use `huggingface-cli login` if needed                         |
| **Missing modules**       | Run `pip install -r requirements.txt` in activated virtualenv |

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m 'feat: Add something cool'`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* [Vosk](https://alphacephei.com/vosk/)
* [Hugging Face Transformers](https://huggingface.co/)
* [pyttsx3](https://pypi.org/project/pyttsx3/)


