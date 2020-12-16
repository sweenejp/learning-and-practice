import datetime
import random

from timestuff.questions import Add, Multiply


class Quiz:
    questions = []
    answers = []
    user_responses = []
    start_time = 0
    end_time = 0

    def __init__(self):
        question_types = (Add, Multiply)
        for _ in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)

    def take_quiz(self):
        # log the start time
        self.start_time = datetime.datetime.now()
        # ask all of the questions
        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()
        return self.summary()

    def ask(self, question):
        correct = False
        # log the start time
        question_start = datetime.datetime.now()
        # capture the answer
        response = input("{} = ".format(question.text))
        # log the end time
        question_end = datetime.datetime.now()
        # if the answer is right, send back true
        if response == str(question.answer):
            correct = True
        return correct, question_end - question_start

    def total_correct(self):
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        # print how many you got right and the total # of questions. ie 5/10
        print("You got {}/{} correct".format(self.total_correct(), len(self.questions)))
        # print the total time for the quiz
        print("It took you {} seconds total.".format(round((self.end_time -
                                                            self.start_time).seconds)))
        print("Here is a detailed summary:")
        for item in self.answers:
            print("{} and it took {}".format(item[0], item[1].seconds))


new_quiz = Quiz()
new_quiz.take_quiz()
