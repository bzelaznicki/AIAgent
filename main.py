import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompt import system_prompt, model_name

from call_function import available_functions


load_dotenv()
def main():
    api_key = os.environ.get("GEMINI_API_KEY")
        
    client = genai.Client(api_key=api_key)
    args = sys.argv[1:]
    if not args:
        raise Exception("The prompt cannot be empty")
    verbose = args.__contains__("--verbose")
    prompt = " ".join(args)
    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]
    if verbose:
        print(f"Working on: {prompt}")
    generate_content(client, messages, verbose)



def generate_content(client, messages, verbose):


    try:
        response = client.models.generate_content(
            model=model_name,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            )
        )
    except Exception as err:
        print(f"Error encountered: {err}")    
    if verbose: 
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    if response.function_calls:
        function_call_part = response.function_calls[0]
        if function_call_part:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:            
        print("Response:")
        print(response.text)
    
if __name__ == "__main__":
    main()