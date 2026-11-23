
import pandas as pd
from chatbot import answer_question

tests = pd.read_csv("data/test_cases.csv")

results = []

for _, test in tests.iterrows():
    question = test["question"]
    response = answer_question(question)

    results.append({
        "id": test["id"],
        "question": question,
        "expected_answer": test["expected_answer"],
        "actual_answer": response,
        "status": "needs_review"
    })

results = pd.DataFrame(results)
results.to_csv("data/results.csv", index=False)

print(results.to_string(index=False))
print(f"\nEvaluated {len(results)} questions.")
print("Results saved to data/results.csv")
