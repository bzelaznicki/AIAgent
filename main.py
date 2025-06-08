import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompt import system_prompt, model_name
from config import MAX_ITERATIONS

from call_function import available_functions, call_function

load_dotenv()

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise Exception("GEMINI_API_KEY is not set in the environment")

    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]
    if not args:
        raise Exception("The prompt cannot be empty")

    verbose = "--verbose" in args
    args = [arg for arg in args if arg != "--verbose"]
    prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    if verbose:
        print(f"Working on: {prompt}")

    iterations = 0
    while True:
        iterations += 1
        if iterations > MAX_ITERATIONS:
            print("Maximum iterations reached")
            sys.exit(1)

        try:
            messages, done = generate_content(client, messages, verbose)
            if done:
                break
        except Exception as e:
            print(f"Error generating content: {e}")
            break


def generate_content(client, messages, verbose):
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
            ),
        )
    except Exception as err:
        print(f"Error encountered: {err}")
        return messages, True

    if not response:
        print("No response received.")
        return messages, True

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.candidates:
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)

    if response.function_calls:
        function_call_part = response.function_calls[0]
        if function_call_part:
            resp = call_function(function_call_part, verbose)
            if not resp.parts or not resp.parts[0].function_response.response:
                raise Exception("No function response provided")
            if verbose:
                print(f"-> {resp.parts[0].function_response.response}")
            messages.append(resp)
        return messages, False
    else:
        print("Response:")
        print(response.text.strip())
        return messages, True


if __name__ == "__main__":
    main()
