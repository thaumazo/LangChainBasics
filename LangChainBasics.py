from dotenv import load_dotenv
import os
from langchain.llms import OpenAI

# Load environment variables from .env file
load_dotenv()

def main():
    # Retrieve the OpenAI API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("OpenAI API key not found. Please check your .env file.")
    
    # Initialize the OpenAI LLM with your API key
    openai_llm = OpenAI(api_key=api_key)
    
    # The prompt you want to send to the model
    prompt = "What is the capital of France?"
    
    # Generating a response from the model
    response = openai_llm(prompt)
    
    # Printing the response text
    print("Response from OpenAI:", response['choices'][0]['text'].strip())

if __name__ == "__main__":
    main()
