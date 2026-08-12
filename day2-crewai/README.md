# Day 2 — Multi-Agent Research Team

## What is this?

A multi-agent AI system built in Python using CrewAI. It receives a research topic from the user and passes it through three specialized agents: Researcher, Analyst, and Writer.

The agents work sequentially to produce a structured final answer.


Input
↓
Researcher
↓
Analyst
↓
Writer
↓
Final Answer

## Project Structure

day2-crewai/
├── main.py           # the multi-agent system
├── README.md         # this file
├── .env              # your real API key
├── .env.example      # template showing what .env should look like
└── requirements.txt  # required Python libraries

## How to Run It

### 1. Get a free API key

Create an API key from your OpenRouter account and copy it.

### 2. Set up the project

cd day2-crewai
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

### 3. Add your API key

Create a `.env` file in this folder:

OPENROUTER_API_KEY=your_api_key_here

Do not commit the `.env` file to GitHub.

### 4. Run it

python main.py

The program will ask:

Enter a research topic:

The topic is then passed through the three agents.

## Example

Input:

Enter a research topic: Machine Learning

Output:
<img width="1600" height="789" alt="image" src="https://github.com/user-attachments/assets/b8f639de-ce85-433c-b9ed-41d8a6aa96d0" />
<img width="1600" height="260" alt="image" src="https://github.com/user-attachments/assets/c09fc1f3-934f-4e21-9a37-50fad220423b" />


Main Findings
...

Key Points
...

Conclusion
...
