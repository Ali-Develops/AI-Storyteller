import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import time

# Load text generator model
def load_text_generator(model_name):
    """Loads the text generation tokenizer and model from Hugging Face."""
    print("Step 2: Loading text generation model...")
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)

        # Set pad token if not already defined for consistent generation
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        # Warm-up run to ensure everything is loaded into memory
        print("Performing warm-up run for text generation model...")
        input_ids = tokenizer("Short test.", return_tensors="pt").input_ids
        # Ensure attention_mask is created even for single input
        attention_mask = torch.ones_like(input_ids) 
        model.generate(input_ids, attention_mask=attention_mask, max_new_tokens=10)
        print("Text generation model loaded and warmed up successfully.")
        return tokenizer, model
    except Exception as e:
        print(f"Error loading text generation model: {e}")
        print("Please ensure the model name is correct and you have an active internet connection or the model is cached locally.")
        exit()

# Generate Story
def generate_story(tokenizer, text_model, prompt):
    """Generates a story based on the given prompt using the loaded text generation model."""
    print("Generating story...")
    start_time = time.perf_counter()
    
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512) # Added max_length
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    # Generate output
    output_ids = text_model.generate(
        input_ids, 
        attention_mask=attention_mask,
        max_new_tokens=300, # Max length of the generated story
        temperature=0.7,    # Controls randomness: lower means more deterministic
        top_k=40,           # Filters out less probable words
        top_p=0.9,          # Nucleus sampling: selects from the smallest set of words whose cumulative probability exceeds p
        repetition_penalty=1.2, # Reduces repetition
        do_sample=True,     # Enables sampling (otherwise greedy decoding)
        pad_token_id=tokenizer.pad_token_id # Important for batch processing and padding
    )

    story = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    print(f"\nGenerated Story:\n{story}")
    print(f"\nStory generated in {execution_time:.2f} seconds")

    return story