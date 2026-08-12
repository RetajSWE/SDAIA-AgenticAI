Day 2 — Multi-Agent Research Team
What is this?

A multi-agent AI system built in Python using CrewAI. It receives a research topic from the user and passes it through three specialized agents: Researcher, Analyst, and Writer.

The agents work sequentially to produce a structured final answer.

This builds on Day 1 by moving from a single agent to multiple agents:

Input
↓
Researcher
↓
Analyst
↓
Writer
↓
Final Answer
Agentic AI Concepts Demonstrated
Multi-Agent System — multiple AI agents working together to complete one task.
Agent Specialization — each agent has a specific role and responsibility.
CrewAI — a framework for creating and orchestrating AI agents.
Tasks — instructions that define what each agent should accomplish.
Sequential Process — agents execute one after another, passing their work forward.
LLM — the language model used by the agents to generate their responses.
Agent Collaboration — each agent builds on the output produced by the previous agent.
Agents

1. Researcher

Role: Research Specialist

The Researcher gathers the main facts and relevant information about the given topic.

2. Analyst

Role: Data Analyst

The Analyst reviews the research findings and identifies the most important insights and key points.

3. Writer

Role: Content Writer

The Writer uses the research and analysis to produce a clear, structured final answer.

Workflow

The project uses a sequential CrewAI process:

User enters a topic
↓
Researcher gathers information
↓
Analyst identifies key insights
↓
Writer creates the final answer
↓
Structured response

Each agent focuses on one part of the problem instead of asking one agent to perform the entire task.

Project Structure
day2-crewai/
├── main.py # the multi-agent system
├── README.md # this file
├── .env # your real API key (never committed to GitHub)
├── .env.example # template showing what .env should look like
└── requirements.txt # required Python libraries
How to Run It

1. Get a free API key

This project uses OpenRouter with a free model.

Create an API key from your OpenRouter account and copy it.

2. Set up the project
   cd day2-crewai
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
3. Add your API key

Create a .env file in the project folder:

OPENROUTER_API_KEY=your_api_key_here

Do not commit the .env file to GitHub.

4. Run the project
   python main.py

The program will ask:

Enter a research topic:

For example:

Enter a research topic: Machine Learning

The topic is then passed through the three agents.

Example

Input:

Enter a research topic: Machine Learning

Process:

Researcher → gathers facts
Analyst → identifies important insights
Writer → creates the final structured answer

Output:


Introduction
...

Main Findings
...

Key Points
...

Conclusion
...
Why CrewAI?

CrewAI makes it easier to build systems where multiple specialized agents work together.

Instead of having one agent perform every step, the task is divided into smaller responsibilities:

Research → Analysis → Writing

This demonstrates an important Agentic AI concept: specialized agents can collaborate to complete a larger task.

Why OpenRouter?

OpenRouter provides access to multiple AI models through a unified API. This makes it possible to experiment with different models without significantly changing the application architecture.

For this project, a free model is used through OpenRouter to keep the project suitable for learning and experimentation without requiring a paid OpenAI API account.
