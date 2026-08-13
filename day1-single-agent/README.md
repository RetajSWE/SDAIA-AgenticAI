# Day 1 — Single Agent (Research Assistant)

## What is this?

A simple AI agent built in Python. It receives a research topic from the user,
sends it to an LLM, and returns a short structured summary.

```
Input → Agent → Output
```
## Project Structure

```
day1-single-agent/
├── main.py          # the agent's code
├── README.md         # this file
├── .env              # your real API key 
├── .env.example       # template showing what .env should look like
└── requirements.txt   # required Python libraries
```

## How to Run It

### 1. Get a free API key
This project uses [Groq](https://console.groq.com), which offers free access
to fast, open-source LLMs (no credit card required).

### 2. Set up the project

```bash
cd day1-single-agent
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file in this folder (copy `.env.example` and rename it):

```
GROQ_API_KEY=your_api_key_here
```

### 4. Run it

```bash
python main.py
```

## Example

**Input:**
```
Enter a research topic: Agentic AI
```

**Output:**
<img width="813" height="656" alt="image" src="https://github.com/user-attachments/assets/5b3f7c6c-8d55-4db1-8af1-11ce90a4ae87" />
