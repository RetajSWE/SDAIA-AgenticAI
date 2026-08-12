# Day 1 — Single Agent (Research Assistant)

## What is this?

A simple AI agent built in Python. It receives a research topic from the user,
sends it to an LLM (Large Language Model) with clear instructions, and returns
a short structured summary.

This is the simplest possible example of an AI Agent:

```
Input → Agent → Output
```

## Agentic AI Concepts Demonstrated

- **AI Agent** — a program that uses an LLM to perform a task on behalf of the user.
- **LLM (Large Language Model)** — the model that actually understands the topic
  and generates the summary (here: Llama 3.3 70B, via Groq's free API).
- **Prompt** — the instructions we give the LLM so it knows exactly what to produce.
- **Input → Agent → Output** — the core flow of any agent: receive a request,
  process it, return a useful result.

This project intentionally does **not** use any tools, frameworks, or multi-agent
logic — that comes in later days. The goal here is to understand the simplest
building block first.

## Project Structure

```
day1-single-agent/
├── main.py          # the agent's code
├── README.md         # this file
├── .env              # your real API key (never committed to GitHub)
├── .env.example       # template showing what .env should look like
└── requirements.txt   # required Python libraries
```

## How to Run It

### 1. Get a free API key
This project uses [Groq](https://console.groq.com), which offers free access
to fast, open-source LLMs (no credit card required).

1. Go to https://console.groq.com
2. Sign up / log in
3. Go to **API Keys** → create a new key
4. Copy it

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


## Why Groq (and not OpenAI)?

OpenAI's API requires a paid account. Groq offers a genuinely free tier with
strong open-source models, and its API is compatible with OpenAI's Python
library — so the code stays exactly the same, we only change the `base_url`,
the API key, and the model name. This shows an important Agentic AI idea:
**the agent's logic is separate from the LLM provider** — you can swap the
provider without changing how the agent works.