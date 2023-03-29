from question import Question

import csv

with open(".\Multiple_choice_quiz\question.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    questions = []

    for row in csv_reader:
        prompt = row[0]
        correct_answer = row[1]
        wrong_answers = row[2:]
        question = Question(prompt, correct_answer, wrong_answers)
        questions.append(question)

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.correct_answer:
            score += 1
            print("Correct answer! Keep going!")
        else:
            print("Wrong answer! Better luck next time!")
            print("Correct answer: " + question.correct_answer)
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
#run_test(questions)
print(questions[0].prompt + ":" + questions[0].correct_answer)