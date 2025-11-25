import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_task(paragraph: str) -> str:
    """Send a paragraph to the OpenAI API and return a short summary phrase."""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You summarize tasks into short, clear, actionable phrases."
            },
            {
                "role": "user",
                "content": paragraph
            },
        ],
        max_completion_tokens=30,
    )

    return response.choices[0].message.content.strip()


def main():
    print("Task 4 - AI Task Summarizer (CLI Mode)\n")

    # ✅ Use CLI arguments instead of input()
    if len(sys.argv) > 1:
        task_descriptions = sys.argv[1:]
    else:
        # fallback sample data if no CLI text is supplied
        task_descriptions = [
            """The user needs to prepare a comprehensive final project report by gathering all documentation, screenshots, and code examples, ensuring that the formatting follows academic guidelines and that all source references are properly cited and explained in detail.""",

            """Organize and clean the entire workspace by sorting files into proper folders, deleting unnecessary temporary documents, backing up critical data to cloud storage, and ensuring the folder structure follows project naming conventions."""
        ]

    for i, description in enumerate(task_descriptions, start=1):
        summary = summarize_task(description)
        print(f"Original Task {i}: {description}\n")
        print(f"Summary {i}: {summary}")
        print("-" * 60)


if __name__ == "__main__":
    main()