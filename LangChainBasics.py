from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

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
    prompt = "Tell me something interesting"
    
    # Generating a response from the model using invoke
    response = openai_llm.invoke(input=prompt)

    # Assuming the response structure is JSON-like and similar to OpenAI's format
    # Adjust this based on the actual structure of the response
    try:
        print("Response from OpenAI:", response)
    except (TypeError, KeyError):
        print("Failed to parse response:", response)

if __name__ == "__main__":
    main()
