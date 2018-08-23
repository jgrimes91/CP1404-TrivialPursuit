from random import shuffle
from random import choice


def main():
    questions = load_questions()
    for i in range(10):
        category = get_random_category()
        question = get_question(category, questions)
        shuffle_options = shuffle_questions(question)
        user_answer = ask_question(question, shuffle_options)
        is_correct_answer(question[1], user_answer)



def ask_question(question, answers):
    """Display questions to the user"""
    print("{}?\nA) {}\nB) {}\nC) {}".format(question, answers[0], answers[1], answers[2]))
    user_answer = ""
    while user_answer != "A" and user_answer != "B" and user_answer != "C":
        user_answer = input(">>> ")
        user_answer = user_answer.upper()

    if user_answer == "A":
        return answers[0]
    if user_answer == "B":
        return answers[1]
    else:
        return answers[2]


def load_questions():
    """Loading questions reading from a file"""
    questions = []
    question_file = open("Questions", "r")
    for line in question_file:
        question = line.strip("\n").split(",")
        questions.append(question)
    question_file.close()

    return questions


def shuffle_questions(question_row):
    """Shuffling questions"""
    options = []
    for i in range(1, 4):
        options.append(question_row[i])
    shuffle(options)
    return options


def is_correct_answer(answer, user_answer):
    if user_answer != answer:
        print("Incorrect answer!")
    else:
        print("That's correct!")


def get_random_category():
    categories = ["The Dark Arts", "Magical People", "Magical Objects", "Hogwarts", "Animals & Magical Creatures",
                  "Magical Spells & Potions"]
    chosen_category = choice(categories)
    return chosen_category

def get_question(category ,questions):
    category_questions = []
    for question in questions:
        if category == question[4]:
            category_questions.append(question)
    chosen_question = choice(category_questions)

    return chosen_question


main()
