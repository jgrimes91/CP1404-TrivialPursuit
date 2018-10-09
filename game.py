from random import choice


class Game:

    def __init__(self, questions, category):
        self.get_categories = category
        self.questions = questions
        self.score = 0
        self.current_question = ''

    def play_game(self):
        points = 0
        while points < 10:
            question = self.get_question()
            user_answer = question.ask_question()
            points = question.is_correct_answer(user_answer)
            self.score += points


    def get_random_category(self):
        categories = ["The Dark Arts", "Magical People", "Magical Objects", "Hogwarts", "Animals & Magical Creatures",
                      "Magical Spells & Potions"]
        chosen_category = choice(categories)
        return chosen_category

    # Function get_question(category, questions):
    def get_question(self, category):
        category_questions = []
        for question in self.questions:
            if category == question.category:
                category_questions.append(question)
        chosen_question = choice(category_questions)
        return chosen_question
