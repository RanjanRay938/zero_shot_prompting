````markdown name=README.md url=https://github.com/RanjanRay938/zero_shot_prompting/blob/d18ffe2f19d969df7baaa075c1fbc31a8f0f00e9/README.md
# zero_shot_prompting

Small example showing how to call Google’s Gemini (via the google-generativeai client) from Python for simple zero-shot prompting.

## What this repo contains
- zero_shot_prompting.py — minimal script that configures the client and generates content from the `gemini-2.5-flash` model.

## Requirements
- Python 3.8+
- An API key for Google Generative AI
- pip packages:
  - python-dotenv
  - google-generativeai

You can install dependencies with:

pip install python-dotenv google-generativeai
```

## Setup
1. Create a `.env` file in the repo root containing:
```
GOOGLE_API_KEY=your_api_key_here
```
2. Update the prompt inside `zero_shot_prompting.py` (the script currently calls `generate_content("")`) to whatever you want to ask Gemini.

##output:
<img width="1292" height="196" alt="image" src="https://github.com/user-attachments/assets/52c5a345-9f9f-4da0-aae8-237954549a7f" />


## Usage
Run the script:

python zero_shot_prompting.py
```
The script will print the model's response to stdout.

## Notes
- Keep your API key secret and do not commit it to source control.
- This is a minimal example for demonstration — extend error handling, request parameters, and prompt management for production use.

## License
MIT
````
