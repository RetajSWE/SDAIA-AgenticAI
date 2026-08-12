Day 3 — AI Report Generator
Overview

A simple AI-powered application that generates a research report based on a topic provided by the user and saves the generated report as a PDF file.

How It Works
User enters a topic
        ↓
AI Agent
        ↓
Generates a research report
        ↓
Python receives the response
        ↓
PDF Generator
        ↓
output/report.pdf
Project Structure
day3-pdfGenerator/
│
├── main.py
├── README.md
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
│
└── output/
    └── report.pdf
Requirements
Python
uv
OpenRouter API key
Setup

Create a .env file in the project folder:

OPENROUTER_API_KEY=your_api_key_here

Do not commit the .env file to GitHub.

Run

Install the dependencies:

uv sync

Run the application:

uv run python main.py

Enter a topic when prompted:

Enter a topic: Artificial Intelligence in Education

The generated report will be saved as:

output/report.pdf
Output

The application generates a PDF research report containing the AI-generated content for the selected topic.

output/report.pdf
Security

The API key is stored in the .env file and should never be committed to GitHub.

The .env file is included in .gitignore.