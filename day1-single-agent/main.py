import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

if not os.getenv("GROQ_API_KEY"):
    print("Error: GROQ_API_KEY is missing. Please add it to your .env file.")
    exit(1)

topic = input("Enter a research topic: ")

prompt = f"""
You are a simple research assistant.

Summarize the following topic:

{topic}

Provide:
1. A short introduction
2. Three main findings
3. Three key points
4. A short conclusion

Keep the answer clear and concise.
"""

try:
    response = client.responses.create(
        model="llama-3.3-70b-versatile",
        input=prompt
    )
    print("\n--- Research Summary ---\n")
    print(response.output_text)
except Exception as e:
    print(f"\nSomething went wrong while contacting the LLM: {e}")