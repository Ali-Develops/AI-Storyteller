import pyttsx3
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer

# Initialize TTS engine (pyttsx3)
def init_tts():
    """Initializes and configures the pyttsx3 Text-to-Speech engine."""
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Adjust speech rate
    
    # Get available voices
    voices = engine.getProperty("voices")
    
    # Select a voice (usually 0 for male, 1 for female - this can vary per system)
    # It's good practice to check if the voice exists before setting.
    if len(voices) > 1:
        engine.setProperty("voice", voices[1].id) # Try to set to a female voice if available
    elif len(voices) > 0:
        engine.setProperty("voice", voices[0].id) # Otherwise, use the first available voice
    
    print("TTS engine initialized.")
    return engine

# Load Vosk Model
def load_vosk_model(model_path):
    """Loads the Vosk speech recognition model."""
    print("Step 1: Loading speech recognition model...")
    try:
        model = Model(model_path)
        recognizer = KaldiRecognizer(model, 16000)
        print("Speech recognition model loaded successfully.")
        return recognizer
    except Exception as e:
        print(f"Error loading Vosk model: {e}")
        print("Please ensure the model path is correct and the model files are present.")
        exit()

# Speech Recognition Function
def recognize_audio(recognizer):
    """Listens for audio input and returns recognized text."""
    print("Listening for input...")
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1) as stream:
        while True:
            # Read data from the audio stream.
            # `overflowed` indicates if the input buffer was not processed fast enough.
            data, overflowed = stream.read(4000) 
            
            # Ensure `data` is bytes, as `stream.read` can sometimes return a memoryview.
            if isinstance(data, memoryview):
                audio_data = data.tobytes()
            else:
                audio_data = bytes(data)

            # Process the audio data with the Vosk recognizer.
            if recognizer.AcceptWaveform(audio_data):
                result = json.loads(recognizer.Result())
                recognized_text = result.get("text", "").lower()
                if recognized_text:
                    print(f"Recognized: {recognized_text}")
                    return recognized_text
            # You might want to add a timeout or a specific keyword to stop listening
            # if no speech is detected for a period.

# Convert Text to Speech
def text_to_speech(engine, text):
    """Converts the given text to speech using the provided TTS engine."""
    print("Converting text to speech...")
    engine.say(text)
    engine.runAndWait()
    print("Speech playback finished.")