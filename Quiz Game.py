class Question:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer


def load_quiz_questions():
    # Define your quiz questions here
    questions = [
        Question("What is the capital of France?", ["A) Paris", "B) London", "C) Rome", "D) Madrid"], "A"),
        Question("Which planet is known as the 'Red Planet'?", ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"], "B"),
        Question("What is the largest mammal on Earth?", ["A) Elephant", "B) Whale", "C) Giraffe", "D) Lion"], "B")
        # Add more questions here
    ]
    return questions


def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions to test your knowledge.\n")


def present_quiz_questions(questions):
    score = 0
    for idx, question in enumerate(questions, start=1):
        print(f"Question {idx}: {question.question}")
        for choice in question.choices:
            print(choice)
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        if user_answer == question.correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question.correct_answer}.\n")
    return score


def main():
    questions = load_quiz_questions()
    display_welcome_message()
    score = present_quiz_questions(questions)

    print("Quiz completed!")
    print(f"Your final score: {score} out of {len(questions)}")

    if score == len(questions):
        print("Congratulations! You got all the questions right.")
    else:
        print("Keep practicing to improve your score!")


if __name__ == "__main__":
    main()
