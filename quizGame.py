import random

def quiz_game():
    print("Test your wits with this quiz!")
    questions = {
        "What is the output of `print('Hello, World!'[7])`?": 
        {'options': ["A) Hello", "B) W", "C) r", "D) o"],
            "answer": "B"},

        "Which of the following is NOT a valid Python data type?": 
        {"options": ["A) List", "B) Dictionary", "C) Tuple", "D) Snippet"],
            "answer": "D"},

        "In Python, which keyword is used to define a function?": {
            "options": ["A) def", "B) func", "C) define", "D) function"],
            "answer": "A"
        },
        
        "What do you call a snake that writes code?": {
            "options": ["A) A Python programmer", "B) A script-snake", 
                        "C) A code-slinger", "D) An anaconda-lyzer"],
            "answer": "A"
        },

        "Which movie features a character named 'Forrest Gump'?": {
            "options": ["A) The Shawshank Redemption", 
                        "B) Forrest Gump", 
                        "C) The Matrix", 
                        "D) Back to the Future"],
            "answer": "B"
        },
        
        "What is the name of the Python library used for data visualization?": {
            "options": ["A) Matplotlib", 
                        "B) Numpy", 
                        "C) Pandas", 
                        "D) Seaborn"],
            "answer": "A"
        },

        "In which movie does the phrase 'Here's looking at you, kid' appear?": {
            "options": ["A) Casablanca", 
                        "B) Titanic", 
                        "C) Star Wars", 
                        "D) The Godfather"],
            "answer": "A"
        },

        "What does the `len()` function do in Python?": {
            "options": ["A) Returns the length of an object",
                        "B) Creates a new list",
                        "C) Finds the largest number in a list",
                        "D) Checks if an object is empty"],
            "answer": "A"
        },

        "Why did the computer go to therapy?": {
            "options": ["A) It had too many bytes.",
                        "B) It couldn’t find its cache.",
                        "C) It had a hard drive.",
                        "D) It felt like it was losing its memory."],
            "answer": "D"
        },

        "Which of these is a popular Python web framework?": {
            "options": ["A) Flask",
                        "B) Jupyter",
                        "C) TensorFlow",
                        "D) Django"],
            "answer": "D"
        }
    }

    # Shuffle through the questions for randomness
    question_items = list(questions.items())
    random.shuffle(question_items)

    score = 0

    # Iterate through each question
    for question, data in question_items:
        print(question)
        for option in data['options']:
            print(option)
        
        answer = input('Your answer (A/B/C/D): ').upper()

        if answer == data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {data['answer']}.\n")

    # Display final score
    print(f"Your final score is: {score}/{len(questions)}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        quiz_game()

# Run the game
if __name__ == "__main__":
    quiz_game()
