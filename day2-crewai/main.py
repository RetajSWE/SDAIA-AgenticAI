import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

load_dotenv()

llm = "openrouter/openai/gpt-oss-20b:free"

researcher = Agent(
    role="Research Specialist",
    goal="Find clear and accurate information about the given topic",
    backstory=(
        "You are an experienced researcher who is skilled at gathering "
        "relevant facts and organizing them clearly."
    ),
    llm=llm,
    verbose=True,
    cache=False,
)

analyst = Agent(
    role="Data Analyst",
    goal="Analyze the research findings and identify the most important insights",
    backstory=(
        "You are a sharp analyst who is skilled at spotting patterns "
        "and identifying meaningful points within raw information."
    ),
    llm=llm,
    verbose=True,
    cache=False,
)

writer = Agent(
    role="Content Writer",
    goal="Turn the analysis into a clear, well-structured final answer",
    backstory=(
        "You are a skilled writer who can explain complex ideas "
        "in a simple and organized way."
    ),
    llm=llm,
    verbose=True,
    cache=False,
)

topic = input("Enter a research topic: ")

research_task = Task(
    description=f"""
    Research the topic: {topic}.
    Gather the key facts and information about it.
    """,
    expected_output="A clear list of the main facts and information about the topic.",
    agent=researcher,
)

analysis_task = Task(
    description="""
    Analyze the research findings and identify the most important insights.
    """,
    expected_output="A short list of the most important insights from the research.",
    agent=analyst,
)

writing_task = Task(
    description="""
    Using the analysis, write a final structured answer with:
    1. Introduction
    2. Main Findings
    3. Key Points
    4. Conclusion
    """,
    expected_output="A well-structured final answer with the four sections above.",
    agent=writer,
)

crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, writing_task],
    process=Process.sequential,
    verbose=True,
)

try:
    result = crew.kickoff()
    print("\n--- Final Answer ---\n")
    print(result)
except Exception as e:
    print(f"\nSomething went wrong while running the crew: {e}")