from question import Question

question_prompts = [
    "What is a sole trader?\n(a) An individual in business, trading in his or her name, or under a trading name\n(b) A group of individuals working together as partners in business\n(c) An organisation, run by trustees, which uses its resources to fund charitable activities under its control\n\n",
    "What colour are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What colour are strawberries?\n(a) Red\n(b) Purple\n(c) Orange\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("Correct answer! Keep going!")
        else:
            print("Wrong answer! Better luck next time!")
            print("Correct answer: " + question.answer )
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)