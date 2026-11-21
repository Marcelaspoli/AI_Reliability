import pandas as pd

tests = pd.read_csv("data/test_cases.csv")

print("AI Reliability Evaluation")
print("Total test cases:", len(tests))

for _, test in tests.iterrows():
    print("\nQuestion:", test["question"])
    print("Expected answer:", test["expected_answer"])
