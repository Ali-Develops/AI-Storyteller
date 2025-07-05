import time
import os
from speech_utils import init_tts, load_vosk_model, recognize_audio, text_to_speech
from text_gen_utils import load_text_generator, generate_story

# Paths
MODEL_PATH = "E:/fyp/vosk-model-small-en-us-0.15"
MODEL_NAME = "Qwen/Qwen2.5-0.5B"

if __name__ == "__main__":
    # Initialize TTS engine
    tts_engine = init_tts()

    # Load Vosk Model for speech recognition
    recognizer = load_vosk_model(MODEL_PATH)

    # Load text generator model
    tokenizer, text_model = load_text_generator(MODEL_NAME)

    while True:
        print("Welcome! Please speak a topic for the story.")
        text_to_speech(tts_engine, "Please tell me a topic for the story.")

        user_input = recognize_audio(recognizer)
        
        if user_input:
            print("Processing your input...")
            # Customize the prompt to ensure it generates content suitable for a 5-year-old.
            story_prompt = f"Tell me a short, simple, and fun story about {user_input} for a 5-year-old kid. Make it cheerful and easy to understand."
            generated_story = generate_story(tokenizer, text_model, story_prompt)
            text_to_speech(tts_engine, generated_story)

            # Ask if they want another story
            print("Would you like another story? Say 'yes' or 'no'.")
            text_to_speech(tts_engine, "Would you like another story? Say yes or no.")

            response = recognize_audio(recognizer)
            if "no" in response or "no thanks" in response: # Added "no thanks" for robustness
                print("Goodbye!")
                text_to_speech(tts_engine, "Goodbye! Have a great day.")
                break  # Exit loop
            elif "yes" in response:
                print("Great! Let's generate another story.")
            else:
                print("I didn't quite catch that. Let's try another story anyway!")