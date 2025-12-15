import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
genai_model = genai.GenerativeModel("gemini-2.5-flash")
gemini_response = genai_model.generate_content("summarize the article about quantam computing in simple sentence")
print("gemini output:\n", gemini_response.text)