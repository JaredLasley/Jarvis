import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
def main ():
	#creating the parsers to parse the user input and --verbose tag
	parser = argparse.ArgumentParser(description="AiAgent")
	parser.add_argument("user_prompt", type=str, help="User input prompt")
	parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
	args = parser.parse_args()
	#stores a list of the user messagges
	messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
	load_dotenv()
#get api key from environment file
	api_key = os.environ.get("GEMINI_API_KEY")
	#checkihng for missing api key
	if api_key is None:
		raise RuntimeError("No API key found. Please input api key")
	#defining the google genai objects (query is the model, and usage is for accessing usage metrics)
	client = genai.Client(api_key=api_key)
	query = client.models.generate_content(model="gemini-2.5-flash",contents=messages)
	usage = query.usage_metadata
	#printing all of the requested info if verbose flag is present
	if args.verbose:
		print(f"User prompt:{args.user_prompt}")
		print(f"Prompt tokens: {usage.prompt_token_count}")
		print(f"Response tokens: {usage.candidates_token_count}\n")
	#error handling for Failed Token API request
	if query.usage_metadata is None:
		raise RuntimeError("Failed API Request: Token counts unavailable")
	print("Response:")
	print(query.text)


if __name__ == "__main__":
    main()
