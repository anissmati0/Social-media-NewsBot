import sys, os, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from google import genai
from google.genai.errors import APIError
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_title(article):
    response = client.models.generate_content(
    model= "gemini-3.5-flash-lite",
    contents= f"title: {article['title']}, summary: {article['summary']}. using the title and the summary generate an attractive main title, wich will be the main title of an instagram post. return just the new title with no other text, and without emojies"
    )
    return response.text

def generate_summary(article):
    response = client.models.generate_content(
    model= "gemini-3.5-flash-lite",
    contents= f"title: {article['title']}, summary: {article['summary']}. Using the title and the summary, generate an engaging Instagram post description that details the core points of the article. Include relevant hashtags, but return just the final description text with no other conversational filler or emojis."
    )
    return response.text

