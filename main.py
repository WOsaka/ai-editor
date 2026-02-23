import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import GEMINI_MODEL, SYSTEM_PROMPT


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    # verbose = False
    # if len(args) == 3 and args[2] == "--verbose":
    #     verbose = True

    # messages = [
    #     types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    # ]

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=args.user_prompt,
        # config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
    )
    if response is None:
        raise RuntimeError("API call failed, no response received")

    if response.usage_metadata is not None:
        # and verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()
