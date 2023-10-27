from Claude.claude import Claude
import time
import json


# Your cookie string
cookie_string = ""
x = 1
# Initialize the Claude instance with your cookie
claude_instance = Claude(cookie_string)

# List of questions (add all your 60 questions here)
questions = [
    "What is the most common type of Thyristor?",
    "How does a thyristor work?",
    "What is the Thyristor?",
    "What is the symbol for an inductor?"
]

for index, question in enumerate(questions, 1):  # Start numbering from 1
    formatted_question = f"In one sentence, answer this: {question} Provide a source URL for the answer you give."
    response = claude_instance.get_answer(formatted_question)

    try:
        # Attempt to parse the response string into a dictionary
        response_dict = json.loads(response)

        # Display the number, question, and answer
        print(f"{index}. Question: {question}")
        print(f"   Answer: {response_dict['answer']}")
        print(f"   Source URL: {response_dict['source']}")

        # Optional: Add a separator for clarity
        print("-" * 50)

    except json.JSONDecodeError:

        # If parsing fails, print the raw response for inspection
        print(f" {x} :{question}")
        print(response)
        print("-" * 50)
        x = x+1

    # Delay to avoid hitting rate limits (e.g., wait for 2 seconds between requests)
    time.sleep(2)


