import random

class Question:
    def __init__(self, prompt, answers):

        self.prompt = prompt
        self.correct_answer = answers[0]

        # Mark the first answer as correct, and all the following as incorrect
        # Shuffle the order of the answers

        correct = [ True ] + [ False ] * (len(answers) - 1)     # This will create a list in the form [True, False, False...]
        answers_correct = list(zip(answers, correct))           # Use tuples to mark the first as correct and the rest as incorrect
        random.shuffle(answers_correct)

        self.answers = answers_correct

    def __str__(self):
        return self.prompt[0:20] + "..." + str(self.answers)



# Adding this section allows us to run the question.py file on it's own
# This way we can check that it works as expected outside of the app.py file

# Without the if __name__ == "__main__": section, the code below would run
# when we import the Question class into quiz.py, which we don't want

if __name__ == "__main__":

    question1 = Question("What is 40 + 40?", ["80", "100", "20", "30"])
    print(question1.answers)
