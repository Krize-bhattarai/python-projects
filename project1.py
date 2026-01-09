# Trivia Game


# List of questions
# Store the answers
# Randomly pick questions
# Ask the questions
# See if they are correct
# Keep track of the score
# Tell the user their score

import random



questions = {

    "What is the key word to define a function in Python?": "def",
    "What data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "What symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What key word is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"


}
def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}.{question}")
        user_answer = input("Your answer: ").lower().strip()

        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f'Wrong. The correct answer is: {correct_answer}.\n')
    print(f'Game Over! Thank You. Your final score is: {score}/{total_questions}')

python_trivia_game()


# Python Codes
