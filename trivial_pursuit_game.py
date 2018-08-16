from random import shuffle


def main():
    questions = load_questions()
    for question in questions:
        shuffle_options = shuffle_questions(question)
        ask_question(question[0], shuffle_options)


def ask_question(question, answers):
    """Display questions to the user"""
    print("{}?\nA) {}\nB) {}\nC) {}".format(question, answers[0], answers[1], answers[2]))
    user_answer = ""
    while user_answer != "A" and user_answer != "B" and user_answer != "C":
        user_answer = input(">>> ")
        user_answer = user_answer.upper()

    return user_answer


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


main()
