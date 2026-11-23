
from pathlib import Path
from ollama import chat

MODEL = "gemma3:1b"


def answer_question(question):
    policies = Path("data/policies.txt").read_text()

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are SouthStar's customer support assistant. "
                    "Answer using only the company policies below. "
                    "If the answer is not in the policies, say you don't know.\n\n"
                    f"{policies}"
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        options={"temperature": 0}
    )

    return response.message.content


if __name__ == "__main__":
    question = input("Ask SouthStar a question: ")
    print("Answer:", answer_question(question))
