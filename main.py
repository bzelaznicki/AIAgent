import os
import sys
from dotenv import load_dotenv
from google import genai


load_dotenv()
def main():
    api_key = os.environ.get("GEMINI_API_KEY")
        
    client = genai.Client(api_key=api_key)
    args = sys.argv[1:]
    if not args:
        raise Exception("The prompt cannot be empty")
    
    prompt = " ".join(args)

    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', contents=prompt
        )
    except Exception as err:
        print(f"Error encountered: {err}")
        
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()