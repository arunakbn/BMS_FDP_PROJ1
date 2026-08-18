# openai_script.py
# Simple script to call OpenAI LLM API

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.")

client = OpenAI(api_key=api_key)

def call_openai_llm(prompt):
    """
    Call OpenAI LLM with a given prompt.
    
    Args:
        prompt (str): The prompt to send to the LLM
    
    Returns:
        str: The response from the LLM
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    user_prompt = "What is the capital of France?"
    print(f"Prompt: {user_prompt}")
    
    response = call_openai_llm(user_prompt)
    if response:
        print(f"Response: {response}")
    else:
        print("Failed to get a response from OpenAI API.")
