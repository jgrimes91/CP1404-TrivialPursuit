def main():

    question_file = open("Questions", "r")
    questions = [ ]

    for line in question_file.readlines():
        question = line.strip("\n").split(",")
        questions.append(question)

    print(questions)

main()