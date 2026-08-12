# Day 2 — Multi-Agent Research Team

## What is this?

A multi-agent AI system built in Python using CrewAI. It receives a research topic from the user and passes it through three specialized agents: Researcher, Analyst, and Writer.

The agents work sequentially to produce a structured final answer.


```text
Input
↓
Researcher
↓
Analyst
↓
Writer
↓
Final Answer
```

## Project Structure

```text
day2-crewai/
├── main.py           # the multi-agent system
├── README.md         # this file
├── .env              # your real API key
├── .env.example      # template showing what .env should look like
└── requirements.txt  # required Python libraries
```

## How to Run It

### 1. Get a free API key

Create an API key from your OpenRouter account and copy it.

### 2. Set up the project

```bash
cd day2-crewai
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file in this folder:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Do not commit the `.env` file to GitHub.

### 4. Run it

```bash
python main.py
```

The program will ask:

```text
Enter a research topic:
```

The topic is then passed through the three agents.

## Example

**Input:**

```text
Enter a research topic: Machine Learning
```

**Output:**
```
<img width="1600" height="789" alt="image" src="https://github.com/user-attachments/assets/94c2d30e-9864-4391-8ffc-580b8ad8bef7" />

<img width="1600" height="260" alt="image" src="https://github.com/user-attachments/assets/7dcf02f6-88ba-48a7-b1d3-ebbf12812001" />
