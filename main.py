import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args = sys.argv
    if len(args) != 2:
        print("Not enough arguments provided")
        sys.exit(1)
    promt = args[1]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=promt,
    )

    print(response.text)
    if response.usage_metadata is not None:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print("Usage metadata is not available in the response.")


if __name__ == "__main__":
    main()
