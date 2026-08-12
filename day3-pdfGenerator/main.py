import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

topic = input("Enter a topic: ")

response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a simple research report writer. Write a clear and organized report."
        },
        {
            "role": "user",
            "content": f"Write a short report about: {topic}"
        }
    ]
)

report = response.choices[0].message.content
os.makedirs("output", exist_ok=True)

pdf = canvas.Canvas("output/report.pdf", pagesize=A4)

pdf.setTitle("AI Research Report")

width, height = A4

x = 25 * mm
y = height - 25 * mm
max_width = width - (50 * mm)


def write_paragraph(text, font="Helvetica", size=11, leading=16):
    global y

    pdf.setFont(font, size)

    words = text.split()
    line = ""

    for word in words:
        test_line = f"{line} {word}".strip()

        if stringWidth(test_line, font, size) <= max_width:
            line = test_line
        else:
            pdf.drawString(x, y, line)
            y -= leading
            line = word

            if y < 25 * mm:
                pdf.showPage()
                y = height - 25 * mm
                pdf.setFont(font, size)

    if line:
        pdf.drawString(x, y, line)
        y -= leading


for line in report.split("\n"):

    line = line.strip()

    if not line:
        y -= 8
        continue

    if line.startswith("###"):
        y -= 5
        write_paragraph(
            line.replace("###", "").strip(),
            font="Helvetica-Bold",
            size=12,
            leading=18
        )

    elif line.startswith("##"):
        y -= 8
        write_paragraph(
            line.replace("##", "").strip(),
            font="Helvetica-Bold",
            size=14,
            leading=20
        )

    elif line.startswith("#"):
        y -= 10
        write_paragraph(
            line.replace("#", "").strip(),
            font="Helvetica-Bold",
            size=18,
            leading=24
        )

    else:
        write_paragraph(line)

pdf.save()

print("\nPDF created successfully: output/report.pdf")